import streamlit as st

st.title("时空透镜：中国省域居民消费结构演化解析")
st.write("这是我在数据分析课上部署的第一个 Streamlit 云端应用。")

years = st.slider("投资年限（年）", 1, 30, 10)
rate = st.slider("年化收益率（%）", 1, 20, 5)
result = 10000 * (1 + rate / 100) ** years
st.metric("1 万元到期本息", f"{result:,.0f} 元")
