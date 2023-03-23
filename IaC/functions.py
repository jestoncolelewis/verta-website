import boto3
import botocore

s3 = boto3.client('s3')
s3r = boto3.resource('s3')
lamb = boto3.client('lambda')
api = boto3.client('api')
ses = boto3.client('sesv2')

def build_s3(name, path, key):
    try:
        s3.create_bucket(
            Bucket = name,
            CreateBucketConfiguration = {
                'LocationConstraint': 'us-west-2'
            }
        )
        s3r.meta.client.upload_file(path, name, key)
    except botocore.exceptions('ClientError') as err:
        print('{}'.format(err.response['Error']['Message']))
    response = s3.list_objects(Bucket = name)
    objects = list(response.items())
    file = objects[3][1][0].get('Key')
    return file

def build_lambda(name):
    try:
        return 'Success'
    except botocore.exceptions('ClientError') as err:
        return err

def build_api(name):
    try:
        return 'Success'
    except botocore.exceptions('ClientError') as err:
        return err

def build_ses():
    try:
        ses.create_email(EmailIdentity = 'email')
        return
    except botocore.exceptions('ClientError') as err:
        return err