from collections import Counter
import pandas as pd
#first input will be taken here for defining number of test cases
test_cases = int(input())
user_name = []

class user:
	def __init__(self,user_name):
		self.user_name = user_name
		counter = Counter(self.user_name)  
		self.max_user = counter.most_common()
		#from here we have used dataframe to clean and display data 
		df = pd.DataFrame(self.max_user)
		df = df[:-1]
		df = df.sort_values(by=[1])
		df.fillna(0)
		print("\n")
		#printing dataframe without index and header
		print(df.to_string(index=False, header=False))
    
for x in range(0,test_cases):
	#second input will be taken here for taking number tweets
    tweets_cnt = int(input())
    for y in range(0,tweets_cnt) :
		#Next starts here for third input will be like name of tweets space id
        tweets = str(input())
		#inputs broken into name and id using seperator " " and assigned into list
        dum = list(tweets.split(" "))
		#storing the user_name
        user_name.append(dum[0])

us = user(user_name)
