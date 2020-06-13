from datetime import datetime 
from constants import TWEET_KEYS, USER_KEYS

def format_tweet(tweet): 
    """Exclude information, compress dictionaries, and format date."""
    # TODO: exlcude urls
    user = tweet['user']['id_str']
    entities = include_keys(tweet['entities'], TWEET_KEYS)
    
    formatted_tweet = include_keys(tweet, TWEET_KEYS)

    formatted_tweet['user_mentions'] = convert_object_to_array(entities['user_mentions'], 'id_str')
    formatted_tweet['user'] = user
    formatted_tweet['hashtags'] = convert_object_to_array(entities['hashtags'], 'text')
    formatted_tweet['created_at'] = format_date(formatted_tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y', '%m-%d-%Y %H:%M:%S')
    formatted_tweet['tweet_id'] = formatted_tweet.pop('id_str')

    return formatted_tweet
    
def format_user(tweet): 
    """Exclude information, compress dictionaries, and format date."""
    formatted_user = include_keys(tweet['user'], USER_KEYS)
    formatted_user['created_at'] = format_date(formatted_user['created_at'], '%a %b %d %H:%M:%S +0000 %Y', '%m-%d-%Y %H:%M:%S')
    formatted_user['user_id'] = formatted_user.pop('id_str')
    return formatted_user
     
def include_keys(obj, keys):
    """Get dictionary with included keys only."""
    return {x: obj[x] for x in obj if x in keys}

def exlude_url(str):
    return ''

def convert_object_to_array(array, key):
    """Convert object to array of values by key."""
    return [x[key] for x in array]

def format_date(date_str, from_format, to_format):
    """Format date to a given format."""
    x = datetime.strptime(date_str, from_format)
    return x.strftime(to_format)

def chunks(arr, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(arr), n):
        yield arr[i:i + n]
