"""推薦関連論文をトピック8軸に分類する（キーワード辞書 + LLM ラベルのハイブリッド）。

一次分類はキーワード辞書。どの軸にも当たらなかった論文は
data/interim/unlabeled.csv に書き出し、LLM がラベル付けした結果
（labels/llm_labels.jsonl）をマージして最終ラベルとする。
LLM ラベルはリポジトリにコミットするため、API キーがなくても再現できる。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

from .dblp_common import load_config

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"
LABELS = ROOT / "labels"
REPORTS = ROOT / "reports"


def load_topics() -> dict[str, tuple[re.Pattern, re.Pattern | None]]:
    """軸ごとに (include パターン, exclude パターン) を返す。"""
    cfg = load_config("topics.yaml")["topics"]
    out = {}
    for key, spec in cfg.items():
        inc = re.compile("|".join(f"(?:{p})" for p in spec["include"]), re.IGNORECASE)
        exc = (
            re.compile("|".join(f"(?:{p})" for p in spec["exclude"]), re.IGNORECASE)
            if spec.get("exclude")
            else None
        )
        out[key] = (inc, exc)
    return out


def topic_labels(lang: str = "en") -> dict[str, str]:
    key = "label_ja" if lang == "ja" else "label"
    return {
        k: v.get(key, v["label"])
        for k, v in load_config("topics.yaml")["topics"].items()
    }


def _match(title: str, inc: re.Pattern, exc: re.Pattern | None) -> bool:
    return bool(inc.search(title)) and not (exc and exc.search(title))


def keyword_classify(titles: pd.Series) -> pd.DataFrame:
    t = titles.fillna("")
    return pd.DataFrame(
        {
            key: t.map(lambda s, i=inc, e=exc: _match(s, i, e))
            for key, (inc, exc) in load_topics().items()
        },
        index=titles.index,
    )


def load_llm_labels() -> dict[str, list[str]]:
    path = LABELS / "llm_labels.jsonl"
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rec = json.loads(line)
            out[rec["dblp_key"]] = rec["topics"]
    return out


def classify(df: pd.DataFrame) -> pd.DataFrame:
    topics = list(load_topics())
    flags = keyword_classify(df.title)
    df = pd.concat([df.reset_index(drop=True), flags.reset_index(drop=True)], axis=1)
    df["label_source"] = "keyword"
    df.loc[~flags.any(axis=1).values, "label_source"] = "unlabeled"

    llm = load_llm_labels()
    if llm:
        for i, key in enumerate(df.dblp_key):
            if key in llm and df.at[i, "label_source"] == "unlabeled":
                for t in llm[key]:
                    if t in topics:
                        df.at[i, t] = True
                df.at[i, "label_source"] = "llm" if llm[key] else "llm_other"

    df["n_topics"] = df[topics].sum(axis=1)
    df["is_other"] = df.n_topics == 0
    return df


def write_unlabeled(df: pd.DataFrame) -> Path:
    """LLM ラベリング対象（キーワードで拾えなかった推薦関連フル論文）を書き出す。"""
    target = df[
        (df.track_class == "full") & df.is_recsys & (df.label_source == "unlabeled")
    ]
    path = INTERIM / "unlabeled.csv"
    target[["dblp_key", "venue", "year", "title"]].to_csv(path, index=False)
    return path


if __name__ == "__main__":
    df = pd.read_csv(INTERIM / "dblp_entries_tracked.csv")
    df = classify(df)
    df.to_csv(INTERIM / "papers_classified.csv", index=False)

    core = df[(df.track_class == "full") & df.is_recsys]
    print(f"recsys-related full papers: {len(core)}")
    print(core.label_source.value_counts().to_string())
    print("\n=== topic hit counts (keyword pass) ===")
    for t, lab in topic_labels().items():
        print(f"  {lab:28s} {int(core[t].sum()):5d}")
    p = write_unlabeled(df)
    print(f"\nunlabeled -> {p} ({sum(1 for _ in open(p)) - 1} rows)")
