import boto3
import json

ses = boto3.client('ses')

def send(event, context):
    body = json.loads(event['body'])
    replyto = body['email']
    response = ses.send_email(
        FromEmailAddress = 'web@vertasafety.com',
        FromEmailAddressIdentityArn = '', # still need this
        Destination = {'ToAddresses': ['info@vertasafety.com']},
        ReplyToAddresses = [replyto],
        Content = {
            'Simple': {
                'Subject': {'Data': 'Beta sign up'},
                'Body': {'Text': {'Data': 'Someone has signed up for the beta, reply to this email to start a conversation or send a new message to:\n {}'.format(replyto)}}
            }
        }
    )
    return response