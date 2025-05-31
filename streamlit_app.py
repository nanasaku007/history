import plotly.express as px
import pandas as pd

# 人物データ
people_data = {
    "村上春樹": {
        "birth_year": 1949,
        "events": [
            {"year": 1979, "description": "『風の歌を聴け』"},
            {"year": 1987, "description": "『ノルウェイの森』"},
            {"year": 2006, "description": "カフカ賞受賞"},
        ]
    },
    "宮崎駿": {
        "birth_year": 1941,
        "events": [
            {"year": 1978, "description": "『未来少年コナン』"},
            {"year": 1988, "description": "『となりのトトロ』"},
            {"year": 2001, "description": "『千と千尋の神隠し』"},
        ]
    },
    "立花隆": {
        "birth_year": 1940,
        "events": [
            {"year": 1974, "description": "『田中角栄研究』"},
            {"year": 1985, "description": "『宇宙からの帰還』"},
            {"year": 1995, "description": "『脳死』討論"},
        ]
    }
}

# データフレームを構築
events = []
for name, info in people_data.items():
    birth = info["birth_year"]
    for event in info["events"]:
        events.append({
            "name": name,
            "year": event["year"],
            "age": event["year"] - birth,
            "event": event["description"]
        })

df = pd.DataFrame(events)

# ========= 西暦基準タイムライン =========
fig_year = px.scatter(
    df,
    x="year",
    y="name",
    text="event",
    title="人物ごとの年表（西暦基準）",
    labels={"year": "年", "name": "人物"},
    height=500
)
fig_year.update_traces(marker=dict(size=12), textposition='top center')
fig_year.update_layout(xaxis=dict(dtick=5))
fig_year.show()

# ========= 年齢基準タイムライン =========
fig_age = px.scatter(
    df,
    x="age",
    y="name",
    text="event",
    title="人物ごとの年表（年齢基準）",
    labels={"age": "年齢", "name": "人物"},
    height=500
)
fig_age.update_traces(marker=dict(size=12), textposition='top center')
fig_age.update_layout(xaxis=dict(dtick=5))
fig_age.show()
