"""キャッシュした DBLP TOC XML をパースし、論文一覧の DataFrame を作る。

TOC XML は <h2>（必要に応じて <h3>）のセクション見出しと、その直後の
<dblpcites> に属する <inproceedings> がフラットに並ぶ構造なので、
文書順に走査して直前の見出しを各論文に付与する。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd
from lxml import etree

from .dblp_common import RAW_DBLP, xml_parser

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"

# "378-382" / "1:1-1:10" / "12" などのページ表記からページ数を推定する
_PAGE_NUM = re.compile(r"(?:(\d+):)?(\d+)")


def page_count(pages: str | None) -> int | None:
    if not pages:
        return None
    parts = pages.split("-")
    nums = [_PAGE_NUM.search(p) for p in parts]
    if not nums[0]:
        return None
    if len(parts) == 1 or not nums[-1]:
        return 1
    start, end = int(nums[0].group(2)), int(nums[-1].group(2))
    return end - start + 1 if end >= start else None


def clean_title(title: str) -> str:
    return re.sub(r"\s+", " ", title).strip().rstrip(".")


def parse_edition(edition: dict) -> list[dict]:
    tree = etree.parse(str(edition["cache_path"]), xml_parser())
    root = tree.getroot()

    papers: list[dict] = []
    heading_h2 = ""
    heading_h3 = ""

    for child in root:
        if child.tag == "h2":
            heading_h2 = clean_title("".join(child.itertext()))
            heading_h3 = ""
            continue
        if child.tag == "h3":
            heading_h3 = clean_title("".join(child.itertext()))
            continue
        if child.tag != "dblpcites":
            continue

        heading = " / ".join(h for h in (heading_h2, heading_h3) if h)
        for ip in child.iter("inproceedings"):
            title = ip.findtext("title")
            if not title:
                continue
            doi = next(
                (
                    ee.text
                    for ee in ip.iter("ee")
                    if ee.text and "doi.org" in ee.text
                ),
                None,
            )
            pages = ip.findtext("pages")
            papers.append(
                {
                    "dblp_key": ip.get("key"),
                    "venue": edition["venue"],
                    "venue_slug": edition["venue_slug"],
                    "year": edition["year"],
                    "edition_key": edition["dblp_key"],
                    "title": clean_title(title),
                    "authors": "; ".join(
                        a.text for a in ip.iter("author") if a.text
                    ),
                    # 著者の同定には表記名ではなく DBLP の pid を使う
                    # （同姓同名は pid で区別される）
                    "author_pids": "; ".join(
                        a.get("pid") for a in ip.iter("author") if a.get("pid")
                    ),
                    "n_authors": sum(1 for a in ip.iter("author") if a.text),
                    "pages": pages,
                    "page_count": page_count(pages),
                    "doi": doi,
                    "track_heading": heading,
                }
            )
    return papers


def parse_all() -> pd.DataFrame:
    editions = json.loads((RAW_DBLP / "editions.json").read_text(encoding="utf-8"))
    rows: list[dict] = []
    for ed in editions:
        got = parse_edition(ed)
        rows.extend(got)
        print(f"  {ed['venue']:7s} {ed['year']}  {len(got):5d} entries")

    df = pd.DataFrame(rows).drop_duplicates(subset="dblp_key")
    INTERIM.mkdir(parents=True, exist_ok=True)
    df.to_csv(INTERIM / "dblp_entries.csv", index=False)
    return df


if __name__ == "__main__":
    df = parse_all()
    print(f"\ntotal {len(df)} entries -> {INTERIM / 'dblp_entries.csv'}")
