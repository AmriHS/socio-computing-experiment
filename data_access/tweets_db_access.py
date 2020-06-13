import logging
from boto3 import resource

dynamodb_resource = resource('dynamodb')
table = dynamodb_resource.Table('tweet_info')

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def insert_all(tweets): 
    """Persist batch of tweets into dynamodb."""
    log.info("Insert tweets with a length of %d", len(tweets))
    log.info(tweets)
    
    try:
        with table.batch_writer() as batch:
            for item in tweets:
                batch.put_item(Item=item)
    except TypeError as e:
        log.error(e)
