import streamlit as st
import pandas as pd
import plotly.express as px
import json

# JSONデータの読み込み
with open("data/profiles.json", encoding="utf-8") as f:
    data = json.load(f)

# Streamlit UI：人物選択
persons = st.multiselect("人物を選んでください", list(data.keys()), default=list(data.keys()))

# 表示モード切替（年齢起点／年起点）
for mode in ["年齢比較（0歳起点）", "同年比較（西暦起点）"]:
    st.subheader(mode)

    # DataFrame用リスト
    rows = []

    for person in persons:
        for event in data[person]:
            rows.append({
                "Person": person,
                "Age": event["age"],
                "Year": event["year"],
                "Event": event["event"]
            })

    df = pd.DataFrame(rows)

    # グラフ表示
    if mode == "年齢比較（0歳起点）":
        fig = px.scatter(df, x="Age", y="Person", text="Event", color="Person", title="年齢起点で比較")
    else:
        fig = px.scatter(df, x="Year", y="Person", text="Event", color="Person", title="同年起点で比較")

    fig.update_traces(marker=dict(size=12), textposition='top center')
    st.plotly_chart(fig)
