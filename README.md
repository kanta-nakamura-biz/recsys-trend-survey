# recsys-trend-survey

レコメンドシステム研究の潮流が 2019–2021 年と 2023–2025 年（生成AI以降）で
どう変わったかを、査読済み会議録の実データで定量化する再現可能な分析。

- **分析レポート**: [`reports/analysis_report.md`](reports/analysis_report.md)
- **note 記事**: （公開後にリンクを追加）

![topic shifts](reports/figures/fig1_period_change.png)

## 何をしているか

| ソース | 対象 | 件数 |
|---|---|---|
| DBLP | RecSys / SIGIR / KDD / WWW / WSDM / CIKM の主研究トラックのフル論文（2019–2025） | 推薦関連 2,108 件 / 全 16,087 エントリ |
| arXiv | cs.IR の推薦関連プレプリント（2019-01〜2026-08） | 7,740 件 |

これらを 8 つのトピック軸（Graph / GNN、Sequential / Session-based、Causal / Debiasing、
Fairness / Explainability、Multimodal、Reinforcement Learning、
Cold-start / Federated、LLM-based）にマルチラベル分類し、期間比較・年次推移・会議別・共起を集計する。

### 設計上の判断

- **すべて比率で見る。** 会議の採択数自体が期間中に大きく増えている
  （KDD のフル論文は 2019 年 174 件 → 2025 年 551 件）ため、件数の増加を
  トレンドの拡大と読み違えないようにしている。
- **主研究トラックのフル論文だけを数える。** デモ・チュートリアル・
  Doctoral Symposium・産業界トラック・Resource / Reproducibility トラックは
  分離した。判定は見出し優先・ページ数フォールバックのハイブリッドで、
  全判定結果を [`reports/track_mapping.md`](reports/track_mapping.md) に出力して
  目視検証できるようにしてある。
- **分類はキーワード辞書 + LLM ラベリングのハイブリッド。** LLM が付けた
  ラベルは [`labels/llm_labels.jsonl`](labels/llm_labels.jsonl) としてコミット
  してあるため、**API キーがなくても第三者が同じ集計結果を再現できる**。
- **抽出語彙がトピック軸と相関しないようにしている。** 推薦関連論文の
  抽出に `debias` のような語を使うと、因果推論軸のシェアが自動的に
  押し上がってしまうため。

限界（タイトルのみでの分類、キーワード辞書の時代バイアス、トラック正規化の
恣意性など）は [レポートの §3](reports/analysis_report.md#3-限界) にまとめてある。

## 実行方法

```bash
git clone <this repo> && cd recsys-trend-survey
make setup     # .venv を作って依存パッケージを入れる
make all       # 取得 → 分類 → 集計 → 作図 → 監査レポート
```

図のラベルは日本語なので、和文フォントが必要。macOS / Windows は同梱の
フォント（ヒラギノ、游ゴシック等）が自動的に使われる。Linux などで見つからない
場合は警告が出るので、`Noto Sans JP` などをインストールしてほしい。

`uv` を使う場合:

```bash
uv venv && uv pip install -r requirements.txt
```

個別に実行することもできる:

```bash
make dblp       # DBLP 目次の取得・パース・トラック分類・推薦関連フィルタ
make classify   # トピック分類（キーワード + LLM ラベルのマージ）
make arxiv      # arXiv メタデータ取得・トピック分類
make aggregate  # シェア集計
make figures    # 図の生成
make audit      # 目視検証用レポートの生成
make clean-cache  # ネットワークキャッシュのみ削除（集計結果とラベルは残す）
```

ネットワーク取得は DBLP が約 40 版、arXiv が約 30 リクエスト。
いずれもリクエスト間隔を空けており（DBLP 1.5 秒、arXiv 3 秒）、
初回の完走に 5–10 分程度かかる。取得結果は `data/raw/` にキャッシュされ、
2 回目以降は再取得しない（`--force` で強制再取得）。

## 出力物

```
data/
  interim/papers_classified.csv   論文一覧（トラック・推薦判定・トピック付き）
  processed/                      集計結果 CSV
labels/llm_labels.jsonl           LLM が付けたラベル（再現性の要）
reports/
  analysis_report.md              分析レポート（本体）
  track_mapping.md                トラック判定の全件一覧（検証用）
  recsys_filter_audit.md          推薦関連フィルタの標本監査
  classification_audit.md         トピック分類の標本監査
  figures/                        図 6 枚
```

## データソースとライセンス

- **DBLP**: メタデータは [ODC-BY 1.0 / CC0](https://dblp.org/faq/1474679.html) で
  提供されている。本リポジトリでは取得元 XML そのものは再配布せず
  （`data/raw/` は `.gitignore`）、スクリプトで再取得できる形にしてある。
- **arXiv**: [arXiv API Terms of Use](https://info.arxiv.org/help/api/tou.html) に
  従い、リクエスト間隔を 3 秒空けている。

分析コードは MIT ライセンス。

## 免責

本リポジトリは個人による調査であり、所属組織とは無関係である。
トピック分類はキーワード辞書と LLM による自動判定を含み、
個々の論文のラベルが常に正しいことを保証するものではない。
