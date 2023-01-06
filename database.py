import sqlite3

dbname = 'name.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

""" cur.execute(
    'CREATE TABLE items(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, price INTEGER)'
) """

""" inserts = [
    (1, "みかん", 80),
    (2, "ぶどう", 150),
    (3, "バナナ", 60)
]

cur.executemany('INSERT INTO items values(?, ?, ?)', inserts)
cur.execute('UPDATE items SET price = 260 WHERE id = "3"')
conn.commit() """

""" st.text("現在の時刻に出退勤する方は下記のボタンを押してください")
    attendanceWorkCurrentTime = st.button("出勤")
    leavingWorkCurrentTime = st.button("退勤")
    print(f'attendanceWorkCurrentTime:{attendanceWorkCurrentTime}')
    print(f'leavingWorkCurrentTime:{leavingWorkCurrentTime}')
    st.text(dt_now.strftime('%Y年%m月%d日 %H:%M:%S')) """

# データ検索
cur.execute('SELECT * FROM name')

# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)


conn.close()