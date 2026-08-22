"""著者の流れを追い、「GNN 勢が LLM に流れた」仮説を検証する。

著者の同定には DBLP の pid を用いる（表記名では同姓同名を区別できない）。
本データに現れる会議・年の範囲でしか著者を追えないため、
「新規参入」は厳密には「2019-2023 に本データの6会議で論文が無かった著者」を指す。
他分野からの流入と、単に別会議で活動していた著者とを区別できない点に注意。
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .classify import load_topics

ROOT = Path(__file__).resolve().parents[2]
INTERIM = ROOT / "data" / "interim"
PROCESSED = ROOT / "data" / "processed"

PAST = (2019, 2023)   # 生成AI以前〜過渡期
NOW = (2024, 2025)    # LLM 台頭後


def _by_author(core: pd.DataFrame) -> pd.DataFrame:
    return core.assign(pid=core.author_pids.str.split("; ")).explode("pid")


def run() -> dict[str, pd.DataFrame]:
    core = pd.read_csv(INTERIM / "papers_classified.csv").query(
        "track_class=='full' and is_recsys"
    )
    topics = list(load_topics())
    a = _by_author(core)
    past, now = a[a.year.between(*PAST)], a[a.year.between(*NOW)]

    graph_past = set(past[past.graph].pid)
    any_past = set(past.pid)
    active_now = set(now.pid)
    llm_now = set(now[now.llm].pid)

    g_act = graph_past & active_now
    o_act = (any_past - graph_past) & active_now

    migration = pd.DataFrame([
        {"群": f"{PAST[0]}-{PAST[1]} に GNN 論文あり", "継続活動": len(g_act),
         "うち LLM 論文": len(g_act & llm_now),
         "割合(%)": round(len(g_act & llm_now) / len(g_act) * 100, 1)},
        {"群": f"{PAST[0]}-{PAST[1]} に GNN 論文なし", "継続活動": len(o_act),
         "うち LLM 論文": len(o_act & llm_now),
         "割合(%)": round(len(o_act & llm_now) / len(o_act) * 100, 1)},
    ])

    origin = pd.DataFrame([
        {"出自": "元GNN勢", "人数": len(llm_now & graph_past)},
        {"出自": "既存だがGNN以外", "人数": len(llm_now & any_past - graph_past)},
        {"出自": "新規参入", "人数": len(llm_now - any_past)},
    ])
    origin["割合(%)"] = (origin.人数 / len(llm_now) * 100).round(1)

    sub = now[now.pid.isin(g_act)]
    after = pd.DataFrame({
        "元GNN勢": (sub[topics].mean() * 100).round(1),
        f"{NOW[0]}-{NOW[1]}全体": (now[topics].mean() * 100).round(1),
    })
    after["差"] = (after.iloc[:, 0] - after.iloc[:, 1]).round(1)
    after.index.name = "topic"

    retention = pd.DataFrame([
        {"群": "元GNN勢", "母数": len(graph_past), "継続": len(g_act),
         "継続率(%)": round(len(g_act) / len(graph_past) * 100, 1)},
        {"群": "それ以外", "母数": len(any_past - graph_past), "継続": len(o_act),
         "継続率(%)": round(len(o_act) / len(any_past - graph_past) * 100, 1)},
    ])

    tables = {
        "author_migration": migration,
        "author_llm_origin": origin,
        "author_exgraph_topics": after.reset_index(),
        "author_retention": retention,
    }
    PROCESSED.mkdir(parents=True, exist_ok=True)
    for name, t in tables.items():
        t.to_csv(PROCESSED / f"{name}.csv", index=False)
    return tables


if __name__ == "__main__":
    for name, t in run().items():
        print(f"\n===== {name} =====")
        print(t.to_string(index=False))
