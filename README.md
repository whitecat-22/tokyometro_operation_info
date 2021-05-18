# tokyometro_operation_info

### 東京メトロの運行情報をLINE Messaging APIにてLINE botとして通知する

- AWS Lambda で定期実行するように対応　（JST:6時～22時の間、毎時00分と30分に実行）
- トリガーは、EventBridge (CloudWatch Events)で設定
- ログは、Amazon SNS により、Cloud Trail Logs へ送信

　
#### 平常時（支障なし）

![tokyometro_operation_info.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info.PNG "tokyometro_operation_info.PNG")

　

#### 支障あり

![tokyometro_operation_info02.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info02.PNG)

　

![tokyometro_operation_info03.PNG](https://github.com/whitecat-22/tokyometro_operation_info/blob/main/tokyometro_operation_info03.PNG)
