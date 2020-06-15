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
query = cur.execute("select pid")

results = cur.fetchall()

for result in results:
    print(result)
    
cur.close()
con.close()
