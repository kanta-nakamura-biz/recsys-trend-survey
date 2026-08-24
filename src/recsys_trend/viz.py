"""集計結果から図を生成する。

配色は dataviz スキルの検証済みパレットに合わせている。
8 軸を 1 枚の折れ線に重ねると判読できず色覚多様性の基準も満たせないため、
年次推移は単色のスモールマルチプルで示し、識別は色ではなく位置と見出しが担う。
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

from .classify import topic_labels

# 図のラベルは日本語。環境によって利用可能な和文フォントが違うため、
# 見つかった最初のものを使い、ひとつも無ければ警告して欧文フォントで描く
# （その場合、日本語が豆腐になる）。
JP_FONT_CANDIDATES = [
    "Hiragino Sans", "Hiragino Kaku Gothic ProN",   # macOS
    "Yu Gothic", "YuGothic", "Meiryo", "BIZ UDGothic",  # Windows / macOS
    "Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAPGothic",  # Linux
]

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "reports" / "figures"

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e5e4e0"
BLUE = "#2a78d6"      # categorical slot 1 / 発散配色の正側
ORANGE = "#eb6834"    # categorical slot 2
RED = "#e34948"       # 発散配色の負側
MID = "#f0efec"       # 発散配色の中点（無彩色）

# 生成AI以降を分ける基準線。ChatGPT 公開は 2022-11 で、
# 2022年の会議投稿の大半はそれ以前に締め切られている。
GENAI_BOUNDARY = 2022.5


def resolve_jp_font() -> str | None:
    from matplotlib import font_manager

    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in JP_FONT_CANDIDATES:
        if name in available:
            return name
    print("  [警告] 和文フォントが見つかりません。図の日本語が正しく描画されません。\n"
          "         例: Noto Sans JP をインストールしてください。")
    return None


def setup() -> None:
    jp = resolve_jp_font()
    if jp:
        mpl.rcParams["font.family"] = [jp]
    mpl.rcParams["axes.unicode_minus"] = False
    mpl.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "text.color": INK,
        "axes.labelcolor": INK_2,
        "xtick.color": INK_2,
        "ytick.color": INK_2,
        "axes.edgecolor": GRID,
        "axes.linewidth": 0.8,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "grid.linestyle": "-",
        "font.size": 10,
        "axes.titlesize": 11,
        "figure.dpi": 160,
    })


def _despine(ax, keep=("left", "bottom")) -> None:
    for side, spine in ax.spines.items():
        spine.set_visible(side in keep)


def fig_period_change() -> Path:
    df = pd.read_csv(PROCESSED / "topic_share_by_period.csv").sort_values("delta_pp")
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    colors = [BLUE if v >= 0 else RED for v in df.delta_pp]
    bars = ax.barh(df.label, df.delta_pp, color=colors, height=0.62)

    for bar, row in zip(bars, df.itertuples()):
        off = 0.35 if row.delta_pp >= 0 else -0.35
        ax.text(row.delta_pp + off, bar.get_y() + bar.get_height() / 2,
                f"{row.delta_pp:+.1f}pt", va="center",
                ha="left" if row.delta_pp >= 0 else "right",
                color=INK_2, fontsize=9)

    ax.axvline(0, color=INK_2, linewidth=0.9)
    ax.set_xlabel("推薦論文に占めるシェアの変化（パーセントポイント）")
    ax.set_title("レコメンド研究のトピック変化\n"
                 "2019–2021年 vs 2023–2025年・主要6会議の主研究トラックのフル論文",
                 loc="left", color=INK)
    ax.set_xlim(df.delta_pp.min() - 2.5, df.delta_pp.max() + 3.5)
    ax.xaxis.grid(True); ax.set_axisbelow(True)
    _despine(ax, keep=("bottom",))
    ax.tick_params(left=False)
    fig.tight_layout()
    out = FIGURES / "fig1_period_change.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def fig_yearly_small_multiples() -> Path:
    df = pd.read_csv(PROCESSED / "topic_share_by_year.csv")
    labels = topic_labels()
    topics = list(labels)
    order = (df[topics].iloc[-1] - df[topics].iloc[0]).sort_values(ascending=False).index

    fig, axes = plt.subplots(2, 4, figsize=(11.5, 5.4), sharex=True, sharey=True)
    ymax = df[topics].max().max() * 1.15

    for ax, topic in zip(axes.ravel(), order):
        ax.axvspan(GENAI_BOUNDARY, df.year.max() + 0.4, color=MID, zorder=0)
        ax.plot(df.year, df[topic], color=BLUE, linewidth=2,
                marker="o", markersize=4.5, zorder=3)
        # 始点→終点は見出しに入れる（パネル内に置くと折れ線と重なる）
        first, last = df[topic].iloc[0], df[topic].iloc[-1]
        ax.set_title(f"{labels[topic]}\n{first:.0f}% → {last:.0f}%",
                     loc="left", color=INK, fontsize=10.5)
        ax.set_ylim(0, ymax)
        ax.set_xlim(df.year.min() - 0.4, df.year.max() + 0.4)
        ax.yaxis.grid(True); ax.set_axisbelow(True)
        _despine(ax, keep=("bottom",))
        ax.tick_params(left=False)

    for ax in axes[1]:
        ax.set_xticks(df.year)
        ax.set_xticklabels([str(y) for y in df.year], rotation=45, fontsize=8)
    for ax in axes[:, 0]:
        ax.set_ylabel("シェア（%）")

    fig.suptitle("トピック別の論文シェア推移（2019–2025年）\n"
                 "網掛けは2023年以降＝ChatGPT公開（2022年11月）後の最初の会議サイクル",
                 x=0.01, y=0.995, va="top", ha="left", color=INK, fontsize=11.5)
    fig.tight_layout(rect=(0, 0, 1, 0.965))
    out = FIGURES / "fig2_yearly_small_multiples.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def fig_venue_heatmap() -> Path:
    df = pd.read_csv(PROCESSED / "topic_share_by_venue_period.csv")
    labels = topic_labels()
    topics = list(labels)
    wide = df.pivot(index="venue", columns="period")
    delta = (wide.xs("2023-2025", level="period", axis=1)
             - wide.xs("2019-2021", level="period", axis=1))[topics]

    cmap = mpl.colors.LinearSegmentedColormap.from_list("div", [RED, MID, BLUE])
    lim = float(abs(delta.to_numpy()).max())

    fig, ax = plt.subplots(figsize=(9.2, 3.8))
    im = ax.imshow(delta.to_numpy(), cmap=cmap, vmin=-lim, vmax=lim, aspect="auto")
    ax.set_xticks(range(len(topics)))
    ax.set_xticklabels([labels[t] for t in topics], rotation=30, ha="right", fontsize=9)
    ax.set_yticks(range(len(delta.index)))
    ax.set_yticklabels(delta.index)

    for i in range(delta.shape[0]):
        for j in range(delta.shape[1]):
            v = delta.iat[i, j]
            ax.text(j, i, f"{v:+.0f}", ha="center", va="center", fontsize=8.5,
                    color="#ffffff" if abs(v) > lim * 0.55 else INK_2)

    ax.set_title("会議別に見たトピックシェアの変化（パーセントポイント）\n"
                 "2019–2021年 → 2023–2025年", loc="left", color=INK)
    cb = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
    cb.outline.set_visible(False)
    cb.ax.tick_params(color=GRID)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(length=0)
    fig.tight_layout()
    out = FIGURES / "fig3_venue_heatmap.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def fig_llm_cooccurrence() -> Path:
    df = pd.read_csv(PROCESSED / "llm_cooccurrence.csv").sort_values("nonllm_share")
    y = range(len(df))
    h = 0.34
    gap = 0.02

    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    ax.barh([v + h / 2 + gap for v in y], df.llm_share, height=h, color=BLUE,
            label="LLM-based 論文のうち")
    ax.barh([v - h / 2 - gap for v in y], df.nonllm_share, height=h, color=ORANGE,
            label="それ以外の論文のうち")
    for i, row in enumerate(df.itertuples()):
        ax.text(row.llm_share + 0.5, i + h / 2 + gap, f"{row.llm_share:.0f}%",
                va="center", color=INK_2, fontsize=8.5)
        ax.text(row.nonllm_share + 0.5, i - h / 2 - gap, f"{row.nonllm_share:.0f}%",
                va="center", color=INK_2, fontsize=8.5)

    ax.set_yticks(list(y)); ax.set_yticklabels(df.label)
    ax.set_xlabel("そのトピックも併せて扱っている論文の割合（%）")
    ax.set_title("LLM-based 推薦は既存トピックとほとんど重なっていない\n"
                 "2023–2025年の推薦フル論文", loc="left", color=INK)
    ax.set_xlim(0, max(df.llm_share.max(), df.nonllm_share.max()) * 1.18)
    ax.xaxis.grid(True); ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower right", fontsize=9)
    _despine(ax, keep=("bottom",))
    ax.tick_params(left=False)
    fig.tight_layout()
    out = FIGURES / "fig4_llm_cooccurrence.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def fig_author_origin() -> Path | None:
    """2024–25年にLLM論文を書いた著者の出自別内訳。乗り換えではなく新規参入が主因。"""
    path = PROCESSED / "author_llm_origin.csv"
    if not path.exists():
        return None
    df = pd.read_csv(path).sort_values("割合(%)")
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    colors = [ORANGE if label == "元GNN勢" else BLUE for label in df["出自"]]
    bars = ax.barh(df["出自"], df["割合(%)"], color=colors, height=0.56)

    for bar, row in zip(bars, df.itertuples()):
        ax.text(row._3 + 1.2, bar.get_y() + bar.get_height() / 2,
                f"{row._3:.1f}%（{row.人数}人）", va="center", color=INK_2, fontsize=9.5)

    ax.set_xlabel("2024–25年にLLM-based論文を書いた著者795人に占める割合（%）")
    ax.set_title("LLM論文を書いた著者の内訳\n主因は新規参入。元GNN勢はGNNをやめていない",
                 loc="left", color=INK)
    ax.set_xlim(0, df["割合(%)"].max() * 1.32)
    ax.xaxis.grid(True); ax.set_axisbelow(True)
    _despine(ax, keep=("bottom",))
    ax.tick_params(left=False)
    fig.tight_layout()
    out = FIGURES / "fig7_author_origin.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def fig_arxiv() -> Path | None:
    """arXiv 側の月次シェア。件数が小さくノイズが乗るため 3 ヶ月移動平均で均す。"""
    path = PROCESSED / "arxiv_monthly.csv"
    if not path.exists():
        return None
    df = pd.read_csv(path)
    df["date"] = pd.PeriodIndex(df.month, freq="M").to_timestamp()
    labels = topic_labels()
    topics = [t for t in labels if t in df.columns]
    smooth = df[topics].rolling(3, center=True, min_periods=1).mean()
    order = (smooth.iloc[-6:].mean() - smooth.iloc[:6].mean()).sort_values(ascending=False).index

    fig, axes = plt.subplots(2, 4, figsize=(11.5, 5.4), sharex=True, sharey=True)
    ymax = smooth.max().max() * 1.15
    for ax, topic in zip(axes.ravel(), order):
        ax.axvspan(pd.Timestamp("2022-11-30"), df.date.max(), color=MID, zorder=0)
        ax.plot(df.date, smooth[topic], color=BLUE, linewidth=1.8, zorder=3)
        ax.set_title(labels[topic], loc="left", color=INK, fontsize=10.5)
        ax.set_ylim(0, ymax)
        ax.yaxis.grid(True); ax.set_axisbelow(True)
        _despine(ax, keep=("bottom",))
        ax.tick_params(left=False)
    for ax in axes[1]:
        ax.tick_params(axis="x", labelrotation=45, labelsize=8)
    for ax in axes[:, 0]:
        ax.set_ylabel("シェア（%）")

    fig.suptitle("arXiv cs.IR の推薦関連プレプリントのトピック別シェア（2019–2026年）\n"
                 "月次の推薦関連投稿に占める割合・3ヶ月移動平均／"
                 "網掛けはChatGPT公開（2022年11月）以降",
                 x=0.01, y=0.995, va="top", ha="left", color=INK, fontsize=11.5)
    fig.tight_layout(rect=(0, 0, 1, 0.955))
    out = FIGURES / "fig5_arxiv_monthly.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def fig_conference_vs_preprint() -> Path | None:
    """査読会議とプレプリントの時間差。プレプリントが先に動き、会議が後から追う。"""
    apath = PROCESSED / "arxiv_monthly.csv"
    if not apath.exists():
        return None
    conf = pd.read_csv(PROCESSED / "topic_share_by_year.csv")
    ax_df = pd.read_csv(apath)
    ax_df["year"] = ax_df.month.str[:4].astype(int)
    # 2026 は 8 月までの部分データなので、年次比較からは外す
    arxiv = ax_df[ax_df.year <= 2025].groupby("year").mean(numeric_only=True)

    labels = topic_labels()
    picks = ["llm", "graph"]
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.0), sharex=True)
    for ax, topic in zip(axes, picks):
        ax.plot(arxiv.index, arxiv[topic], color=ORANGE, linewidth=2,
                marker="o", markersize=5, label="arXiv プレプリント（cs.IR）")
        ax.plot(conf.year, conf[topic], color=BLUE, linewidth=2,
                marker="o", markersize=5, label="査読済み会議録")
        ax.set_title(labels[topic], loc="left", color=INK, fontsize=11)
        ax.set_ylim(0, max(arxiv[picks].to_numpy().max(),
                           conf[picks].to_numpy().max()) * 1.15)
        ax.set_xticks(conf.year)
        ax.tick_params(axis="x", labelrotation=45, labelsize=9)
        ax.yaxis.grid(True); ax.set_axisbelow(True)
        _despine(ax, keep=("bottom",))
        ax.tick_params(left=False)
    axes[0].set_ylabel("推薦論文に占めるシェア（%）")
    axes[0].legend(frameon=False, loc="upper left", fontsize=9)

    fig.suptitle("LLM-based ではプレプリントが先行、Graph / GNN は両者そろって減少\n"
                 "arXiv はタイトル＋要約、会議録はタイトルのみで判定しているため、"
                 "水準ではなく形状を比較する",
                 x=0.01, y=0.995, va="top", ha="left", color=INK, fontsize=11.5)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    out = FIGURES / "fig6_conference_vs_preprint.png"
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def run() -> list[Path]:
    setup()
    FIGURES.mkdir(parents=True, exist_ok=True)
    made = [fig_period_change(), fig_yearly_small_multiples(),
            fig_venue_heatmap(), fig_llm_cooccurrence()]
    for fn in (fig_author_origin, fig_arxiv, fig_conference_vs_preprint):
        out = fn()
        if out:
            made.append(out)
        else:
            print(f"  (arXiv データが未取得のため {fn.__name__} はスキップ)")
    return made


if __name__ == "__main__":
    for p in run():
        print(f"  wrote {p}")
