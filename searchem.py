from flask import Flask, render_template, url_for, g #, request, session, redirect, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku


app    = Flask(__name__)
heroku = Heroku(app)
db     = SQLAlchemy(app)



@app.route('/')
def index():
  return render_template('index.html', name="this is the main page")

@app.route('/search/')
def search():
  return "this is the search page"


if __name__ == '__main__':
    app.run(debug=True)
