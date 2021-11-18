# tokyometro_operation_info

### [東京メトロ](https://www.tokyometro.jp/index.html)の運行情報を[LINE Messaging API](https://developers.line.biz/ja/services/messaging-api/)にてLINE botとして通知する

- [東京メトロオープンデータ開発者サイト](https://developer.tokyometroapp.jp/info) に登録　　＜※[ユーザ登録申請](https://developer.tokyometroapp.jp/ja/users/sign_up)→承認まで２営業日＞
- APIを利用して、運行情報を取得
- AWS Lambda で定期実行するように対応　　　　　（毎日 JST:6:00～22:00の間、毎時00分に実行）
- トリガーは、EventBridge (旧 CloudWatch Events)で設定
- ログは、Amazon SNS により Cloud Trail Logs へ送信

　

### 利用ライブラリ：
- pytz　　...UTC→JSTへ変換する際に利用　※Linuxの時間はUTCで管理されているため、通知前にJSTへ変換する必要あり
- line-bot-sdk

　

### 使用技術：
- Python 3.8
- AWS
  - Lambda
  - EventBridge
  - SNS
  - CloudTrailLogs

　

### 執筆記事：[AWS Lambdaで列車運行情報を定期的にLINEへ通知してみた【Python】](https://zenn.dev/whitecat_22/articles/9681ab7c85519c)
<a href="https://zenn.dev/whitecat_22/articles/9681ab7c85519c">
  <img src="https://github.com/whitecat-22/tokyometro_operation_info/blob/main/zenn.png">
</a>

　
### 通知結果
#### ●平常時（支障なし）

![tokyometro_operation_info.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info.PNG "tokyometro_operation_info.PNG")

　

#### ●支障あり
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
