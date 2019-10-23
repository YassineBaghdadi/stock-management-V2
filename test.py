import sqlite3


conn = sqlite3.connect('src/db.db')
curs = conn.cursor()


curs.execute('UPDATE user SET adress = "guercif"')
conn.commit()