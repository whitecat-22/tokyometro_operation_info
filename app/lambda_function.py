"""
lambda_function.py
"""
# postリクエストをline notify APIに送るためにrequestsのimport
import os
import time
from datetime import datetime, timezone
import pytz
import urllib.request, urllib.error
from linebot import LineBotApi
from linebot.models import TextSendMessage
import json

consumer_key = os.getenv("CONSUMER_KEY")

# line messaging APIのトークン
line_access_token = os.getenv("LINE_ACCESS_TOKEN")


def lambda_handler(event, context):
    """
    lambda_handler
    """
    print('event: {}'.format(event))
    print('context: {}'.format(context))

    url = os.getenv("URL")
    response_body = urllib.request.urlopen(url=url).read()
    data_dict = json.loads(response_body)

    # 現在時刻
    now = datetime.now(tz=timezone.utc)
    tokyo = pytz.timezone('Asia/Tokyo')
    # 東京のローカル時間に変換
    jst_now = tokyo.normalize(now.astimezone(tokyo))
    content0 = jst_now.strftime("%m月%d日 %H:%M現在")

    info_list = []
    for t in range(9):
        line_name = data_dict[t]["odpt:railway"]
        train_info_text = data_dict[t]["odpt:trainInformationText"]

        content = []
        # 路線名
        if line_name == "odpt.Railway:TokyoMetro.Hanzomon":
            line_name_text = "半蔵門線"
        elif line_name == "odpt.Railway:TokyoMetro.Yurakucho":
            line_name_text = "有楽町線"
        elif line_name == "odpt.Railway:TokyoMetro.Namboku":
            line_name_text = "南北線"
        elif line_name == "odpt.Railway:TokyoMetro.Tozai":
            line_name_text = "東西線"
        elif line_name == "odpt.Railway:TokyoMetro.Marunouchi":
            line_name_text = "丸ノ内線"
        elif line_name == "odpt.Railway:TokyoMetro.Ginza":
            line_name_text = "銀座線"
        elif line_name == "odpt.Railway:TokyoMetro.Chiyoda":
            line_name_text = "千代田線"
        elif line_name == "odpt.Railway:TokyoMetro.Fukutoshin":
            line_name_text = "副都心線"
        elif line_name == "odpt.Railway:TokyoMetro.Hibiya":
            line_name_text = "日比谷線"

        content1 = line_name_text

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

    line_bot_api = LineBotApi(line_access_token)
    line_bot_api.broadcast(TextSendMessage(text=notification_message))

    return {
        'status_code': 200
    }

if __name__ == "__main__":
    print(lambda_handler(event=None, context=None))
