import json
import tweepy
from ssm_params_service import get_secret
from data_formatter import format_tweet, format_user

def dataCollector(event, context):
    tweeter_key = get_secret('tweeter_key')
    keys = tweeter_key.split(',')
    api_key = keys[0]
    api_secret_key = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search(q='oil', count=1)

    formatted_tweets = [format_tweet(tweet) for tweet in tweets['statuses']]
    formatted_users = [format_user(tweet) for tweet in tweets['statuses']]
    return {
        "statusCode": 200,
        "body": "",
    }

dataCollector('a', 'b')