# Postgres SQL

import psycopg2

con = psycopg2.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
cur = con.cursor()

print(con)
query = cur.execute("select pid, state, usename,client_addr, query, query_start FROM pg_stat_activity WHERE pid in (SELECT pid from pg_locks l JOIN pg_class t on l.relation = t.oid AND t.relkind = 'r'")

results = cur.fetchall()

for result in results:
    print(result)
    
cur.close()

con.close()
