from flask import render_template

from application import app


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

@app.route('/login')
def login():
    # code goes here
    return render_template('login.html', title='Login Page')

@app.route('/leaderboard')
def leaderboard():
    # code goes here
    return render_template('Leaderboard.html', title='Leaderboard')

@app.route('/tracker')
def tracker():
    # code goes here
    return render_template('tracker.html', title='Tracker')
