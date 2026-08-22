PY := .venv/bin/python

.PHONY: all setup dblp arxiv classify aggregate figures audit clean-cache

all: dblp classify arxiv aggregate figures audit

setup:
	python3 -m venv .venv
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

# DBLP: 会議目次の取得 → パース → トラック分類 → 推薦関連フィルタ
dblp:
	$(PY) -m src.recsys_trend.fetch_dblp
	$(PY) -m src.recsys_trend.parse_dblp
	$(PY) -m src.recsys_trend.classify_tracks
	$(PY) -m src.recsys_trend.recsys_filter

# トピック分類（キーワード辞書 + labels/llm_labels.jsonl のマージ）
classify:
	$(PY) -m src.recsys_trend.classify

# arXiv: メタデータ取得 → 同じ辞書でトピック分類
arxiv:
	$(PY) -m src.recsys_trend.fetch_arxiv
	$(PY) -m src.recsys_trend.arxiv_topics

aggregate:
	$(PY) -m src.recsys_trend.aggregate
	$(PY) -m src.recsys_trend.author_flow

figures:
	$(PY) -m src.recsys_trend.viz

# 目視検証用のレポート（トラック分類・推薦関連フィルタ・トピック分類）
audit:
	$(PY) -m src.recsys_trend.audit

# ネットワークキャッシュのみ削除（集計結果とラベルは残す）
clean-cache:
	rm -rf data/raw
