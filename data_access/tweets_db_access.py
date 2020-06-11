from boto3 import resource

dynamodb_resource = resource('dynamodb')
table = dynamodb_resource.Table('tweet_info')

def insert_all(tweets): 
    try:
        with table.batch_writer() as batch:
            for item in tweets:
                batch.put_item(Item=item)
    except TypeError as e:
        print(e)
