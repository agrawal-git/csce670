'''
 Created by Hong-hoe Kim

'''

import os
import re
import math
print "What do you want to query?"

dirPath = '/Users/hong-hoegim/Dropbox/class/CPSC670/project/tweets'
userPath = '/Users/hong-hoegim/Dropbox/class/CPSC670/project/UserInfo.txt'

pattern = re.compile(",(?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))")
pattern = re.compile(ur'[\u064B-\u0652\u06D4\u0670\u0674\u06D5-\u06ED\u2019s]+', 
                      re.UNICODE)

#input = raw_input()
maxPrint = 20 # how many returns
input = "hello"
input = input.split()

df = {} # document frequency
idf = {}  # idf
tf = {} # term frequency
query_tf = {}  # term frequency of query
docVector = []

for subQuery in input:
    if(query_tf.has_key(subQuery) == False):
        query_tf[subQuery] = 1
    else:
        query_tf[subQuery] = query_tf[subQuery] + 1

for subString in query_tf:
    query_tf[subString] = 1 + math.log(query_tf[subString]) / math.log(2)
         
cnt = 0

'''
 Retrieve user info
'''
user_list = []
userFile = open(userPath, 'r')
    
for line in userFile:
    friend_info = {}
    index = 0
    name = ""
    id = ""
    followers_cnt = ""
    friends_cnt = ""
    status_cnt = ""
    #name
    for index in range(line.index("name")+6, line.index(",id:")):
        name = name + line[index]
        
    #id
    for index in range(line.index("id")+4, line.index(",followers_cnt:")):
        id = id + line[index]
        
    #followers_cnt
    for index in range(line.index("followers_cnt")+14, line.index(",friends_cnt:")):
        followers_cnt = followers_cnt + line[index]  
        
    #friends_cnt    
    for index in range(line.index("friends_cnt")+12, line.index(",status_cnt:")):
        friends_cnt = friends_cnt + line[index]   
        
    #status_cnt
    for index in range(line.index("status_cnt")+11, len(line)-1):
        status_cnt = status_cnt + line[index]   
    user_list.append(friend_info)
    
    friend_info["name"] = name
    friend_info["id"] = id
    friend_info["followers_cnt"] = followers_cnt
    friend_info["friends_cnt"] = friends_cnt
    friend_info["status_cnt"] = status_cnt

normalize_followers_cnt = 0.0
normalize_friends_cnt = 0.0
normalize_status_cnt = 0.0

for subList in user_list:
    subList["followers_cnt"] = 1 + math.log(float(subList["followers_cnt"])) / math.log(2)
    subList["friends_cnt"] = 1 + math.log(float(subList["friends_cnt"])) / math.log(2)
    subList["status_cnt"] = 1 + math.log(float(subList["status_cnt"])) / math.log(2)
    normalize_followers_cnt = normalize_followers_cnt + subList["followers_cnt"] * subList["followers_cnt"]
    normalize_friends_cnt = normalize_friends_cnt + subList["friends_cnt"] * subList["friends_cnt"]
    normalize_status_cnt = normalize_status_cnt + subList["status_cnt"] * subList["status_cnt"]
   
   
'''
  normalize user's followers_cnt, friends_cnt, status_cnt to get user's ranking
'''   
sqrt = 0.0
for subList in user_list:
    subList["followers_cnt"] = subList["followers_cnt"] / (normalize_followers_cnt **(.5))
    subList["friends_cnt"] = subList["friends_cnt"] / (normalize_friends_cnt **(.5))
    subList["status_cnt"] = subList["status_cnt"] / (normalize_status_cnt **(.5))
    
    
    
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
    #for userList in user_list:
       # if(subList["user"] == userList["name"]):
       #     product = userList["followers_cnt"] * userList["friends_cnt"] * userList["status_cnt"]
    
    

docVector.sort(key= lambda s: s["product"], reverse=True) # sort by length

if(len(docVector) == 0):
    print "No result"
else:
 cnt = 0
 for subList in docVector:
  
   if(cnt == maxPrint):
       break
   else:
    print subList
    cnt = cnt + 1
        
    
    
         


    
    