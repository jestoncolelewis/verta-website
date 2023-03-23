import boto3
import botocore

s3 = boto3.client('s3')
s3r = boto3.resource('s3')
lamb = boto3.client('lambda')
api = boto3.client('api')
ses = boto3.client('ses')

def build_s3():
    return

def build_lambda():
    return

def build_api():
    return

def build_ses():
    return