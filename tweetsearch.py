import tweepy
from textblob import TextBlob
conskey ='91NpZMGETsHGb5a8mmZTfMfr5'
Consecret = 'gt9aRi4gDagFT9ADYKygyBcg8YC2aJeKsNj89C2laEWlI7ulzk'
Access_Token='906588942488633344-9c5NRlDm3mJN0uO9iYMdzZEvsGnrGjE'
AccessTokenSecret='wKqRxTEFkO8jfY2etwi5RJ1ncXzvYOpQZsCn46XZfWR1W'
auth= tweepy.OAuthHandler(conskey,Consecret)
auth.set_access_token(Access_Token,AccessTokenSecret)
vapi = tweepy.API(auth)
var_name=  input("search tweet from:  ")
public_tweet= vapi.search(var_name)
for twt in public_tweet:
    tweet=twt.text
    print(tweet)
analysis= TextBlob(tweet)
print(analysis.sentiment)
