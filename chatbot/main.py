'''

啟動flask server

flask starter example

'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return  'Hello, World!'

'''
準備一個路徑(URN)
此路徑為lbh
用戶訪問此路徑的時候，回傳hahaha
'''

@app.route('/lbh')
def hello_lbh():
    return 'ha'*4

'''
準備一個路徑(URN)
此路徑為simulate-ai
用戶訪問此路徑的時候，我們會執行1+1，並把運算結果回傳給他
'''
@app.route('/simulate-ai')
def simulate_ai():
    # ai
    calResult = 1+1
    return str(calResult)

'''
準備一個路徑
此路徑為return-html
用戶訪問此路徑的時候，我們會回傳一個網頁給他
flask return html example
'''
@app.route('/return-html')
def return_html():
    # ai
    calResult = 1+1
    return str(calResult)

'''
準備一個路徑
此路徑為fake-html
用戶訪問此路徑的時候，我們用requests模組去訪問某網頁
request get some website example
把該網頁的文字回傳給用戶
'''
import requests
@app.route('/fake-html')
def fake_html():
    crawlerResult = requests.get('https://tw.yahoo.com')
    return crawlerResult.text


app.run()
#app.run(host='0.0.0.0')