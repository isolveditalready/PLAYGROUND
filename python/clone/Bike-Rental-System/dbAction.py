import sqlite3
dbName = 'bikeDb.db'

class dbActionMe:
    def __init__(self):
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()

    def finishDbConnect(self):
        self.conn.commit()
        self.conn.close()

    def dbUpdate(self,stock):
        print(f"===============>stock is {stock}")
        sql_update_query = """update bikeTable set numOfBikes = """ + str(stock) + ";"
        self.c.execute(sql_update_query)
        self.finishDbConnect()
        return None 

    def dbRead(self):
        self.c.execute('select numOfBikes from bikeTable')
        numOfBikesExtract = self.c.fetchone()
        numOfBikesInInt =  numOfBikesExtract[0]
        self.finishDbConnect()
        return numOfBikesInInt


