from flask import escape, request, render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, login_required

@app.route('/', methods = ['Get', 'POST'])
def index():
    formsignup = RegistrationForm()
    formslogin = LoginForm()

    if formsignup.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(formsignup.password.data).decode('utf-8')
        user = User(username=formsignup.username.data, email= formsignup.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('index'))
    
    if formslogin.validate_on_submit():
        user = User.query.filter_by(email = formslogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formslogin.password.data):
            login_user(user, remember=formslogin.remember.data)
            return redirect(url_for('form'))
        
        else:
            flash('Login Unsuccesful. Please check email and password...', 'danger')

    return render_template('index.html', formsignup=formsignup, formslogin=formslogin)

@app.route('/form')
@login_required
def form():

    return render_template('form.html')