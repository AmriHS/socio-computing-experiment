import json
import tweepy
import data_formatter
import logging
from ssm_params_service import get_secret
from data_access import tweets_db_access, users_db_access
from sesService import send_email
from constants import BATCH_SIZE 

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def get_keys():
    # TODO: PythonDoc
    log.info('Getting tweeter account keys...')
    tweeter_key = get_secret('tweeter_key')
    splitted_keys = tweeter_key.split(',')

    return {
        'api_key': splitted_keys[0],
        'api_secret_key': splitted_keys[1], 
        'access_token': splitted_keys[2],
        'access_token_secret': splitted_keys[3]
    }

def dataCollector(event, context):
    """ 
    Lambda handler to collect tweets and persist then in database

    """
    # TODO: Error handling
    # TODO: Handler response
    # TODO: Email notification
    # TODO: Logging

    log.info('New data collector invocation at')
    keys = get_keys()
    auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret_key'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    query_str = '(lang:en OR lang:ar) -filter:retweets -filter:replies'
    log.info('Search tweets with query filters %s' % query_str)

    tweets = [tweet._json for tweet in tweepy.Cursor(api.search, q=query_str, tweet_mode='extended').items(100)]
    log.info('Tweets are retrieved with a length of %d' % len(tweets))

    formatted_tweets = [data_formatter.format_tweet(tweet) for tweet in tweets]
    formatted_users = [data_formatter.format_user(tweet) for tweet in tweets]

    tweet_batches = data_formatter.chunks(formatted_tweets, BATCH_SIZE)
    user_batches = data_formatter.chunks(formatted_users, BATCH_SIZE)

    for t_batch in tweet_batches:
        tweets_db_access.insert_all(t_batch)

    for u_batch in user_batches:
        users_db_access.insert_all(u_batch)

    send_email('Successful invocation', 'Tweets are retrieved with a length of %d' % len(tweets))

    return {
        "statusCode": 200,
        "body": "",
    }

if __name__ == "__main__":
    dataCollector(1,2)