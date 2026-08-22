"""トピックシェアを集計する。

論文数そのものは会議規模の拡大に引きずられるため、指標はすべて
「その年（またはその期間）の推薦関連フル論文に占める割合」で扱う。
マルチラベルのため、軸ごとの割合の合計は 100% を超える。
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .classify import load_topics, topic_labels

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"
PROCESSED = ROOT / "data" / "processed"

# 比較の主軸。2022 は生成AI前後の移行期にあたるため年次推移には含めるが、
# 両区間を3年ずつに揃えるため期間比較からは外す。
PERIODS = {"2019-2021": (2019, 2021), "2023-2025": (2023, 2025)}


def core_papers(df: pd.DataFrame) -> pd.DataFrame:
    """本サーベイの集計対象：主研究トラックのフル論文かつ推薦関連。"""
    return df[(df.track_class == "full") & df.is_recsys].copy()


def period_of(year: int) -> str | None:
    for name, (lo, hi) in PERIODS.items():
        if lo <= year <= hi:
            return name
    return None


def denominators(df: pd.DataFrame) -> pd.DataFrame:
    full = df[df.track_class == "full"]
    out = (
        full.groupby(["year", "venue"])
        .agg(n_full=("dblp_key", "size"), n_recsys=("is_recsys", "sum"))
        .reset_index()
    )
    out["recsys_share"] = (out.n_recsys / out.n_full * 100).round(2)
    return out


def share_by_year(core: pd.DataFrame, topics: list[str]) -> pd.DataFrame:
    grouped = core.groupby("year")
    out = (grouped[topics].sum().T / grouped.size() * 100).T
    out["n_papers"] = grouped.size()
    return out.round(2).reset_index()


def share_by_period(core: pd.DataFrame, topics: list[str]) -> pd.DataFrame:
    c = core.copy()
    c["period"] = c.year.map(period_of)
    c = c[c.period.notna()]
    grouped = c.groupby("period")
    share = (grouped[topics].sum().T / grouped.size() * 100).T

    out = share.T.round(2)
    out.columns.name = None
    out["delta_pp"] = (out["2023-2025"] - out["2019-2021"]).round(2)
    out["ratio"] = (out["2023-2025"] / out["2019-2021"]).round(2)
    out.index.name = "topic"
    out = out.reset_index()
    out.insert(1, "label", out.topic.map(topic_labels()))
    out.insert(2, "label_ja", out.topic.map(topic_labels("ja")))
    return out.sort_values("delta_pp", ascending=False)


def share_by_venue_period(core: pd.DataFrame, topics: list[str]) -> pd.DataFrame:
    c = core.copy()
    c["period"] = c.year.map(period_of)
    c = c[c.period.notna()]
    grouped = c.groupby(["venue", "period"])
    share = (grouped[topics].sum().T / grouped.size() * 100).T
    return share.round(2).reset_index()


def llm_cooccurrence(core: pd.DataFrame, topics: list[str]) -> pd.DataFrame:
    """LLM 軸が他の軸をどれだけ「吸収」しているかを見る。

    - llm_share: LLM 論文のうちその軸も扱う割合
    - nonllm_share: LLM 以外の論文のうちその軸を扱う割合（比較対照）
    """
    recent = core[core.year.between(2023, 2025)]
    llm, other = recent[recent.llm], recent[~recent.llm]
    rows = []
    for t in topics:
        if t == "llm":
            continue
        rows.append(
            {
                "topic": t,
                "label": topic_labels()[t],
                "label_ja": topic_labels("ja")[t],
                "llm_share": round(llm[t].mean() * 100, 2),
                "nonllm_share": round(other[t].mean() * 100, 2),
            }
        )
    out = pd.DataFrame(rows)
    out["diff_pp"] = (out.llm_share - out.nonllm_share).round(2)
    return out.sort_values("llm_share", ascending=False)


def run() -> dict[str, pd.DataFrame]:
    df = pd.read_csv(INTERIM / "papers_classified.csv")
    topics = list(load_topics())
    core = core_papers(df)

    tables = {
        "denominators": denominators(df),
        "topic_share_by_year": share_by_year(core, topics),
        "topic_share_by_period": share_by_period(core, topics),
        "topic_share_by_venue_period": share_by_venue_period(core, topics),
        "llm_cooccurrence": llm_cooccurrence(core, topics),
    }
    PROCESSED.mkdir(parents=True, exist_ok=True)
    for name, t in tables.items():
        t.to_csv(PROCESSED / f"{name}.csv", index=False)
    return tables


if __name__ == "__main__":
    tables = run()
    for name, t in tables.items():
        print(f"\n===== {name} =====")
        print(t.to_string(index=False))
