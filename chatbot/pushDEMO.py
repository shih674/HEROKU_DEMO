from linebot import (
    LineBotApi
)

from linebot.models import (
    MessageEvent, TextMessage, ImageSendMessage, TextSendMessage, FollowEvent, QuickReplyButton, QuickReply, MessageAction
)

# 創造Line_bot_api
line_bot_api = LineBotApi('a0PPA+VvNtKUi+yJcpQ7VK1w4MKJ67Wp5Tge0ydzpqPArCYuIQYmncLjp8ltBYaOwG38C8GEcAik63WRw3yjgUwVSOzOec8FQC1yXKH/F2gvO9+Be0mu+KQwJ5jBF57O2paNMFl89sOOLZPXykcmdAdB04t89/1O/w1cDnyilFU=')

# 推撥給指定用戶
#userID = ''
#line_bot_api.push_message(to=userID,
#                          messages=[TextSendMessage('請秉宏老師喝飲料')])

# 全體廣播
#line_bot_api.broadcast((TextSendMessage('你們花我五十則消息，都得請喝飲料')))

# 指定多位用戶
# Quick
#id1 = ''
#id2 = ''
#message_qnb = QuickReplyButton(action = MessageAction(label='五十嵐',text= '請五十嵐'))
#message_qnb2= QuickReplyButton(action = MessageAction(label='星巴克',text= '請星巴克'))
#quick_reply_list = QuickReply(items=[message_qnb, message_qnb2])
#text_demo_message = TextSendMessage('你打算請炳宏喝什麼',quick_reply=quick_reply_list)
#line_bot_api.multicast(to=[id1,id2], messages=[text_demo_message])