import emoji
import re
import functools
from datetime import datetime 
from constants import TWEET_KEYS, USER_KEYS

def format_tweet(tweet): 
    """Exclude information, compress dictionaries, and format date."""
    user = tweet['user']['id_str']
    entities = include_keys(tweet['entities'], TWEET_KEYS)
    
    formatted_tweet = include_keys(tweet, TWEET_KEYS)
    formatted_tweet['user_mentions'] = convert_object_to_array(entities['user_mentions'], 'id_str')
    formatted_tweet['user'] = user
    formatted_tweet['hashtags'] = convert_object_to_array(entities['hashtags'], 'text')
    formatted_tweet['created_at'] = format_date(formatted_tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y', '%m-%d-%Y %H:%M:%S')
    formatted_tweet['tweet_id'] = formatted_tweet.pop('id_str')

    formatted_tweet['full_text'] = clean_tweet(formatted_tweet['full_text'])
    return formatted_tweet
    
def format_user(tweet): 
    """Exclude information, compress dictionaries, and format date."""
    formatted_user = include_keys(tweet['user'], USER_KEYS)
    formatted_user['created_at'] = format_date(formatted_user['created_at'], '%a %b %d %H:%M:%S +0000 %Y', '%m-%d-%Y %H:%M:%S')
    formatted_user['user_id'] = formatted_user.pop('id_str')
    return formatted_user
     

def clean_tweet(tweet):
    """Clean tweets from emoji, url, hatags, and user mentions."""
    composed_functions = compose(exclude_emoji, exclude_url, exclude_hashtags, exclude_mentions)
    return composed_functions(tweet)

def compose(*functions):
    """Compose multiple functions."""
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def include_keys(obj, keys):
    """Get dictionary with included keys only."""
    return {x: obj[x] for x in obj if x in keys}

def exclude_url(str):
    """Remove url from string."""
    return re.sub(r"http\S+", '', str)

def exclude_emoji(str):
    """Remove emoji from strint."""
    return emoji.get_emoji_regexp().sub(u'', str)

def exclude_mentions(str):
    """Remove user mentions from string."""
    return re.sub(r'@[^\s]+', 'USER_MENTION', str)

def exclude_hashtags(str):
    """Remove hashtags from string."""
    return re.sub(r'#[^\s]+', '', str)

def convert_object_to_array(array, key):
    """Convert object to array of values by key."""
    return [x[key] for x in array]

def format_date(date_str, from_format, to_format):
    """Format date to a given format."""
    x = datetime.strptime(date_str, from_format)
    return x.strftime(to_format)

def get_tody_date(format):
    """Get today date for a given format."""
    return datetime.utcnow().strftime(format)

def chunks(arr, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(arr), n):
        yield arr[i:i + n]
