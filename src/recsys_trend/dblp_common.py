"""DBLP 取得まわりの共通ユーティリティ。"""
from __future__ import annotations

import time
from pathlib import Path

import requests
import yaml
from lxml import etree

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
RAW_DBLP = ROOT / "data" / "raw" / "dblp"

DBLP_BASE = "https://dblp.org/"
USER_AGENT = (
    "recsys-trend-survey/0.1 (research survey; "
    "https://github.com/; contact via GitHub issues)"
)
REQUEST_INTERVAL_SEC = 1.5

_last_request_at = 0.0


def load_config(name: str) -> dict:
    with (CONFIG_DIR / name).open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def xml_parser() -> etree.XMLParser:
    """DBLP の XML は HTML 実体参照を含むため recover モードで読む。"""
    return etree.XMLParser(recover=True, resolve_entities=False, load_dtd=False)


def fetch_text(
    url: str, cache_path: Path, force: bool = False, retries: int = 5
) -> str:
    """URL を取得してキャッシュに保存する。キャッシュがあればそれを返す。

    DBLP は一時的に 503 を返すことがあるため、指数バックオフで再試行する。
    """
    if cache_path.exists() and not force:
        return cache_path.read_text(encoding="utf-8")

    global _last_request_at
    last_error: Exception | None = None

    for attempt in range(retries):
        wait = REQUEST_INTERVAL_SEC - (time.monotonic() - _last_request_at)
        if wait > 0:
            time.sleep(wait)
        try:
            resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=60)
            _last_request_at = time.monotonic()
            resp.raise_for_status()
        except requests.RequestException as exc:
            _last_request_at = time.monotonic()
            last_error = exc
            backoff = REQUEST_INTERVAL_SEC * (2**attempt)
            print(f"    [retry {attempt + 1}/{retries}] {url} ({exc}) "
                  f"— {backoff:.0f}s 待機", flush=True)
            time.sleep(backoff)
            continue

        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(resp.text, encoding="utf-8")
        return resp.text

    raise RuntimeError(f"DBLP の取得に {retries} 回失敗しました: {url}") from last_error
