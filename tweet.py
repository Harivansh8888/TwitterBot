import tweepy
import time

auth = tweepy.OAuthHandler('','') #removed auth keys
auth.set_access_token('','') #removed auth keys
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'DevOps'
nrTweets = 20

api.update_status("Hello World !")
