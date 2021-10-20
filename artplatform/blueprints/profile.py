from flask import Blueprint, request, render_template, redirect, url_for, abort
from flask_login import current_user
from ..database import database
from ..models.model import Post
from werkzeug import secure_filename
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
def introduction():
    return render_template('profile.html')

@app.route('/', methods=['POST'])
def introduction_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text
