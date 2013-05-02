from flask import Flask, render_template, url_for, g, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
from models import db
from models import Friend
from models import Tweet
import models
from search import Search
from flask import jsonify
import random

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
  #rand  = random.randrange(0, db.session.query(Tweet).count())
  #tweet = db.session.query(Tweet)[rand]
  username = "wa3l"
  query = "south" #get it from the index page text field
  search_obj = Search(username,query)
  search_result = search_obj.search()
  # ??? how to send a list using jsonfy
  return jsonify(
    id=tweet.tweet_id,
    text=tweet.text,
    link=tweet.link,
    user_id=tweet.user_id,
    screen_name=tweet.screen_name,
    retweet_count=tweet.retweet_count,
  )


if __name__ == '__main__':
    app.run(debug=True)
