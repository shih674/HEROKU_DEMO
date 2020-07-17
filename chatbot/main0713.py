from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, ImageSendMessage, TextSendMessage, FollowEvent,
    TemplateSendMessage, ButtonsTemplate, MessageAction, URIAction, PostbackAction,
    PostbackEvent, FlexSendMessage, QuickReplyButton, QuickReply, LocationAction,
    ImageMessage, VideoMessage
)


import random
import json

app = Flask(__name__)

line_bot_api = LineBotApi('a0PPA+VvNtKUi+yJcpQ7VK1w4MKJ67Wp5Tge0ydzpqPArCYuIQYmncLjp8ltBYaOwG38C8GEcAik63WRw3yjgUwVSOzOec8FQC1yXKH/F2gvO9+Be0mu+KQwJ5jBF57O2paNMFl89sOOLZPXykcmdAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('59ecf1f0848ac89b37a0db7c8236ade7')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
'''
告知handler
若收到關注事件，
    則取人家個資，並打印出來
                打印出來太LOW，準備存成檔案
    送文字消息給用戶
        生成文字消息
        交給line_bot_api做訊息回覆
    送圖片消息給用戶
        引入圖片消息套件
        生成圖片消息
            要準備兩張圖片的https link
        交給line_bot_api做訊息回覆
            
'''
@handler.add(FollowEvent)
def handle_follow(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)

    # 開啟一個檔案，將用戶個資轉成json保存
    with open('./user.txt','a') as myfile:
        myfile.write((json.dumps(vars(user_profile))))
        #新資料換行
        myfile.write('/r/n')

    # 建立文字消息
    follow_text_send_message = TextSendMessage('感謝提供個資')

    # 建立圖片訊息
    follow_img_send_message = ImageSendMessage(
        original_content_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2019/12/11/20191211-105221_U16223_M575797_9872.jpg?itok=OteP5iqj',
        preview_image_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2019/12/11/20191211-105221_U16223_M575797_9872.jpg?itok=OteP5iqj'
    )

    # 建立範本消息(最多同時4個)
    # alt_text: 消息在line聊天列表的替代文字
    # template: Carousel, Button, Confirm, ImageCarousel
    # title: 標題
    # text: 描述
    # actions: 那些案件
    #   MessageAction:
    #       Label: 按鍵的字樣
    #       text: 當用戶點擊時，以用戶身分發出的文字，串接場景
    #   UriAction:
    #       lavel: 按鍵的字樣
    #       url: 網址
    #   PostBackAction:
    #
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/3/3c/Assassination_Classroom_Volume_1.jpg',
            title='Menu',
            text='Please select',
            actions=[
                MessageAction(
                    label='message',
                    text='message text'
                ),
                PostbackAction(
                    label='以後常用的回傳動作',
                    text='以用戶身分發話',
                    data='special'
                ),
                URIAction(
                    label='夯哥的電話',
                    uri='tel://0929122033'
                ),
                URIAction(
                    label='女友評分器',
                    uri='https://line.me/R/nv/camera/'
                )
            ]
        )
    )
    '''
    用json生成模板消息
        讀取本地的json檔案- json.load取得json物件
        將json物件放入TemplateSendMessage的new_from_json_dict方法，並存在變數內即可
    '''
    with open('sendmessage.json', 'r', encoding='utf8') as jsonfile:
        json_object = json.load(jsonfile)
    template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)

    with open('flex_message.json', 'r',encoding='utf8') as jsonfile:
        json_object = json.load(jsonfile)
    flex_message_from_json = FlexSendMessage.new_from_json_dict(json_object)

    # 麻煩line_bot_api把文字消息交給line，一次最多五則
    line_bot_api.reply_message(event.reply_token, [follow_img_send_message, follow_text_send_message, template_message_from_json, flex_message_from_json])


