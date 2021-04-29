"""
lambda_function.py
"""
# postリクエストをline notify APIに送るためにrequestsのimport
import os
import time
import requests
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime, timezone
import pytz
from linebot import LineBotApi
from linebot.models import TextSendMessage

url_list = [
    "https://www.tokyometro.jp/unkou/history/ginza.html",
    "https://www.tokyometro.jp/unkou/history/marunouchi.html",
    "https://www.tokyometro.jp/unkou/history/hibiya.html",
    "https://www.tokyometro.jp/unkou/history/touzai.html",
    "https://www.tokyometro.jp/unkou/history/chiyoda.html",
    "https://www.tokyometro.jp/unkou/history/yurakucho.html",
    "https://www.tokyometro.jp/unkou/history/hanzoumon.html",
    "https://www.tokyometro.jp/unkou/history/nanboku.html",
    "https://www.tokyometro.jp/unkou/history/fukutoshin.html"
]

# line messaging APIのトークン
line_access_token = os.getenv("LINE_ACCESS_TOKEN")


def move_bin(
    fname: str, src_dir: str = "/var/task/bin", dest_dir: str = "/tmp/bin"
) -> None:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    dest_file = os.path.join(dest_dir, fname)
    shutil.copy2(os.path.join(src_dir, fname), dest_file)
    os.chmod(dest_file, 0o775)


def create_driver(
    options: webdriver.chrome.options.Options,
) -> webdriver.chrome.webdriver:
    driver = webdriver.Chrome(
        executable_path="/tmp/bin/chromedriver", chrome_options=options
    )
    return driver


def lambda_handler(event, context):
    """
    lambda_handler
    """
    print('event: {}'.format(event))
    print('context: {}'.format(context))

    move_bin("headless-chromium")
    move_bin("chromedriver")

    #headless_chromium = os.getenv('HEADLESS_CHROMIUM', '')
    #chromedriver = os.getenv('CHROMEDRIVER', '')
    # webdriverの設定
    options = Options()
    #options.binary_location = headless_chromium
    options.binary_location = "/tmp/bin/headless-chromium"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--homedir=/tmp")

    driver = create_driver(options)
    # driver = webdriver.Chrome(executable_path=chromedriver, options=options)

    # 現在時刻
    now = datetime.now(tz=timezone.utc)
    tokyo = pytz.timezone('Asia/Tokyo')
    # 東京のローカル時間に変換
    jst_now = tokyo.normalize(now.astimezone(tokyo))
    content0 = jst_now.strftime("%m月%d日 %H:%M現在")

    info_list = []
    for url in url_list:
        content = []
        driver.get(url)
        time.sleep(1)
        # 路線名
        content1 = driver.find_element_by_css_selector("#v2_contents > div.v2_contents > div > div.v2_headingH1.v2_headingRoute > h1")
        # 運行状況（概要）
        content2 = driver.find_element_by_css_selector("#v2_contents > div.v2_contents > div > div.v2_gridC.v2_section.v2_clear.v2_stationUnkouMap.v3_stationUnkouMap > div.v2_sectionS.v2_gridCRow > div.v2_unkouReportInfo > div > div > div.v2_unkouReportTxtCaption.v3_unkouReportTxtCaption > p")
        # 運行状況（詳細）
        content3 = driver.find_elements_by_css_selector("#v2_contents > div.v2_contents > div > div.v2_gridC.v2_section.v2_clear.v2_stationUnkouMap.v3_stationUnkouMap > div.v2_sectionS.v2_gridCRow > div.v2_unkouReportInfo > div > p")

        # lineに通知するメッセージを組み立て
        content.append("●" + content1.text[:-5])
        content.append(content2.text)
        for content3s in content3:
            content.append(content3s.text)

        info_list.append(content)

    content_text = []
    for i in range(9):
        content_text.append('\n'.join(info_list[i]))

    notification_message = content0 +'\n' + '\n\n'.join(content_text)

    driver.close()
    driver.quit()

    line_bot_api = LineBotApi(line_access_token)
    line_bot_api.broadcast(TextSendMessage(text=notification_message))

    return {
        'status_code': 200
    }

if __name__ == "__main__":
    print(lambda_handler(event=None, context=None))
