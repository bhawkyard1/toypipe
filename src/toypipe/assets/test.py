import sqlite3

with sqlite3.connect("database.db") as con:
	cur = con.cursor()

    # Create table
    cur.execute('''CREATE ASSETSTACKS stocks
                   (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

	# Save (commit) the changes
	con.commit()

