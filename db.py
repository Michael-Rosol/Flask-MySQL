#Simple db.py files to show columns, tables, and databases in MySQL
import mysql.connector  

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="fruits"
)

mycursor = mydb.cursor() 


mycursor.execute("CREATE TABLE Users (id INTEGER AUTO_INCREMENT PRIMARY Key, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table[0])
mycursor.execute("SHOW DATABASES")
for db in mycursor: 
    print(db)