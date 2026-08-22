"""分類結果を目視検証するための標本を出力する。"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .classify import load_topics, topic_labels

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"
REPORTS = ROOT / "reports"
SEED = 20260822


def write_audit(n_per_topic: int = 20) -> Path:
    df = pd.read_csv(INTERIM / "papers_classified.csv")
    core = df[(df.track_class == "full") & df.is_recsys]
    topics = list(load_topics())
    labels = topic_labels()

    lines = [
        "# トピック分類の標本監査",
        "",
        "各軸に分類された論文から無作為抽出したもの。",
        "キーワード辞書（`config/topics.yaml`）と LLM ラベル（`labels/llm_labels.jsonl`）の",
        "判定が妥当かを目視で確認するための資料。`source` は判定の由来を示す。",
        "",
        "## 軸ごとの件数と判定の由来",
        "",
    ]
    summary = (
        core.melt(
            id_vars=["label_source"], value_vars=topics,
            var_name="topic", value_name="hit",
        )
        .query("hit")
        .pivot_table(index="topic", columns="label_source", values="hit",
                     aggfunc="size", fill_value=0)
    )
    summary.insert(0, "label", [labels[t] for t in summary.index])
    lines += [summary.to_markdown(), ""]

    for t in topics:
        hits = core[core[t]]
        sample = hits.sample(min(n_per_topic, len(hits)), random_state=SEED)
        lines += [
            f"## {labels[t]}（全 {len(hits)} 件から無作為 {len(sample)} 件）",
            "",
            sample[["venue", "year", "title", "label_source"]]
            .rename(columns={"label_source": "source"})
            .to_markdown(index=False),
            "",
        ]

    other = core[core.is_other]
    sample = other.sample(min(n_per_topic, len(other)), random_state=SEED)
    lines += [
        f"## どの軸にも該当しなかった論文（全 {len(other)} 件から無作為 {len(sample)} 件）",
        "",
        "古典的な協調フィルタリング、評価・再現性、システム効率化など、",
        "8 軸のいずれにも属さない研究がここに入る。取りこぼしがないかを確認する。",
        "",
        sample[["venue", "year", "title"]].to_markdown(index=False),
        "",
    ]

    path = REPORTS / "classification_audit.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


if __name__ == "__main__":
    print(f"wrote {write_audit()}")
