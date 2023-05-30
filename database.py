import sqlite3

con = sqlite3.connect('db/lower_right.db')
cur = con.cursor()
cur.execute("SELECT * FROM a1")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()




