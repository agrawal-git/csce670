'''
 Created by Hong-hoe Kim

'''

import tweepy
'''
CONSUMER_KEY = 'CoepSUu9aTBDacbsSvyFdQ'
CONSUMER_SECRET = 'HfCJmpnP4kdVyl4ToBXLRu9Him5O4QrPoB3gNWYWlM'
ACCESS_KEY ='108510830-gSiBhqpAd3gZLm0fcL5ht5Yn26v20fAF0a3CiXmp'
ACCESS_SECRET =  'OoZpY2yg6t7guh8QTGQP6rjVvJz1VEhQ8CwpFiQ'
'''

CONSUMER_KEY = 'Y7OQhFD8dLX4sSxJaTXStg'
CONSUMER_SECRET = 'vMmkEO5Uj65HPcdWiANOThm4J8xrh3jMwFmBXl1bY'
ACCESS_KEY ='108510830-4W9HuJ2EqaAaqO9yXgk9HTQmphiZpXoNxmPWGS9K'
ACCESS_SECRET =  '7NLMqlTNZJ8vYxO2aRTIaXVaPXdCS2JFkRBeqRrRrY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  #Your consumer key and secret here
 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)  #Your access key and secret here
api = tweepy.API(auth)

user_list = []

user = api.get_user("TheRealCaverlee") # our boss
friend_info = {}
name = "@" + user.screen_name
friend_info["name"] = name
friend_info["id"] = user.id
friend_info["followers_cnt"] = user.followers_count
friend_info["friends_cnt"] = user.friends_count
friend_info["status_cnt"] = user.statuses_count
user_list.append(friend_info)
    
f = open('/Users/hong-hoegim/Dropbox/class/CPSC670/project/adamdangelo.txt', 'w')
file = open('/Users/hong-hoegim/Dropbox/class/CPSC670/project/UserInfo.txt', 'w')


## adding user's friends

friend_list = user.friends()
print len(user.friends())

for friend in user.friends():
    friend_info = {}
    name = "@" + friend.screen_name
    friend_info["name"] = name
    friend_info["id"] = friend.id
    friend_info["followers_cnt"] = friend.followers_count
    friend_info["friends_cnt"] = friend.friends_count
    friend_info["status_cnt"] = friend.statuses_count
    
    user_list.append(friend_info)

for user in user_list:
  info = ""
  info = "name:"+user["name"]
  info = info + ",id:"+str(user["id"])
  info = info + ",followers_cnt:"+str(user["followers_cnt"])
  info = info + ",friends_cnt:"+str(user["friends_cnt"])
  info = info + ",status_cnt:"+str(user["status_cnt"])
  #file.write(info)
  #file.write('\n')
  

file.close()
#print len(user.friends()) # this prints at most 100



'''
 1. Save teets per person
 Retrieve user's tweets
'''


page = 1

print user
print "Start"
NoTimeline = False
user = '@adamdangelo'
while(NoTimeline == False):
  timeline = api.user_timeline(user, count = 200,page = page)
 
  if timeline:
    for tweet in timeline:
        f.write("user:")
        f.write(user)
        f.write(",id:")
        f.write(tweet.id_str)
        f.write(",created_at:")
        f.write(str(tweet.created_at))
        f.write(",text:")
        f.write(tweet.text)
        f.write(",retweete_count:")
        f.write(str(tweet.retweet_count))
        f.write(",in_reply_to_user_id:")
        f.write(str(tweet.in_reply_to_user_id))
        f.write('\n')
    page = page + 1
  else:
   print "Nothing"
   NoTimeline = True
  

#f.close()

'''
  2. Tweets of all friends
'''

'''
for user in user_list:
 print user
 print "Start"
 NoTimeline = False
 page = 1
 while(NoTimeline == False):
  timeline = api.user_timeline(user, count = 200,page = page)
 
  if timeline:
    print timeline
    for tweet in timeline:
        stream = ""
        stream = user + ";" + str(tweet.created_at) + ";" +  tweet.text 
        f.write(stream+'\n')
    page = page + 1
  else:
   print "Nothing"
   NoTimeline = True
  
 print "End"
 
f.close()
'''
