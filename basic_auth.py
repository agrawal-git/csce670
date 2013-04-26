import tweepy
CONSUMER_KEY = 'CoepSUu9aTBDacbsSvyFdQ'
CONSUMER_SECRET = 'HfCJmpnP4kdVyl4ToBXLRu9Him5O4QrPoB3gNWYWlM'
ACCESS_KEY ='108510830-gSiBhqpAd3gZLm0fcL5ht5Yn26v20fAF0a3CiXmp'
ACCESS_SECRET =  'OoZpY2yg6t7guh8QTGQP6rjVvJz1VEhQ8CwpFiQ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  #Your consumer key and secret here
 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)  #Your access key and secret here
api = tweepy.API(auth)

user = api.get_user("TheRealCaverlee")

print len(user.friends()) # this prints at most 100

print user.screen_name
print user.followers_count
#for friend in user.friends():
#   print friend.screen_name
page = 2
timeline = api.user_timeline('@TheRealCaverlee' , count = 200,page = page)

if timeline:
    print timeline
    for tweet in timeline:
        print tweet.created_at
        print tweet.text
    page = page + 1
else:
   print "Nothing"

print page