import os
from functions import *

name = 'vertasafety.com'

key = 'index.py'

path = os.getcwd()
path = path + '/' + key

build_s3(name, path, key)

language = 'python3.9'

role = ''

code = [name, key]

description = ''

target = build_lambda(name, language, role, code, description)

build_api(name, target)

build_ses()