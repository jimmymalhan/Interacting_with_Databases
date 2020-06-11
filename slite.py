#SQL Lite

import sqlite3

def create_tables():
    con=sqlite3.connect("lite.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    con.commit()
    con.close()
    
# Inserting Data to avoid SQL injection
def insert(item,quantity,price):
    con=sqlite3.connect("lite.db")
    cur=con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    con.commit()
    con.close()
    
# Viewing all data
def view():
    con=sqlite3.connect("lite.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    con.close()
    return rows

# delete a row of Wine Glass
def delete(item):
    con=sqlite3.connect("lite.db")
    cur=con.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    con.commit()
    con.close()
    
# Updating data
def update(quantity,price,item):
    con=sqlite3.connect("lite.db")
    cur=con.cursor()
    cur.execute("UPDATE store SET quantity=?, price=?WHERE item=?",(quantity,price,item))
    con.commit()
    con.close()

update(11,6,"Coffee Cup") #updating quanity and price values for the argument ?
#delete("Wine Glass") # Deleting Wine Glass from the row for the argument ?
print(view())
#insert("Coffee Cup",10,5) # Inserting data for the argument `?`
