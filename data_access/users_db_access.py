import logging
from boto3 import resource

dynamodb_resource = resource('dynamodb')
table = dynamodb_resource.Table('user_info')

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def insert_all(users): 
    """Persist batch of tweets' users into dynamodb."""    
    log.info("Insert users with a length of %d", len(users))
    log.info(users)
    
    with table.batch_writer() as batch:
        for item in users:
            batch.put_item(Item=item)