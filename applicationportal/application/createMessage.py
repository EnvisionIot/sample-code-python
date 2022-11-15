"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createMessage
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Create common messages and alert messages on the Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/create_message.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime

current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def createMessage(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/message/produce"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"messages": [{"messageId": "test_messageId",
                          "orgId": orgId,
                          "accessKey": accessKey,
                          "produceTime": current_time,
                          "zoneOffset": "+08:00",
                          "authUnitId": "G5M8Ojhd",
                          "callbackUrl": "/",
                          "actionName": {"en_US": "ACK",
                                         "zh_CN": "确认",
                                         "ja_JP": "はい",
                                         "es_ES": "Sí"},
                          "type": 1,
                          "body": {"default": "Type message here default",
                                   "en_US": "Type message here English",
                                   "zh_CN": "在此处输入中文信息",
                                   "ja_JP": "ここにメッセージを入力してください日本語",
                                   "es_ES": "escriba el mensaje aquí español" },
                          "color": 1,
                          "ring": 1,
                          "tags": [{"default": "Severe",
                                    "en_US": "Severe",
                                    "zh_CN": "严重",
                                    "ja_JP": "重度",
                                    "es_ES": "grave"},
                                   {"default": "Performance Alarm",
                                    "en_US": "Performance Alarm",
                                    "zh_CN": "性能告警",
                                    "ja_JP": "パフォーマンスアラーム",
                                    "es_ES": "alarma de rendimiento"},
                                   {"default": "Inverter",
                                    "en_US": "Inverter",
                                    "zh_CN": "逆变器",
                                    "ja_JP": "インバーター",
                                    "es_ES": "inversora"}],
                          "state": 0,

                          "feature": {"default": "This is a feature test in default",
                                      "en_US": "This is a feature test in english",
                                      "zh_CN": "这是中文的功能测试",
                                      "ja_JP": "これは日本語の機能テストです",
                                      "es_ES": "Esta es una prueba de características en español"},
                          # "linkedAppId": "accessKey",
                          # "linkedMenuCode": "menucode",
                          # "linkedStates": "states",
                          # "assetId": "G5M8Ojhd"
                          }]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
