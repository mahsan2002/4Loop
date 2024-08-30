import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    database='login_Database',
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM users')

users = mycursor.fetchall()

for user in users:
    print(user)
