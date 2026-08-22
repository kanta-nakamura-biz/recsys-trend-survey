"""arXiv API から cs.IR の推薦関連プレプリントのメタデータを取得する。

件数だけを問い合わせる方式（月×トピックで数百リクエスト）ではなく、
年単位でメタデータをまとめて取得し、分類はローカルで行う。
これによりリクエスト数が 1/20 になるうえ、DBLP 側と同じ
`config/topics.yaml` の正規表現で分類でき、手法を揃えられる。

ただし arXiv 側はタイトル + アブストラクトで判定するのに対し、
DBLP 側はタイトルのみである点に注意（水準は直接比較しない）。
"""
from __future__ import annotations

import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd
import requests

from .dblp_common import load_config

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw" / "arxiv"
INTERIM = ROOT / "data" / "interim"

API = "https://export.arxiv.org/api/query"
USER_AGENT = "recsys-trend-survey/0.1 (research survey)"
INTERVAL_SEC = 3.0
PAGE_SIZE = 500
NS = {"a": "http://www.w3.org/2005/Atom"}


def _get(params: dict, retries: int = 4) -> str:
    for attempt in range(retries):
        try:
            resp = requests.get(
                f"{API}?" + urllib.parse.urlencode(params),
                headers={"User-Agent": USER_AGENT},
                timeout=120,
            )
            resp.raise_for_status()
            if "<entry>" in resp.text or "totalResults" in resp.text:
                return resp.text
        except requests.RequestException:
            pass
        time.sleep(INTERVAL_SEC * (2**attempt))
    raise RuntimeError(f"arXiv query failed: {params.get('search_query')}")


def _or_clause(terms: list[str]) -> str:
    return "(" + " OR ".join(f'abs:"{t}"' for t in terms) + ")"


def _parse(xml: str) -> list[dict]:
    rows = []
    for e in ET.fromstring(xml).findall("a:entry", NS):
        rows.append({
            "arxiv_id": (e.findtext("a:id", namespaces=NS) or "").rsplit("/", 1)[-1],
            "published": e.findtext("a:published", namespaces=NS),
            "title": " ".join((e.findtext("a:title", namespaces=NS) or "").split()),
            "abstract": " ".join((e.findtext("a:summary", namespaces=NS) or "").split()),
        })
    return rows


def fetch(force: bool = False) -> pd.DataFrame:
    cache = RAW / "arxiv_recsys.csv"
    if cache.exists() and not force:
        return pd.read_csv(cache)

    cfg = load_config("arxiv.yaml")
    cat = f"cat:{cfg['category']}"
    rec = _or_clause(cfg["recsys_terms"])
    years = range(int(cfg["start"][:4]), int(cfg["end"][:4]) + 1)

    rows: list[dict] = []
    totals: list[dict] = []
    for year in years:
        span = f"submittedDate:[{year}01010000 TO {year + 1}01010000]"
        base = {"sortBy": "submittedDate", "sortOrder": "ascending"}

        xml = _get({**base, "search_query": f"{cat} AND {span}", "start": 0,
                    "max_results": 1})
        n_cat = int(ET.fromstring(xml).find(
            "{http://a9.com/-/spec/opensearch/1.1/}totalResults").text)
        totals.append({"year": year, "n_cs_ir": n_cat})
        time.sleep(INTERVAL_SEC)

        start, got = 0, 0
        while True:
            xml = _get({**base, "search_query": f"{cat} AND {span} AND {rec}",
                        "start": start, "max_results": PAGE_SIZE})
            page = _parse(xml)
            rows.extend(page)
            got += len(page)
            time.sleep(INTERVAL_SEC)
            if len(page) < PAGE_SIZE:
                break
            start += PAGE_SIZE
        print(f"  {year}: cs.IR={n_cat:5d}  recsys-related={got:5d}", flush=True)

    df = pd.DataFrame(rows).drop_duplicates(subset="arxiv_id")
    df["published"] = pd.to_datetime(df.published, format="ISO8601", utc=True)
    df["month"] = df.published.dt.tz_convert(None).dt.to_period("M").astype(str)
    df["year"] = df.published.dt.year

    RAW.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache, index=False)
    pd.DataFrame(totals).to_csv(RAW / "arxiv_category_totals.csv", index=False)
    return df


if __name__ == "__main__":
    import sys

    df = fetch(force="--force" in sys.argv)
    print(f"\n{len(df)} preprints -> {RAW / 'arxiv_recsys.csv'}")
