# tokyometro_operation_info

### [東京メトロ](https://www.tokyometro.jp/index.html)の運行情報を[LINE Messaging API](https://developers.line.biz/ja/services/messaging-api/)にてLINE botとして通知する

- [公共交通オープンデータセンター 開発者サイト](https://developer.odpt.org/)に登録　　＜※[ユーザ登録申請](https://developer.odpt.org/users/sign_up)→承認まで２営業日＞
- APIを利用して、運行情報を取得
- AWS Lambda で定期実行するように対応　　　　　（毎日 JST:6:00～22:00の間、毎時00分に実行）
- トリガーは、EventBridge (旧 CloudWatch Events)で設定
- ログは、Amazon SNS により Cloud Trail Logs へ送信

　

### ◆利用ライブラリ：
- [pytz](https://pythonhosted.org/pytz/)  
　[UTC(協定世界時)](https://ja.wikipedia.org/wiki/%E5%8D%94%E5%AE%9A%E4%B8%96%E7%95%8C%E6%99%82)→[JST(日本標準時)](https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)へ変換する際に利用  
　※Linuxの時間はUTCで管理されているため、通知前にJSTへ変換する必要あり  
- [line-bot-sdk](https://github.com/line/line-bot-sdk-python)

　

### ◆使用技術：
- [Python](https://www.python.org/) 3.8
- AWS
  - [Lambda](https://aws.amazon.com/jp/lambda/?nc2=h_ql_prod_serv_lbd)
  - [EventBridge](https://aws.amazon.com/jp/eventbridge/?nc2=h_ql_prod_serv_eb)
  - [SNS](https://aws.amazon.com/jp/sns/?nc2=h_ql_prod_ap_sns&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
  - [CloudTrailLogs](https://aws.amazon.com/jp/cloudtrail/?nc2=h_ql_prod_mg_ct)

　

### ◆執筆記事：[AWS Lambdaで列車運行情報を定期的にLINEへ通知してみた【Python】](https://zenn.dev/whitecat_22/articles/9681ab7c85519c)
<a href="https://zenn.dev/whitecat_22/articles/9681ab7c85519c">
  <img src="https://github.com/whitecat-22/tokyometro_operation_info/blob/main/zenn.png">
</a>

　
### ◆通知結果：
#### ●平常時（支障なし）：

![tokyometro_operation_info.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info.PNG "tokyometro_operation_info.PNG")

　

#### ●支障あり：
(1)
![tokyometro_operation_info02.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info02.PNG)

　

(2)
![tokyometro_operation_info03.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info03.PNG)

　

(3)
![tokyometro_operation_info04.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info04.PNG)

　

(4)
![tokyometro_operation_info05.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info05.PNG)

　

(5)
![tokyometro_operation_info06.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info06.PNG)
