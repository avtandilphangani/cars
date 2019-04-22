import sqlite3
conn = sqlite3.connect('gzd.db')
c = conn.cursor()
c.execute('SELECT * FROM rf_Employees')
print(c.fetchone())
conn.close()
