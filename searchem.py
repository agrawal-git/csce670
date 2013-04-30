from flask import Flask, render_template, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
from models import db
from models import Friend
import models

'''initiate the app and db:'''
app    = Flask(__name__)
heroku = Heroku(app)
db.app = app
db.init_app(app)

@app.route('/')
def index():
  '''This is the homepage'''
  return render_template('index.html')


@app.route('/search/')
def search():
  '''This is the search endpoint'''
  return "this is the search page"


if __name__ == '__main__':
    app.run(debug=True)
