import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

if __name__ == "__main__":
    

    user = api.get_user("s2t2")
    print(user.id)
    print(user.screen_name)
    print(user.friends_count)
    print(user.followers_count)

    statuses = api.user_timeline("s2t2", tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    for status in statuses:
        print("---")
        print(status.full_text)