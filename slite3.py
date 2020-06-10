#SQL Lite

import sqlite3

con=sqlite3.connect("lite.db")
cur = con.cursor()

print(con)
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
cur.execute()


con.commit()
cur.close()
con.close()