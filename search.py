import requests
import sys
import os


class Search:
	
	def __init__(self,username,query):
		self.username = username
		self.query = query
	
	def getFriends(self):
		#print "Enter User Screen name"
		username = self.username
		get_friends_url = "https://api.twitter.com/1/friends/ids.json?cursor=-1&screen_name="
		url = get_friends_url + username
		friends = requests.get(url)
		#print len(friends.json()["ids"])
		return friends.json()["ids"]

	def accessFriendsInfo(self):
		#friend_info = []
		friends_ids = self.getFriends()
		friends_dict = []
		user_lookup_url =  "https://api.twitter.com/1/users/lookup.json?user_id="
		for friend in friends_ids:
			user_lookup_url += str(friend) + ','
		user_lookup_url = user_lookup_url[:-1]
		#print user_lookup_url
		friends_info = requests.get(user_lookup_url).json()
		for friend in friends_info:
			info_dict = {}
			#friend_id = friend["id_str"]
			info_dict["id_str"] = friend["id_str"]
			info_dict["followers_count"] = friend["followers_count"]
			info_dict["friends_count"] = friend["friends_count"]
			info_dict["screen_name"] = '@' + friend["screen_name"]
			friends_dict.append(info_dict)
		#for key,value in friends_dict.items():
			#print key,value
		#print len(friends_dict)
		#print friends_dict
		return friends_dict

	def rankfriends(self):
		#based on followers count. Need to update
		friends_dict = self.accessFriendsInfo()
		friends_dict = sorted(friends_dict, key=lambda d:(d['followers_count']),reverse = True)
		#for x in friends_dict:
			#print x['screen_name'],x['followers_count']
		#print friends_dict
		user_rank = {}
		i = 1
		for friend in friends_dict:
			user_rank[friend["id_str"]] = i
			i += 1
			
		return user_rank
	
	
	def combinerank(self):
		#username = "1308ashish"
		user_rank = self.rankfriends()
		return user_rank
	
	def search(self):
		print self.combinerank()
		
def main():
	#Call the funtion to access username and search query here
	searchobj = Search("1308ashish","blah")
	searchobj.search()

if __name__ == '__main__':
	main()