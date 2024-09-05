import sys

from flask import render_template, request, redirect, url_for, session

from application import app
from application.my_connector import get_users, add_user, get_user_byusername
from application.login import is_strong_password, is_strong_username
import bcrypt

def get_username():
    user = session.pop('username',None)
    if user != None:
        return session['username']
    else:
        return 'Guest'

@app.route('/')
@app.route('/home')
# @app.route('/home')
def home():
    name = get_username()
    print(name)
    return render_template('HomePage.html', title='Home', username=name)


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group='Everyone')


@app.route('/contact')
def contact_us():
    # code goes here
    name = get_username()
    return render_template('contact.html', location='Osterley', title='Contact Us', username=name)


@app.route('/aboutus')
def about_us():
    # code goes here
    name = get_username()
    return render_template('AboutUs.html', title='About us', username=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = get_username()

        username = request.form['username']
        password = request.form['password']

        logged_in_user = get_user_byusername(username)
        print(logged_in_user)
        stored_hashed_password = logged_in_user[1]
        print(stored_hashed_password)

        if bcrypt.checkpw(password.encode("utf-8"), stored_hashed_password.encode('utf-8')):

            session['username'] = username

            return render_template('HomePage.html', title="Home", username=name)

    return render_template('login.html', title="Login", username=name)


@app.route('/leaderboard')
def leaderboard():
    # code goes here
    name = get_username()
    return render_template('Leaderboard.html', title='Leaderboard', username=name)


# @app.route('/tracker')
# def tracker():
#     # code goes here
#     return render_template('tracker.html', title='Tracker')

@app.route('/tracker')
def tracker():
    # code goes here
    name = get_username()
    return render_template('tracker.html', title='Tracker', username=name)


@app.route('/users')
def all_users_from_db():
    users_from_db = get_users()
    print(users_from_db)
    return render_template('users.html', users=users_from_db, title='Database People')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    name = get_username()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password_strong = is_strong_password(password)
        username_strong = is_strong_username(username)
        # print("Is the password strong", password_strong)
        # print("Is the username strong", username_strong)

        if password_strong[0] == False or username_strong[0] == False:
            error = password_strong[1] + username_strong[1]

        else:
            # converting password to array of bytes
            bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            # Hashing the password
            hashed_password = bcrypt.hashpw(bytes, salt)

            add_user(username, hashed_password)

            return render_template('login.html', title='Login', username=name)

    return render_template('register.html', title='Register', message=error, username="Guest")

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username',None)

    return redirect(url_for("home"))
