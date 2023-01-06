import streamlit as st
import datetime
import sqlite3


def main():
    st.title("勤怠管理アプリ")
    name = st.text_input("名前を入力してください")
    st.text("日付・時刻を選択して下記のボタンを押してください")
    date = st.date_input("日付",datetime.date(2023,1,1))
    startTime = st.time_input("勤務を始めた時刻",datetime.time(0,00))
    endTime = st.time_input("勤務を終えた時刻",datetime.time(0,00))
    workPastTime = st.button("出退勤を確定する")
    st.text("出退勤の履歴を確認することができます")
    display = st.button("履歴")


    if workPastTime:
        dbname = 'main.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        inserts = [
            (name,date.year,date.month,date.day,startTime.hour,startTime.minute,endTime.hour,endTime.minute),
        ]
        cur.executemany('INSERT INTO kintai values(?, ?, ?, ?, ?, ?, ?, ?)', inserts)
        conn.commit()
        conn.close()


    if display:
        dbname = 'main.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM kintai')
        for row in cur:
            st.text(row)
        conn.close()


if __name__ == '__main__':
    main()