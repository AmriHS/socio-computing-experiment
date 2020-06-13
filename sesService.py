import boto3
from constants import SOURCE_EMAIL, DEST_EMAIL 

ses = boto3.client('ses')

def send_email(emaiL_subject, email_body):
    """Send email to recipient email address."""
    dest = {
            'ToAddresses': [
                DEST_EMAIL,
            ]
        }
    msg = {
            'Subject': {
                'Data': emaiL_subject,
            },
            'Body': {
                'Text': {
                    'Data': email_body,
                }
            }
        }
        
    ses.send_email(
        Source = SOURCE_EMAIL,
        Destination=dest,
        Message=msg
    )
