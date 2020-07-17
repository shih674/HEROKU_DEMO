import boto3
import requests
#from bs4 import Beautifulsoup

'''
爬網頁下來，

並存到S3桶子內
'''

res = requests.get('https://www.toutiao.com/')
with open('sample.html','w', encoding='utf-8') as f:
    f.write(res.text)
    print(f)