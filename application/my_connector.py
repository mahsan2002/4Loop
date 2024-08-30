import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     port='3306',
#     database='login_Database',
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute('SELECT * FROM users')
#
# users = mycursor.fetchall()
#
# for user in users:
#     print(user)
#     print('Username: ' + user[1])
#     print('Password: ' + user[2])


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loops"
    )

    return mydb

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "Select ID, username from db_users"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    user_list = []
    for user in result_set:
        user_list.append({'ID': user[0], 'username': user[1]})
    return user_list

def add_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO db_users (username, password) VALUES (%s, %s)"
    val = (username, password)
    cursor.execute(sql, val)

    conn.commit()