# Todoapp

## How to use this repo
If you have a look at the commit history, you'll notice I have arranged all the
commits in order for you to follow the development of the Todo app step by step.
I have also created a `flask-for-restful-apis` branch for step number 10, which
turns the app into a RESTful service.

## Stack 
- Python 3.8
- Good Ol' Javascript
- [W3CSS](https://www.w3schools.com/w3css) for simple styling
- [SQLite](https://www.sqlite.org/index.html) for in memory data storage

## Pre
Make sure you have Python3.8 on your machine.

## Running the app
To run the app:
```bash
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
export FLASK_APP=artplatform/app.py
export FLASK_ENV=development
flask create_all # Create database and tables inside it
flask populate   # Populate tables with some initial data
flask run        # Spin the server
```
You can now browse to <http://localhost:5000> and see the app live.

## for future commits
anything from webgl, add build and template data under static/, rename index to gallery and puth under templates/