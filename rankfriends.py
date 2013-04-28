import requests
import sys
import tweepy
import math

'''
CONSUMER_KEY = 'Y7OQhFD8dLX4sSxJaTXStg'
CONSUMER_SECRET = 'vMmkEO5Uj65HPcdWiANOThm4J8xrh3jMwFmBXl1bY'
ACCESS_KEY ='108510830-4W9HuJ2EqaAaqO9yXgk9HTQmphiZpXoNxmPWGS9K'
ACCESS_SECRET =  '7NLMqlTNZJ8vYxO2aRTIaXVaPXdCS2JFkRBeqRrRrY'
'''

CONSUMER_KEY = 'CoepSUu9aTBDacbsSvyFdQ'
CONSUMER_SECRET = 'HfCJmpnP4kdVyl4ToBXLRu9Him5O4QrPoB3gNWYWlM'
ACCESS_KEY ='108510830-gSiBhqpAd3gZLm0fcL5ht5Yn26v20fAF0a3CiXmp'
ACCESS_SECRET =  'OoZpY2yg6t7guh8QTGQP6rjVvJz1VEhQ8CwpFiQ'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  #Your consumer key and secret here 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)  #Your access key and secret here
api = tweepy.API(auth)  



name = ""

def getFriends():
	user_list = []
	print "Enter User Screen name"
	username = raw_input() # TheRealCaverlee
	user = api.get_user(username) # our boss
	name = "@" + user.screen_name
	friend_info = {}
	
	'''
	  1. First make user's info
	'''
	friend_info["name"] = name
	friend_info["id"] = user.id
	friend_info["friends_cnt"] = user.friends_count
	friend_info["followers_cnt"] = user.followers_count
	friend_info["status_cnt"] = user.statuses_count
	user_list.append(friend_info)
	
	'''
	  2. Make friends info
	'''
	friend_list = user.friends()
	for friend in friend_list:
		friend_info = {}
		name = "@" + friend.screen_name
		friend_info["name"] = name
		friend_info["id"] = friend.id
		friend_info["followers_cnt"] = friend.followers_count
		friend_info["friends_cnt"] = friend.friends_count
		friend_info["status_cnt"] = friend.statuses_count
		user_list.append(friend_info)
	
	return user_list
    

'''
  rank user list by normalizing
'''
def rankFriends(friends_dict):
	normalize_followers_cnt = 0.0
	normalize_friends_cnt = 0.0
	normalize_status_cnt = 0.0
	
	for subList in friends_dict:
		subList["followers_cnt"] = 1 + math.log(float(subList["followers_cnt"])) / math.log(2)
		subList["friends_cnt"] = 1 + math.log(float(subList["friends_cnt"])) / math.log(2)
                subList["status_cnt"] = 1 + math.log(float(subList["status_cnt"])) / math.log(2)
                normalize_followers_cnt = normalize_followers_cnt + subList["followers_cnt"] * subList["followers_cnt"]
                normalize_friends_cnt = normalize_friends_cnt + subList["friends_cnt"] * subList["friends_cnt"]
                normalize_status_cnt = normalize_status_cnt + subList["status_cnt"] * subList["status_cnt"]
                
        for subList in user_list:
                subList["followers_cnt"] = subList["followers_cnt"] / (normalize_followers_cnt **(.5))
                subList["friends_cnt"] = subList["friends_cnt"] / (normalize_friends_cnt **(.5))
                subList["status_cnt"] = subList["status_cnt"] / (normalize_status_cnt **(.5))
    	
	return friends_dict
	

# To access every tweet for each friends will be heavy

def main():
	friends_dict = []
	friends_dict = getFriends()

	friends_ranked = rankFriends(friends_dict)

if __name__ == '__main__':
	main()
