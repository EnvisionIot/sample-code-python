"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createHistoryAlert
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description: Create a new history alert. Except for the mandatory fields, there is no need to verify the legality of other parameters. The parameters used by users such as contentId would not be maintained on the EnOS platform. Alerts with the same assetId, measurepointId, and occurTime will be updated
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_history_alert.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def createHistoryAlert_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"historyAlert": {"assetId": "AvxV8hkR",
                           "modelId": "Python_Demo_Model",
                           "measurepointId": "Int_MeasurementPoint",
                           "value": 10,
                           "occurTime": current_utc,
                           "recoverTime": current_utc,
                           # Optional Parameter
                           "localOccurTime": current_local,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_HisotryAlert_recoverReason",
                           "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                           "modelIdPath": "/Python_Demo_Model",
                           "severityId": "HA_severityId",
                           "severityDesc": {"defaultValue": "Default_HA_severityDescription",
                                            "i18nValue": {"en_US": "HA_severityDescription",
                                                          "zh_CN": "HA_严重性 描述",
                                                          "ja_JP": "HA_重大度説明",
                                                          "es_ES": "HA_severidad Descripción"}},
                           "typeId": "HA_typeId",
                           "typeDesc": {"defaultValue": "Default_HA_typeDescription",
                                        "i18nValue": {"en_US": "HA_typeDescription",
                                                      "zh_CN": "HA_类型描述",
                                                      "ja_JP": "HA_タイプの説明",
                                                      "es_ES": "HA_descripción del tipo"}},
                           "subTypeId": "HA_subTypeId",
                           "subTypeDesc": {"defaultValue": "Default_HA_subtypeDescription",
                                           "i18nValue": {"en_US": "HA_subtypeDescription",
                                                         "zh_CN": "HA_子类型描述",
                                                         "ja_JP": "HA_サブタイプの説明",
                                                         "es_ES": "HA_descripción del subtipo"}},
                           "contentId": "HA_contentId",
                           "contentDesc": {"defaultValue": "Default_HA_contentDescription",
                                           "i18nValue": {"en_US": "HA_contentDescription",
                                                         "zh_CN": "HA_内容描述",
                                                         "ja_JP": "HA_コンテンツの説明",
                                                         "es_ES": "HA_descripción del contenido"}},
                           "tag": {"HistoryAlertKey1": "HistoryAlertValue1",
                                   "HistoryAlertKey2": "HistoryAlertValue2",
                                   "HistoryAlertKey3": "HistoryAlertValue3"},
                           }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createHistoryAlert_deviceStatus(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"historyAlert": {"assetId": "AvxV8hkR",
                           "modelId": "Python_Demo_Model",
                           "deviceStatus": "offline",
                           "value": "offline",
                           "occurTime": current_utc,
                           "recoverTime": current_utc,
                           # Optional Parameter
                           "localOccurTime": current_local,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_HisotryAlert_recoverReason",
                           "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                           "modelIdPath": "/Python_Demo_Model",
                           "severityId": "HA_severityId",
                           "severityDesc": {"defaultValue": "Default_HA_severityDescription",
                                            "i18nValue": {"en_US": "HA_severityDescription",
                                                          "zh_CN": "HA_严重性 描述",
                                                          "ja_JP": "HA_重大度説明",
                                                          "es_ES": "HA_severidad Descripción"}},
                           "typeId": "HA_typeId",
                           "typeDesc": {"defaultValue": "Default_HA_typeDescription",
                                        "i18nValue": {"en_US": "HA_typeDescription",
                                                      "zh_CN": "HA_类型描述",
                                                      "ja_JP": "HA_タイプの説明",
                                                      "es_ES": "HA_descripción del tipo"}},
                           "subTypeId": "HA_subTypeId",
                           "subTypeDesc": {"defaultValue": "Default_HA_subtypeDescription",
                                           "i18nValue": {"en_US": "HA_subtypeDescription",
                                                         "zh_CN": "HA_子类型描述",
                                                         "ja_JP": "HA_サブタイプの説明",
                                                         "es_ES": "HA_descripción del subtipo"}},
                           "contentId": "HA_contentId",
                           "contentDesc": {"defaultValue": "Default_HA_contentDescription",
                                           "i18nValue": {"en_US": "HA_contentDescription",
                                                         "zh_CN": "HA_内容描述",
                                                         "ja_JP": "HA_コンテンツの説明",
                                                         "es_ES": "HA_descripción del contenido"}},
                           "tag": {"HistoryAlertKey1": "HistoryAlertValue1",
                                   "HistoryAlertKey2": "HistoryAlertValue2",
                                   "HistoryAlertKey3": "HistoryAlertValue3"},
                           }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


