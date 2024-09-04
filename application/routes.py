import sys

from flask import render_template, request, redirect, url_for, session

from application import app
from application.my_connector import get_users, add_user
from application.login import is_strong_password, is_strong_username
import bcrypt


@app.route('/')
@app.route('/home')
# @app.route('/home')
def home():
    return render_template('HomePage.html', title='Home')


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group='Everyone')


@app.route('/contact')
def contact_us():
    # code goes here
    return render_template('contact.html', location='Osterley', title='Contact Us')


@app.route('/aboutus')
def about_us():
    # code goes here
    return render_template('AboutUs.html', title='About us')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        logged_in_users = get_users()

        for user in logged_in_users:

            if username == user['username'] and password == user['password']:
                return render_template('HomePage.html', title="Home")

            else:
                print('no match')

    return render_template('login.html', title="Login")


@app.route('/leaderboard')
def leaderboard():
    # code goes here
    return render_template('Leaderboard.html', title='Leaderboard')


@app.route('/tracker')
def tracker():
    # code goes here
    return render_template('tracker.html', title='Tracker')


@app.route('/users')
def all_users_from_db():
    users_from_db = get_users()
    print(users_from_db)
    return render_template('users.html', users=users_from_db, title='Database People')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password_strong = is_strong_password(password)
        username_strong = is_strong_username(username)



        if password_strong[0] == False or username_strong[0] == False:
            error = password_strong[1]

        else:
            # converting password to array of bytes
            bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            # Hashing the password
            hashed_password = bcrypt.hashpw(bytes, salt)

            shortened_hash = hashed_password[:32]

            add_user(username, shortened_hash)

            return render_template('login.html', title='Login')

    return render_template('register.html', title='Register', message=error)
