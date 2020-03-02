import sqlite3

conn = sqlite3.connect('bikeDb.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS bikeTable ( numOfBikes integer ) """ )
c.execute("INSERT INTO bikeTable VALUES (1000)")

conn.commit()
conn.close()