'''
This is a test for getting a user tweets and his friends' tweets.
'''
import twitter
from oauth  import Auth
from tweet  import Tweets
from user   import User
from models import Friend
from models import Tweet
from searchem import db

api     = Auth().api
account = User(api).get_user('wa3l')

def insert_tweets(tweets):
  for tweet in tweets:
    db.session.add(Tweet(tweet))
  db.session.commit()

# process main account's tweets:
tweets = Tweets(api).timeline(account['user_id'], account['user_id'])
insert_tweets(tweets)

# process tweets of friends:
for friend in Friend.query.all():
  tweets = Tweets(api).timeline(friend.user_id, account['user_id'])
  insert_tweets(tweets)
