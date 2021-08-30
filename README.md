# tokyometro_operation_info

### 東京メトロの運行情報をLINE Messaging APIにてLINE botとして通知する

- [東京メトロオープンデータ開発者サイト](https://developer.tokyometroapp.jp/info) に登録
- APIを利用して、運行情報を取得
- AWS Lambda で定期実行するように対応　（平日のJST:6:00～22:30の間、毎時00分と30分に実行）
- トリガーは、EventBridge (CloudWatch Events)で設定
- ログは、Amazon SNS により、Cloud Trail Logs へ送信

### 執筆記事：AWS Lambdaで列車運行情報を定期的にLINEへ通知してみた【Python】
<a href="https://zenn.dev/whitecat_22/articles/9681ab7c85519c">
  <img src="https://github.com/whitecat-22/tokyometro_operation_info/blob/main/zenn.png">
</a>

　
#### ●平常時（支障なし）

![tokyometro_operation_info.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info.PNG "tokyometro_operation_info.PNG")

　

#### ●支障あり

![tokyometro_operation_info02.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info02.PNG)

　

![tokyometro_operation_info03.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info03.PNG)

　

![tokyometro_operation_info04.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info04.PNG)

　

![tokyometro_operation_info05.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info05.PNG)

　

![tokyometro_operation_info06.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info06.PNG)
