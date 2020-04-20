import tweepy
import time

auth = tweepy.OAuthHandler()

auth.set_access_token()

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user)
print("Hari")