"""論文をトラック種別（full / short / industry / other_track / excluded）に分類する。

見出し優先・ページ数フォールバックのハイブリッド。判定根拠（どのルールで
決まったか）を rule 列に残し、reports/track_mapping.md で検証できるようにする。
"""
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


def classify_row(heading: str, page_count, venue: str, cfg: dict) -> tuple[str, str]:
    """(track_class, 適用したルール名) を返す。"""
    h = heading or ""
    rules = [
        ("excluded", cfg["_excluded"], "heading:excluded"),
        ("industry", cfg["_industry"], "heading:industry"),
        ("other_track", cfg["_other"], "heading:other_track"),
        ("short", cfg["_short"], "heading:short"),
        ("full", cfg["_full"], "heading:full"),
    ]
    for label, pattern, rule in rules:
        if pattern.search(h):
            # 産業界トラックでも短い抄録（1-4ページ）は査読論文として扱わない
            if label == "industry":
                min_pg = cfg["full_paper_min_pages"].get(
                    venue, cfg["full_paper_min_pages"]["default"]
                )
                if pd.isna(page_count) or page_count < min_pg:
                    return "excluded", "heading:industry+pages:short"
            return label, rule

    min_pg = cfg["full_paper_min_pages"].get(
        venue, cfg["full_paper_min_pages"]["default"]
    )
    if pd.isna(page_count):
        return "unknown", "pages:missing"
    return ("full", "pages:full") if page_count >= min_pg else ("short", "pages:short")


def classify(df: pd.DataFrame) -> pd.DataFrame:
    raw = load_config("tracks.yaml")
    cfg = dict(raw)
    cfg["_excluded"] = _compile(raw["excluded_patterns"])
    cfg["_industry"] = _compile(raw["industry_patterns"])
    cfg["_other"] = _compile(raw["other_track_patterns"])
    cfg["_short"] = _compile(raw["short_patterns"])
    cfg["_full"] = _compile(raw["full_patterns"])

    out = df.apply(
        lambda r: classify_row(r.track_heading, r.page_count, r.venue, cfg),
        axis=1,
        result_type="expand",
    )
    df = df.copy()
    df["track_class"] = out[0]
    df["track_rule"] = out[1]
    return df


def write_mapping_report(df: pd.DataFrame) -> None:
    """全見出しと判定結果を一覧化し、人手検証できるようにする。"""
    g = (
        df.groupby(["venue", "year", "track_heading", "track_class", "track_rule"])
        .agg(n=("dblp_key", "size"), median_pages=("page_count", "median"))
        .reset_index()
        .sort_values(["venue", "year", "track_class", "n"], ascending=[1, 1, 1, 0])
    )
    lines = [
        "# トラック正規化の判定一覧",
        "",
        "DBLP の目次見出し（`<h2>`）ごとに、どのルールでどのトラック種別に",
        "判定されたかを全件示す。`config/tracks.yaml` のルールを検証するための資料。",
        "",
        "- `full`: 主研究トラックのフル論文（**本サーベイの集計対象**）",
        "- `short`: 短編・ポスター論文",
        "- `industry`: 産業界トラックのフル長論文（主集計外・別途参照用）",
        "- `other_track`: Resource / Reproducibility / Dataset など別枠の査読トラック（主集計外）",
        "- `excluded`: デモ・チュートリアル・招待講演・Doctoral Symposium 等",
        "",
        "## 種別ごとの件数",
        "",
        df.track_class.value_counts().to_frame("n").to_markdown(),
        "",
        "## 会議 × 年 × 見出しの判定結果",
        "",
        g.to_markdown(index=False),
        "",
    ]
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "track_mapping.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    df = pd.read_csv(INTERIM / "dblp_entries.csv")
    df = classify(df)
    df.to_csv(INTERIM / "dblp_entries_tracked.csv", index=False)
    write_mapping_report(df)
    print(df.track_class.value_counts().to_string())
    print()
    print(
        df[df.track_class == "full"]
        .pivot_table(index="year", columns="venue", values="dblp_key", aggfunc="count")
        .to_string()
    )
