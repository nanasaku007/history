# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 年表データ（簡易例）
data = {
    "村上春樹": [
        {"age": 0, "year": 1949, "event": "誕生"},
        {"age": 29, "year": 1978, "event": "『風の歌を聴け』"},
        {"age": 39, "year": 1988, "event": "『ノルウェイの森』"}
    ],
    "立花隆": [
        {"age": 0, "year": 1940, "event": "誕生"},
        {"age": 34, "year": 1974, "event": "『田中角栄研究』"},
        {"age": 50, "year": 1990, "event": "宇宙論研究開始"}
    ]
}

# UIで人物選択
persons = st.multiselect("人物を選んでください", list(data.keys()), default=list(data.keys()))

# タイムライン表示
for mode in ["年齢比較（0歳起点）", "同年比較（西暦起点）"]:
    st.subheader(mode)
    df = pd.DataFrame()

    for person in persons:
        for event in data[person]:
            df = df.append({
                "Person": person,
                "Age": event["age"],
                "Year": event["year"],
                "Event": event["event"]
            }, ignore_index=True)

    if mode == "年齢比較（0歳起点）":
        fig = px.scatter(df, x="Age", y="Person", text="Event", color="Person", title="年齢起点で比較")
    else:
        fig = px.scatter(df, x="Year", y="Person", text="Event", color="Person", title="同年起点で比較")

    fig.update_traces(marker=dict(size=12), textposition='top center')
    st.plotly_chart(fig)
