import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    database='login_Database',
)
