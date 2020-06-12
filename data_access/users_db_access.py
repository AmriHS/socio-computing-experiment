from boto3 import resource

dynamodb_resource = resource('dynamodb')
table = dynamodb_resource.Table('user_info')

def insert_all(users): 
    # TODO: accept only 25 items 
    with table.batch_writer() as batch:
        for item in users:
            batch.put_item(Item=item)