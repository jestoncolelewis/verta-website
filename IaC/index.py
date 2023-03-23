import boto3

ses = boto3.client('ses')

def send(event, context):
    ses.send_email(
        Destination = {
            'ToAddresses': ['email']
        },
        Message = {
            'Subject': {
                'Charset': 'UTF-8',
                'Data': ''
            },
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': ''
                    }}
        },
        Source = 'website@jestonlewiscreative.com'
    )