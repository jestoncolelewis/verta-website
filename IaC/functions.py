import boto3
import botocore

s3 = boto3.client('s3')
s3r = boto3.resource('s3')
lamb = boto3.client('lambda')
api = boto3.client('api')
ses = boto3.client('sesv2')

def build_s3():
    try:
        return 'Success'
    except botocore.exceptions('ClientError') as err:
        return err

def build_lambda():
    try:
        return 'Success'
    except botocore.exceptions('ClientError') as err:
        return err

def build_api():
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