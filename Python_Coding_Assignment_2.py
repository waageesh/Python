from collections import Counter
test_cases = int(input())
#print(test_cases)
user_name = []

#class and def for calculating high tweeted
class user:
 def __init__(self,user_name):
    # split() returns list of all the words in the string 
    # split_it = data_set.split()  
    # Pass the split_it list to instance of Counter class. 
    self.user_name = user_name
    counter = Counter(self.user_name)  
    # most_common() produces k frequently encountered 
    # input values and their respective counts. 
    self.max_user = counter.most_common()
    print(self.max_user)
    #return(self.max_user)
    
for x in range(0,test_cases):
    tweets_cnt = int(input())
    #print(tweets_cnt)
    for y in range(0,tweets_cnt) :
        tweets = str(input())
        dum = list(tweets.split(" "))
        #print(dum[0])
        user_name.append(dum[0])
#print(user_name)
us = user(user_name)
#us.user_tweeted_max(user_name)
# most_common() produces k frequently encountered 
# input values and their respective counts. 
#user_name.append(dum[0)
