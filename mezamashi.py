import streamlit as st
from datetime import datetime
import time

st.title("rise or pay")

success_count=0
fail_count=0


#メールアカウント登録
email= st.text_input("メールアドレス")

#パスワード入力
password=st.text_input("パスワード",type="password")

if st.button("ログイン"):
    if email==""or password=="":
        st.warning("メールアドレスとパスワードを入力してください")
    else:
        st.success("ログイン情報を受け取りました")
        st.write("入力されたメールアドレス:",email)

#時間と金額入力
alarm_time = st.time_input("通知する時間")
money = st.number_input("金額を入力", min_value=0)

#時間判定
placeholder = st.empty()


while True:
    now = datetime.now().time()

    if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
        placeholder.warning(f"⏰ 時間です！ 金額：{money}円")

        
        break

    placeholder.info("待機中...")
    time.sleep(1)
