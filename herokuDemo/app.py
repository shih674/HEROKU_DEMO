from flask import Flask
import json
import os

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImagemapSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('a0PPA+VvNtKUi+yJcpQ7VK1w4MKJ67Wp5Tge0ydzpqPArCYuIQYmncLjp8ltBYaOwG38C8GEcAik63WRw3yjgUwVSOzOec8FQC1yXKH/F2gvO9+Be0mu+KQwJ5jBF57O2paNMFl89sOOLZPXykcmdAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('59ecf1f0848ac89b37a0db7c8236ade7')

#--
import boto3
# 創造S3的客戶端
s3Client = boto3.client('s3', aws_access_key_id='AKIAR4NDUH53GWDLQFNM', aws_secret_access_key='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')

# 用客戶端上傳圖片到S3 bucket內，iii-tutorial-v2
#s3Client.upload_file(file_name, bucket, object_name)
#s3Client.upload_file('Procfile', 'iii-tutorial-v2', 'student28/Procfile')
#--

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 用json產生Imagemap物件
    #with open('test1.json', 'r',encoding='utf8') as jsonfile:
    #    json_object = json.load(jsonfile)
    json_object = {
                  "type": "imagemap",
                  "baseUrl": "https://i.imgur.com/lRAVpQ9.jpg",
                  "altText": "This is an imagemap",
                  "baseSize": {"width": 1040, "height": 868 },
                  "actions": [{
                      "type": "message",
                      "area": {
                        "x": 66,
                        "y": 40,
                        "width": 932,
                        "height": 523
                      },
                      "text": "機車"
                    }
                  ]
                }
    Imagemap_from_json = ImagemapSendMessage.new_from_json_dict(json_object)
    # 請line bot api回復文字訊息
    line_bot_api.reply_message(event.reply_token,
                               [TextSendMessage(text=event.message.text), Imagemap_from_json])

'''
告知handler，收到圖片消息
    要從line上把圖片抓回來
    並且檔名要以消息id為命名
    把檔案上傳到s3，位置 student28/消息id.jpg
'''
from  linebot.models import (
    ImageMessage
)
#@handler.add(MessageEvent, message=ImageMessage)
#def handle_image_message(event):
    # 請line_bot_api抓圖片回來，哈哈 忘記也沒關係
#    image_temp_variable = line_bot_api.get_message_content(event.message.id)

    # 把圖片存成檔案
#    with open(event.message.id+'.jpg', 'wb') as f:
#        for chunk in image_temp_variable.iter_content():
#            f.write(chunk)
    # 把圖片存到S3上面
#    s3Client.upload_file(event.message.id+'.jpg', 'iii-tutorial-v2', 'student28/'+event.message.id+'.jpg')

    # line-bot-api回覆消息
#    line_bot_api.reply_message(event.reply_token, TextSendMessage(event.message.id))

#if __name__ == "__main__":
#    app.run()


#app.run(host='0.0.0.0', port='62525')

# heroku專用，偵測heroku給我們的port
app.run(host='0.0.0.0', port=os.environ['PORT'])
