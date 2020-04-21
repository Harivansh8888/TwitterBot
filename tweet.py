import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('','')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'DevOps'
nrTweets = 20

api.update_status("Hello World !")
