# program to create the guitar stock table in the datarep database. 
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="datarep",
auth_plugin='mysql_native_password'
)


cursor = db.cursor()

# create guitars table only if it does not exist already
query1="  CREATE TABLE if not exists guitars (id INT AUTO_INCREMENT PRIMARY KEY, guitarmodel VARCHAR(255), price int, quantity int, datereceived date, colour varchar(255)) " 

cursor.execute(query1)

# create example stock
query2= " Insert into guitars (guitarmodel, price, quantity, datereceived, colour) values ('Gibson Les Paul', '1700', '1', '2021/05/12', 'Red' )"

cursor.execute(query2)

db.commit()

print("Guitar table created in db")