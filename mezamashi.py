import streamlit as st
from datetime import datetime
import time

st.title("時間＆金額通知アプリ")

alarm_time = st.time_input("通知する時間")
money = st.number_input("金額を入力", min_value=0)

placeholder = st.empty()

while True:
    now = datetime.now().time()

    if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
        placeholder.warning(f"⏰ 時間です！ 金額：{money}円")
        break

    placeholder.info("待機中...")
    time.sleep(1)
