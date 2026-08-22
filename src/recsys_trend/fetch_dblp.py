"""DBLP から対象会議の主会議録 TOC を取得してローカルにキャッシュする。

各会議の index.xml から実在する版を列挙するため、TOC の URL を推測しない。
（KDD は 2025 年以降 volume 分割されており URL 規則が一定ではない）
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from lxml import etree

from .dblp_common import DBLP_BASE, RAW_DBLP, fetch_text, load_config, xml_parser


def list_editions(force: bool = False) -> list[dict]:
    """対象会議 × 対象年の主会議録を列挙する。"""
    cfg = load_config("venues.yaml")
    years = set(cfg["years"])
    editions: list[dict] = []

    for slug, vc in cfg["venues"].items():
        index_xml = fetch_text(
            f"{DBLP_BASE}db/conf/{slug}/index.xml",
            RAW_DBLP / slug / "index.xml",
            force=force,
        )
        tree = etree.fromstring(index_xml.encode("utf-8"), xml_parser())
        booktitle_re = re.compile(vc["main_booktitle"])

        for proc in tree.iter("proceedings"):
            booktitle = (proc.findtext("booktitle") or "").strip()
            if not booktitle_re.match(booktitle):
                continue

            key = proc.get("key", "")
            # workshop 版は <year> が実際の開催年とずれることがあるため
            # 主会議録は key 側の年（conf/kdd/2025-1 → 2025）を正とする
            key_year = re.search(r"/(\d{4})", key)
            year = int(key_year.group(1)) if key_year else int(proc.findtext("year"))
            if year not in years:
                continue

            toc_html = proc.findtext("url")
            if not toc_html:
                continue
            toc_xml = re.sub(r"\.html$", ".xml", toc_html)

            editions.append(
                {
                    "venue": vc["name"],
                    "venue_slug": slug,
                    "year": year,
                    "dblp_key": key,
                    "booktitle": booktitle,
                    "toc_url": DBLP_BASE + toc_xml,
                    "cache_path": str(RAW_DBLP / slug / Path(toc_xml).name),
                    "apply_recsys_filter": vc["apply_recsys_filter"],
                }
            )

    editions.sort(key=lambda e: (e["venue_slug"], e["year"], e["dblp_key"]))
    return editions


def fetch_all(force: bool = False) -> list[dict]:
    editions = list_editions(force=force)
    for ed in editions:
        fetch_text(ed["toc_url"], Path(ed["cache_path"]), force=force)
        print(f"  fetched {ed['venue']:7s} {ed['year']}  {ed['dblp_key']}")

    manifest = RAW_DBLP / "editions.json"
    manifest.write_text(
        json.dumps(editions, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return editions


if __name__ == "__main__":
    import sys

    eds = fetch_all(force="--force" in sys.argv)
    print(f"\n{len(eds)} editions cached under {RAW_DBLP}")