# 收到文字消息的時候
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '暗殺教室':
        img_send_message = ImageSendMessage(
        original_content_url='https://www.animen.com.tw/FilesUpload/CK-Images/150925_71_2.jpg',
        preview_image_url='https://upload.wikimedia.org/wikipedia/zh/3/3c/Assassination_Classroom_Volume_1.jpg'
    )
        line_bot_api.reply_message(
            event.reply_token,
            img_send_message)
    elif event.message.text == '帥哥':
        img_list = [['https://i0.wp.com/www.littleoslo.com/lyc/home/wp-content/uploads/2016/04/%E9%9F%8B%E7%A6%AE%E5%AE%89.png?fit=1024%2C1024', 'https://img.mymusic.net.tw/mms/singer/732/18732s.jpg']
                    ]
        index = random.randint(0,len(img_list))
        img_send_message = ImageSendMessage(
        original_content_url=img_list[index][0],
        preview_image_url=img_list[index][1]
    )
        line_bot_api.reply_message(
            event.reply_token,
            img_send_message)

    elif event.message.text == '隱藏功能':
        # 創造一個QuickReplyButton
        text_quickreply = QuickReplyButton(action=MessageAction(label='我是標籤', text='我幫你打字'))
        #
        location_quickreply = QuickReplyButton(action=LocationAction(label='助教在哪裡'))

        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quickreply, location_quickreply])
        # 生成一個文字消息
        reply_text_message = TextSendMessage(event.message.text, quick_reply=quick_reply_array)

        line_bot_api.reply_message(event.reply_token, reply_text_message)

    elif event.message.text == '我要點餐':
        # 創造一個QuickReplyButton
        text_quickreply0 = QuickReplyButton(action=MessageAction(label='1. 大麥克', text='配餐選擇'))
        text_quickreply1 = QuickReplyButton(action=MessageAction(label='2. 雙層牛肉吉士堡', text='配餐選擇'))
        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quickreply0, text_quickreply1])
        # 生成一個文字消息
        reply_text_message = TextSendMessage('請選擇主餐', quick_reply=quick_reply_array)

        line_bot_api.reply_message(event.reply_token, reply_text_message)

    elif event.message.text == '配餐選擇':
        # 創造一個QuickReplyButton
        text_quickreply0 = QuickReplyButton(action=MessageAction(label='A 經典配餐', text='A'))
        text_quickreply1 = QuickReplyButton(action=MessageAction(label='B 清爽配餐', text='B'))
        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quickreply0, text_quickreply1])
        # 生成一個文字消息
        reply_text_message = TextSendMessage('請選擇配餐', quick_reply=quick_reply_array)

        line_bot_api.reply_message(event.reply_token, reply_text_message)

    else:
        # 把用戶的化轉成文字發送消息
        reply_text_message = TextSendMessage(event.message.text)

        # line_bot_api 傳送回去
        line_bot_api.reply_message(event.reply_token, reply_text_message)

'''
告知handler收到Postback event做xxx事情
    判斷postback的data
        若為specific
            則取他個資
        
'''
@handler.add(PostbackEvent)
def handle_postback_event(event):
    if event.postback.data == 'specific':
        user = line_bot_api.get_profile(event.source.user_id)
        print('hello',user)

'''
當用戶發出圖片消息的時候，
    我們用文字消息回應她，把他的訊息編號傳給他
'''
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    # 用戶的圖片消息id
    message_id = event.message.id

    # 變成文字消息
    image_id_text_send_message = TextSendMessage(text=message_id)

    # 將該文字消息傳回給用戶
    line_bot_api.reply_message(event.reply_token, image_id_text_send_message)

    # 請line_bot_api 拿照片回來，取回一個檔案
    # 得自己存在硬碟內
    content_file = line_bot_api.get_message_content(message_id=message_id)
    # 存圖片，必須以二進制方式存，wb
    # 但content_file不是二進制編碼，所以得用iter_content()轉成二進制，再寫入
    with open(message_id+'.jpg','wb') as temp_file:
        for chunk in content_file.iter_content():
            temp_file.write(chunk)

'''
當用戶傳影片給我們，
    我們把影片存回本地端，把他的訊息編號傳給他
'''
@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    # 請line_bot_api 向line取回影片
    video_content = line_bot_api.get_message_content(event.message.id)

    # 開啟一個以message_id為名的影片檔案，並要求line_bot_api把影片檔轉成二進制檔案寫入
    with open(event.message.id+'.mp4','wb') as temp_file:
        for chunk in video_content.iter_content():
            temp_file.write(chunk)

    # 回覆用戶，成功上傳
    line_bot_api.reply_message(event.reply_token, TextSendMessage('影片已上傳'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')