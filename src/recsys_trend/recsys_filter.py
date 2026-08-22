"""汎用会議のフル論文から推薦システム関連論文を抽出する。"""
from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from .dblp_common import load_config

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"
REPORTS = ROOT / "reports"


def _compile(patterns: list[str]) -> re.Pattern:
    return re.compile("|".join(f"(?:{p})" for p in patterns), re.IGNORECASE)


def apply_filter(df: pd.DataFrame) -> pd.DataFrame:
    cfg = load_config("recsys_filter.yaml")
    venues = load_config("venues.yaml")["venues"]
    inc = _compile(cfg["include_patterns"])
    exc = _compile(cfg["exclude_patterns"])
    needs_filter = {
        v["name"] for v in venues.values() if v["apply_recsys_filter"]
    }

    df = df.copy()
    hit = df.title.fillna("").map(lambda t: bool(inc.search(t)) and not exc.search(t))
    # RecSys は会議全体が推薦研究なので無条件に対象とする
    df["is_recsys"] = hit | ~df.venue.isin(needs_filter)
    df["filter_hit"] = hit
    return df


def write_audit(df: pd.DataFrame, n_sample: int = 40, seed: int = 20260822) -> None:
    """フィルタの当たり外れを目視検証するための標本を出力する。"""
    full = df[df.track_class == "full"]
    general = full[full.venue != "RecSys"]
    hits = general[general.filter_hit].sample(
        min(n_sample, general.filter_hit.sum()), random_state=seed
    )
    misses = general[~general.filter_hit].sample(n_sample, random_state=seed)

    lines = [
        "# 推薦関連フィルタの標本監査",
        "",
        "汎用会議（SIGIR/KDD/WWW/WSDM/CIKM）のフル論文に対し、",
        "`config/recsys_filter.yaml` の語彙がどう効いているかを無作為標本で確認する。",
        "DBLP はアブストラクトを持たないためタイトルのみでの判定であり、",
        "本文で推薦を扱っていてもタイトルに現れない論文は取りこぼす。",
        "",
        f"## 抽出された論文（無作為 {len(hits)} 件）",
        "",
        hits[["venue", "year", "title"]].to_markdown(index=False),
        "",
        f"## 抽出されなかった論文（無作為 {len(misses)} 件・取りこぼし確認用）",
        "",
        misses[["venue", "year", "title"]].to_markdown(index=False),
        "",
    ]
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "recsys_filter_audit.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    df = pd.read_csv(INTERIM / "dblp_entries_tracked.csv")
    df = apply_filter(df)
    df.to_csv(INTERIM / "dblp_entries_tracked.csv", index=False)
    write_audit(df)

    full = df[df.track_class == "full"]
    print("=== full papers: recsys-related counts ===")
    print(
        full[full.is_recsys]
        .pivot_table(index="year", columns="venue", values="dblp_key", aggfunc="count")
        .to_string()
    )
    print("\n=== share of recsys-related among full papers ===")
    share = full.groupby(["year", "venue"]).is_recsys.mean().unstack() * 100
    print(share.round(1).to_string())
