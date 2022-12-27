# Progarm to create the database for the guitar shop
import mysql.connector
# import pysqlcreatetable 

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
auth_plugin='mysql_native_password'
)


cursor = db.cursor()

# Creating the database schema called datarepresentation.
cursor.execute("CREATE DATABASE datarep")

print("datarepresentation schema created")