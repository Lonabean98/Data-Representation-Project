# Data Access Object (DOA) for the guitar Website


import mysql.connector
from mysql.connector import cursor

# Create the database class that will be called from the server program
class GuitarDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'datarep'
        )

# Function to create a new stock into the database called from the flask server. 
# Data is entered on the web page and  and written to the database. 
    def create(self,stock):
        cursor = self.db.cursor()
        sql = "insert into guitars (guitarmodel, price, quantity, datereceived, colour) values (%s,%s,%s,%s,%s)"
        attributes = [
            stock['guitarmodel'],
            stock['price'],
            stock['quantity'],
            stock['datereceived'],
            stock['colour'] 
        ]
        cursor.execute(sql, attributes)
        self.db.commit()
        return cursor.lastrowid

# Function to return all of the records from the database 
    def fetchAll(self):
        cursor = self.db.cursor()
        sql = 'select * from guitars'
        cursor.execute(sql)
        records = cursor.fetchall()
        returnArray = []
        for result in records:
            resultAsDict=self.ToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

# Function to find a specifc record, used when the stock update is selected on the web page, the data is returned to the webpage and displaed in the update form.
    def searchForId(self, id):
        cursor = self.db.cursor()
        sql = 'select * from guitars where id = %s'
        attributes=[id]
        cursor.execute(sql, attributes)
        result=cursor.fetchone()
        return self.ToDict(result)

# Function to update a specific stock record. The findById function returns the record to be updated and this function takes the updates and writes back to the database. 
    def update(self,stock):
        cursor = self.db.cursor()
        sql = "update guitars set guitarmodel = %s, price = %s, quantity = %s, datereceived=%s, colour=%s where id = %s"
        attributes = [
            stock['guitarmodel'],
            stock['price'],
            stock['quantity'],
            stock['datereceived'],
            stock['colour'],
            stock['id']
        ]
        cursor.execute(sql, attributes)
        self.db.commit()
        return stock

# Function to delete a specific record from the database.
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from guitars where id = %s'
        attributes=[id]
        cursor.execute(sql, attributes)
        self.db.commit()
        print('delete complete')
        return {}

# converts the records from the database to a dict type that can be written to the web page. 
    def ToDict(self, result):
        colnames = ['id','guitarmodel', 'price', 'quantity', 'datereceived', 'colour' ]
        stock = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                stock[colName] = value
            return stock

guitarDao = GuitarDAO()