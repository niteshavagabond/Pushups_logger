from flask import Blueprint, render_template


auth = Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return render_template('signup')

@auth.route('/login')
def login():
    return render_template('login')

@auth.route('/logout')
def logout():
    return render_template('index.html')