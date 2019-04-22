import sqlite3
conn = sqlite3.connect('gzd.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM rf_Employees'):
    print(row)

conn.close()
print(sqlite3.version_info)

