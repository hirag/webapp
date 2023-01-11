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
        
        dbname = 'm.db'
        conn = sqlite3.connect(dbname)
        table = "従業員"
        data = (name,)
        cur = conn.cursor()
        cur.execute('insert into 従業員(名前) values(?);',data)
        conn.commit()

        table = "日付"
        sql = f"insert into {table} (年,月,日) values(?,?,?)"
        data = (date.year,date.month,date.day,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        table = "時間"
        sql = f"insert into {table} (勤務開始時刻h,勤務開始時刻m,勤務終了時刻h,勤務終了時刻m) values(?,?,?,?)"
        data = (startTime.hour,startTime.minute,endTime.hour,endTime.minute,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        table = "勤怠"
        cur = conn.cursor()
        cur.execute("select max(従業員ID), max(日付ID), max(時間ID) from 従業員,日付,時間")
        for r in cur:
            data = r
        
        sql = f"insert into {table} (従業員ID,日付ID,時間ID) values(?,?,?)" 
        cur.execute(sql,data)
        #print(data)
        conn.commit()

        conn.close()


    if display:
        dbname = 'm.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM 勤怠')
        st.text("勤怠ID 従業員ID 日付ID 時間ID")
        for row in cur:
            st.text(row)
        cur.execute('SELECT * FROM 従業員')
        st.text("従業員ID 名前")
        for row in cur:
            st.text(row)
        cur.execute('SELECT * FROM 日付')
        st.text("日付ID 年 月 日")
        for row in cur:
            st.text(row)
        cur.execute('SELECT * FROM 時間')
        st.text("時間ID 開始(h)開始(m) 終了(h) 終了(m)")
        for row in cur:
            st.text(row)
        conn.close()


if __name__ == '__main__':
    main()