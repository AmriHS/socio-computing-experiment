from datetime import datetime 
from constants import TWEET_KEYS, USER_KEYS

def format_tweet(tweet): 
    """ 
    format tweet 
  
    Exclude information, compress dictionaries, and format date
  
    Parameters: 
    tweet (dict): tweet dictionary 
  
    Returns: 
    dict: formatted tweet 
  
    """
    original_tweet = tweet
    if 'retweeted_status' in tweet:
        original_tweet = tweet['retweeted_status']

    formatted_tweet = include_keys(original_tweet, TWEET_KEYS)
    entities = include_keys(original_tweet['entities'], TWEET_KEYS)
    metadata = include_keys(original_tweet['metadata'], TWEET_KEYS)

    formatted_tweet['user_mentions'] = extract_key_to_array(entities['user_mentions'], 'id_str')
    formatted_tweet['hashtags'] = extract_key_to_array(entities['hashtags'], 'text')
    formatted_tweet['created_at'] = format_date(formatted_tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y', '%m-%d-%Y %H:%M:%S')
    formatted_tweet['iso_language_code'] = metadata['iso_language_code']
    formatted_tweet['tweet_id'] = formatted_tweet.pop('id_str')
    return formatted_tweet
    
def format_user(tweet): 
    """ 
    format user 
  
    Exclude information, compress dictionaries, and format date
  
    Parameters: 
    tweet (dict): tweet dictionary 
  
    Returns: 
    dict: formatted user 
  
    """
    original_tweet = tweet
    if 'retweeted_status' in tweet:
        original_tweet = tweet['retweeted_status']   
         
    formatted_user = include_keys(original_tweet['user'], USER_KEYS)
    formatted_user['created_at'] = format_date(formatted_user['created_at'], '%a %b %d %H:%M:%S +0000 %Y', '%m-%d-%Y %H:%M:%S')
    formatted_user['user_id'] = formatted_user.pop('id_str')
    return formatted_user
     
def include_keys(obj, keys):
    """ 
    include Keys 
  
    get dictionary with included keys only
  
    Parameters: 
    keys (array): array of keys
    tweet (dict): tweet dictionary 
  
    Returns: 
    dict: dictionay with only specified keys
  
    """
    return {x: obj[x] for x in obj if x in keys}

def convert_object_to_array(array, key):
    """ 
    convert object to array of values by key
  
    get dictionary with included keys only
  
    Parameters: 
    array (array): array of objects
    key (string): key 
  
    Returns: 
    array: array of values
  
    """
    return [x[key] for x in array]

def format_date(date_str, from_format, to_format):
    """ 
    format date to a given format
  
    description
  
    Parameters: 
    date_str (string): date in string
    from_format (string): fromat to convert from 
    to_format (string): format to convert to 

    Returns: 
    string: formatted date
  
    """
    x = datetime.strptime(date_str, from_format)
    return x.strftime(to_format)