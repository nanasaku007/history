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

    rows = []
    sort_key = {}

    for person in persons:
        events = data[person]
        
        if mode == "年齢比較（0歳起点）":
            span = max(e["age"] for e in events) - min(e["age"] for e in events)
        else:  # 年起点では誕生年（最も早い year）で並べる
            span = min(e["year"] for e in events)
        
        sort_key[person] = span

        for event in events:
            rows.append({
                "Person": person,
                "Age": event["age"],
                "Year": event["year"],
                "Event": event["event"]
            })

    df = pd.DataFrame(rows)

    if mode == "年齢比較（0歳起点）":
        sorted_persons = sorted(sort_key, key=sort_key.get, reverse=True)  # age spanが大きい順
    else:
        sorted_persons = sorted(sort_key, key=sort_key.get)  # 生まれが早い順（yearが小さい順）

    df["Person"] = pd.Categorical(df["Person"], categories=sorted_persons, ordered=True)

    if mode == "年齢比較（0歳起点）":
        fig = px.scatter(df, x="Age", y="Person", text="Event", color="Person", title="年齢起点で比較")
    else:
        fig = px.scatter(df, x="Year", y="Person", text="Event", color="Person", title="同年起点で比較")

    fig.update_traces(marker=dict(size=12), textposition='top center')
    st.plotly_chart(fig)
