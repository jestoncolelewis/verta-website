import boto3
import botocore.exceptions

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
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))
    response = s3.list_objects(Bucket = name)
    objects = list(response.items())
    file = objects[3][1][0].get('Key')
    return file

def build_lambda(name, lang, role, code, desc):
    try:
        response = lamb.create_function(
            Runtime = lang,
            Role = role,
            Code = {
                'S3Bucket': code[0],
                'S3Key': code[1]
            },
            Description = desc,
            FunctionName = name,
            Handler = 'index.send'
        )
        return response.get('FunctionArn')
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))
        response = lamb.get_function(FunctionName = name)
        return response['Configuration']['FunctionArn']

def build_api(name, target):
    try:
        api.creat_api(
            Name = name,
            ProtocolType = 'HTTP',
            CorsConfiguration = {
                'AllowOrigins': ['*']
            },
            Target = target
        )
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))

def build_ses():
    try:
        ses.create_email(EmailIdentity = 'email')
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))