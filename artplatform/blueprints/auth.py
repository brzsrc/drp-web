from flask import Blueprint, redirect, render_template, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from ..models.model import UserLogin
from ..database import database as db

auth = Blueprint('auth', __name__)


# check this link for help:
# https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

@auth.route('/login')
def login():
    return render_template("auth/login.html")


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    remember = True if request.form.get('remember') else False
    user = UserLogin.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('profile'))


@auth.route('/register')
def register():
    return render_template("auth/register.html")


@auth.route('/register', methods=['POST'])
def register_post():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    error = None

    user = UserLogin.query.filter_by(email=email).first()

    if not email:
        error = 'E-mail is required.'
    elif not name:
        error = 'Name is required.'
    elif not password:
        error = 'Password is required.'
    elif user:
        error = f'User {name} with E-mail address {email} is already registered.'

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    if error is None:
        new_user = UserLogin(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    flash(error)
    return redirect(url_for("auth.register"))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
