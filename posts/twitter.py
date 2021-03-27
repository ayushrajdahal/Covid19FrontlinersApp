import tweepy
from tweepy.auth import OAuthHandler
from .models import Tweet


def user_tweets():
    auth = OAuthHandler('XnBO8h5wSJMlPM79l8dmOOCl5', 'yc6RnHCSgVarbwDO0Mv1ks5yLe5Icu6UB2iexkc8kv27v3gfeh')
    auth.set_access_token('1019431627049525248-cvKyIZ1wUvxPHHkZm9Jsu38aliP1xO', 'UNHAO5eXaTc1tkRsbNxPcAg54mvyhomtrCj3WjzI8vzPj')
    api = tweepy.API(auth)
    user_tweets = api.user_timeline(count=50)
    return user_tweets


def save_to_db():
    original_tweets = user_tweets()
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(tweet_id=original_tweet.id):
                new_tweet = Tweet(tweet_id=original_tweet.id, tweet_text=original_tweet.text,
                                  published_date=original_tweet.created_at, is_active=True)
                new_tweet.save()


def set_inactive(pk):
    Tweet.objects.filter(tweet_id=pk).update(is_active=False)


def set_active(pk):
    Tweet.objects.filter(tweet_id=pk).update(is_active=True)

