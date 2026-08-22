"""arXiv プレプリントを DBLP と同じトピック辞書で分類し、月次シェアを集計する。

タイトル + アブストラクトで判定する（DBLP はタイトルのみ）ため、
arXiv 側のシェアの「水準」は DBLP 側と直接比較できない。
比較してよいのは arXiv 内部での時系列変化だけである。
頑健性確認として、タイトルのみで判定した場合の系列も併せて出力する。
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .classify import keyword_classify, load_topics

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw" / "arxiv"
PROCESSED = ROOT / "data" / "processed"


def _monthly_share(df: pd.DataFrame, text: pd.Series, topics: list[str]) -> pd.DataFrame:
    flags = keyword_classify(text)
    flags["month"] = df.month.values
    grouped = flags.groupby("month")
    share = (grouped[topics].sum().T / grouped.size() * 100).T.round(2)
    share["n_papers"] = grouped.size()
    return share.reset_index()


def run() -> dict[str, pd.DataFrame]:
    df = pd.read_csv(RAW / "arxiv_recsys.csv")
    topics = list(load_topics())

    full_text = (df.title.fillna("") + " " + df.abstract.fillna("")).astype(str)
    tables = {
        "arxiv_monthly": _monthly_share(df, full_text, topics),
        "arxiv_monthly_title_only": _monthly_share(df, df.title.fillna(""), topics),
    }
    PROCESSED.mkdir(parents=True, exist_ok=True)
    for name, t in tables.items():
        t.to_csv(PROCESSED / f"{name}.csv", index=False)
    return tables


if __name__ == "__main__":
    tables = run()
    for name, t in tables.items():
        yearly = t.assign(year=t.month.str[:4]).groupby("year").mean(numeric_only=True)
        print(f"\n===== {name} (年平均) =====")
        print(yearly.round(1).to_string())
