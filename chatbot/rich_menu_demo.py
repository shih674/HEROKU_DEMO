from linebot import (
    LineBotApi
)
from  linebot.models import RichMenu


import  json

# 創造Line_bot_api
line_bot_api = LineBotApi('a0PPA+VvNtKUi+yJcpQ7VK1w4MKJ67Wp5Tge0ydzpqPArCYuIQYmncLjp8ltBYaOwG38C8GEcAik63WRw3yjgUwVSOzOec8FQC1yXKH/F2gvO9+Be0mu+KQwJ5jBF57O2paNMFl89sOOLZPXykcmdAdB04t89/1O/w1cDnyilFU=')

# 將設定檔傳給line

# 讀取json檔

# 轉成json格式

# line_bot_api傳給line

# 把rich menu id打印出來
#with open('home.json','r', encoding='utf8') as json_file:
#    rich_menu_json_object = json.load(json_file)
# 將json格式做成RichMenu的變數
#richMenu = RichMenu.new_from_json_dict(rich_menu_json_object)
#rich_menu_id = line_bot_api.create_rich_menu((richMenu))
#print(rich_menu_id)
#-------------------------------------------------------------------
# 把照片傳給指定的圖文選單id
rich_menu_id = 'richmenu-d064ffdd57e2055c21e9796e3c80bce9'
with open('home.jpg','rb') as image_file:
     response = line_bot_api.set_rich_menu_image(
            rich_menu_id=rich_menu_id,
            content_type='image/jpeg',
            content=image_file
        )
print(response)
#-------------------------------------------------------------------
# 綁定用戶
#userid = ''
#rich_menu_id = 'richmenu-8d53c6de5edc7c84edd3ed067b646010'
#line_bot_api.link_rich_menu_to_user(
#    user_id=userid,
#    rich_menu_id=rich_menu_id
#)

# 解除綁定
#userid = ''
#line_bot_api.unlink_rich_menu_from_user(
#    user_id=userid
#)

# 刪除圖文選單
#rich_menu_id = 'richmenu-8d53c6de5edc7c84edd3ed067b646010'
#line_bot_api.delete_rich_menu(rich_menu_id=rich_menu_id)