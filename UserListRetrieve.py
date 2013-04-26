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
  file.write(info)
  file.write('\n')
  

file.close()
