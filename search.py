import requests
import sys
import os
import re
import math


class Search:

	def __init__(self,username,query):
		self.username = username
		self.query = query

	def getTweets(self):
		dirPath   = 'tweets/'
		userPath  = 'UserInfo.txt'

		df = {} # document frequency
		idf = {}  # idf
		tf = {} # term frequency
		query_tf = {}  # term frequency of query
		docVector = []
		query = self.query.split()
		for subQuery in query:
			if(query_tf.has_key(subQuery) == False):
				query_tf[subQuery] = 1
			else:
				query_tf[subQuery] = query_tf[subQuery] + 1

		for subString in query_tf:
			query_tf[subString] = 1 + math.log(query_tf[subString]) / math.log(2)

		cnt = 0


		for filename in os.listdir(dirPath):
			if(filename != '.DS_Store'):
				f = open(dirPath + "/" + filename, 'r')

				for line in f:
				  docInfo = {}
				  cnt = cnt + 1
				  checkDF = []
				  text = ""
				  user = ""
				  id = ""
				  created_at = ""
				  retweet_count = ""
				  in_reply_to_user_id = ""
				  index = line.index(",text:")

				  # user
				  for index in range (line.index("user:")+6 , line.index(",id:")):
					  user = user + str(line[index])
				  # id
				  for index in range (line.index("id:")+3 , line.index(",created_at:")):
					  id = id + str(line[index])

				  # created_at
				  for index in range (line.index("created_at:")+11 , line.index(",text:")):
					  created_at = created_at + str(line[index])

				  # text
				  for index in range (line.index(",text:")+6, line.index(",retweete_count:")):
					  text = text + line[index].lower()

				  # make df
				  textArray = text.split()
				  for subText in textArray:
				   if(len(checkDF) == 0):
					  checkDF.append(subText)
					  df[subText] = 1
				   else:
					 if( (subText in checkDF) == False):
					  if(df.has_key(subText)):
						  df[subText] = df[subText] + 1
						  checkDF.append(subText)
					  else:
						  df[subText] = 1
						  checkDF.append(subText)

				  # retweet_count
				  for index in range (line.index("retweete_count:")+15, line.index(",in_reply_to_user_id:")):
					  retweet_count = retweet_count + line[index].lower()

				  #  in_reply_to_user_id
				  for index in range (line.index("in_reply_to_user_id:")+20, len(line)):
					  in_reply_to_user_id = in_reply_to_user_id + line[index].lower()

				  #lineString = re.findall(r"[\w']+", line)

				  # we will keep docInfo if the doc has a query term
				  found = False
				  for subString in query_tf:
					  if(subString in checkDF):
						  found = True
						  break

				  if(found):

				   docInfo["id"] = id
				   docInfo["user"] = user
				   docInfo["created_at"] = created_at
				   docInfo["text"] = text
				   docInfo["retweet_count"] = retweet_count
				   docInfo["in_reply_to_user_id"] = in_reply_to_user_id
				   docVector.append(docInfo)

				f.close()

			# lineString = re.findall(r"[\w']+", lineString)

		for subString in df:
			numerator  = cnt / df[subString]
			idf[subString] = math.log(numerator) /math.log(2)


		query_tf_idf = {} # tf-idf of query
		sqrt = 0.0
		normalize_query = 0.0
		for subString in query_tf:
			if(subString in idf):
			 query_tf_idf[subString] = (1 + math.log(query_tf[subString]) / math.log(2)) * idf[subString]
			 normalize_query = normalize_query + query_tf_idf[subString] * query_tf_idf[subString]

		sqrt = normalize_query**(.5)

		'''
		  normalize the query_tf_idf !!
		'''

		for subString in query_tf_idf:
			query_tf_idf[subString] = query_tf_idf[subString] / sqrt




		'''
		  Calculate TF-IDF of document
		'''
		for subList in docVector:

			tf= {} # term frequency
			tf_idf = {} # tf-idf
			normalize_document = 0.0
			sqrt = 0.0
			text = subList["text"]
			subString = text.split()
			# tf-raw
			for string in subString:
				if(tf.has_key(string)):
					tf[string] = tf[string] + 1
				else:
					tf[string] = 1

			#tf-weight
			for subString in tf:
				if(subString in idf):
				 tf[subString] = 1 + math.log(tf[subString]) / math.log(2)
				 tf_idf[subString] = tf[subString] * idf[subString]
				 normalize_document = normalize_document + tf_idf[subString] * tf_idf[subString]

			sqrt = normalize_query**(.5)

			for subString in tf_idf:
				tf_idf[subString] = tf_idf[subString] / sqrt

			product = 0.0
			for subString1 in query_tf_idf:
				for subString2 in tf_idf:
					if(subString1 == subString2):
						product = product + query_tf_idf[subString1] * tf_idf[subString2]
			subList["product"] = product

		docVector.sort(key= lambda s: s["product"], reverse=True) # sort by length

		return docVector

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

		loop = 0
		max = 100
		friends_info = {}
		finished = 0
		while finished == 0 :
			user_lookup_url =  "https://api.twitter.com/1/users/lookup.json?user_id="
			if loop+100 >= len(friends_ids):
				max = len(friends_ids) - loop
				finished = 1

			for i in range(max):
				user_lookup_url += str(friends_ids[i+loop]) + ','
			loop += 100
			user_lookup_url = user_lookup_url[:-1]
			friends_info = requests.get(user_lookup_url).json()
			for friend in friends_info:
				info_dict = {}
				info_dict["id_str"] = friend["id_str"]
				info_dict["followers_count"] = friend["followers_count"]
				info_dict["status_count"] = friend["statuses_count"]
				info_dict["friends_count"] = friend["friends_count"]
				info_dict["screen_name"] = '@' + friend["screen_name"]
				if int(friend["statuses_count"]) >= int(friend["followers_count"]):
					info_dict["rank_variable"] = friend["statuses_count"]
				else:
					info_dict["rank_variable"] = friend["followers_count"]
				friends_dict.append(info_dict)

		return friends_dict

	def rankfriends(self):
		#based on followers count. Need to update
		friends_dict = self.accessFriendsInfo()
		friends_dict = sorted(friends_dict, key=lambda d:(d['rank_variable']),reverse = True)
		user_rank = {}
		i = 1
		for friend in friends_dict:
			user_rank[friend["screen_name"]] = i
			i += 1

		return user_rank



	def combinerank(self):
		user_rank = self.rankfriends()
		tweet_rank = self.getTweets()
		for subTweet in tweet_rank:
			cnt = 1
			for user in user_rank:
			    user = user.replace("@", "")

		            if(subTweet["user"] == user):
				    divider = (len(user_rank) - cnt + 1) / len(user_rank)
				    subTweet["product"] = subTweet["product"] * divider

			    cnt = cnt + 1
		tweet_rank.sort(key= lambda s: s["product"], reverse=True) # sort by length

		return tweet_rank


	def search(self):
		return self.combinerank()

def main():
	#Call the funtion to access username and search query here
	searchobj = Search("TheRealCaverlee","south")
	searchobj.search()

if __name__ == '__main__':
	main()
