"""
lambda_function.py
"""
# postリクエストをline bot APIに送るためにrequestsのimport
import os
import time
from datetime import datetime, timezone
import pytz
import urllib.request, urllib.error
from linebot import LineBotApi
from linebot.models import TextSendMessage
import json

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
# line messaging APIのトークン
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")

line_name_dict = {
    "odpt.Railway:TokyoMetro.Ginza": "銀座線",
    "odpt.Railway:TokyoMetro.Marunouchi": "丸ノ内線",
    "odpt.Railway:TokyoMetro.Chiyoda": "千代田線",
    "odpt.Railway:TokyoMetro.Tozai": "東西線",
    "odpt.Railway:TokyoMetro.Yurakucho": "有楽町線",
    "odpt.Railway:TokyoMetro.Fukutoshin": "副都心線",
    "odpt.Railway:TokyoMetro.Hanzomon": "半蔵門線",
    "odpt.Railway:TokyoMetro.Hibiya": "日比谷線",
    "odpt.Railway:TokyoMetro.Namboku": "南北線",
}

def lambda_handler(event, context):
    """
    lambda_handler
    """
    print('event: {}'.format(event))
    print('context: {}'.format(context))

    URL = os.getenv("URL")
    response_body = urllib.request.urlopen(url=URL).read()
    data_dict = json.loads(response_body)
    print(data_dict)

    # 現在時刻
    now = datetime.now(tz=timezone.utc)
    tokyo = pytz.timezone('Asia/Tokyo')
    # 東京のローカル時間に変換
    jst_now = tokyo.normalize(now.astimezone(tokyo))
    content0 = jst_now.strftime("%m月%d日 %H:%M現在")

    info_list = []
    for t in range(9):
        line_name = data_dict[t]["odpt:railway"]
        train_info_text = data_dict[t]["odpt:trainInformationText"]["ja"]

        content = []
        # 路線名
        content1 = line_name_dict[line_name]

        # 運行状況（詳細）
        content3 = train_info_text

        # lineに通知するメッセージを組み立て
        content.append("●" + content1)
        content.append(content3)

        info_list.append(content)

    content_text = []
    for i in range(9):
        content_text.append('\n'.join(info_list[i]))

    notification_message = content0 +'\n' + '\n\n'.join(content_text)

    line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
    line_bot_api.broadcast(TextSendMessage(text=notification_message))

    return {
        'status_code': 200
    }

if __name__ == "__main__":
    print(lambda_handler(event=None, context=None))
