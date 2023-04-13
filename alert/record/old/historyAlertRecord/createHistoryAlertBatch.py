"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createHistoryAlertBatch
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description: Batch create history alerts
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_history_alerts_in_batch.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def createHistoryAlertBatch_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"historyAlertList": [{"assetId": "AvxV8hkR",
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
                                "severityId": "HA1_severityId",
                                "severityDesc": {"defaultValue": "Default_HA1_severityDescription",
                                                 "i18nValue": {"en_US": "HA1_severityDescription",
                                                               "zh_CN": "HA1_严重性 描述",
                                                               "ja_JP": "HA1_重大度説明",
                                                               "es_ES": "HA1_severidad Descripción"}},
                                "typeId": "HA1_typeId",
                                "typeDesc": {"defaultValue": "Default_HA1_typeDescription",
                                             "i18nValue": {"en_US": "HA1_typeDescription",
                                                           "zh_CN": "HA1_类型描述",
                                                           "ja_JP": "HA1_タイプの説明",
                                                           "es_ES": "HA1_descripción del tipo"}},
                                "subTypeId": "HA1_subTypeId",
                                "subTypeDesc": {"defaultValue": "Default_HA1_subtypeDescription",
                                                "i18nValue": {"en_US": "HA1_subtypeDescription",
                                                              "zh_CN": "HA1_子类型描述",
                                                              "ja_JP": "HA1_サブタイプの説明",
                                                              "es_ES": "HA1_descripción del subtipo"}},
                                "contentId": "HA1_contentId",
                                "contentDesc": {"defaultValue": "Default_HA1_contentDescription",
                                                "i18nValue": {"en_US": "HA1_contentDescription",
                                                              "zh_CN": "HA1_内容描述",
                                                              "ja_JP": "HA1_コンテンツの説明",
                                                              "es_ES": "HA1_descripción del contenido"}},
                                "tag": {"HistoryAlert1Key1": "HistoryAlert1Value1",
                                        "HistoryAlert1Key2": "HistoryAlert1Value2",
                                        "HistoryAlert1Key3": "HistoryAlert1Value3"},
                                },
                               {"assetId": "AvxV8hkR",
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
                                "severityId": "HA2_severityId",
                                "severityDesc": {"defaultValue": "Default_HA2_severityDescription",
                                                 "i18nValue": {"en_US": "HA2_severityDescription",
                                                               "zh_CN": "HA2_严重性 描述",
                                                               "ja_JP": "HA2_重大度説明",
                                                               "es_ES": "HA2_severidad Descripción"}},
                                "typeId": "HA2_typeId",
                                "typeDesc": {"defaultValue": "Default_HA2_typeDescription",
                                             "i18nValue": {"en_US": "HA2_typeDescription",
                                                           "zh_CN": "HA2_类型描述",
                                                           "ja_JP": "HA2_タイプの説明",
                                                           "es_ES": "HA2_descripción del tipo"}},
                                "subTypeId": "HA2_subTypeId",
                                "subTypeDesc": {"defaultValue": "Default_HA2_subtypeDescription",
                                                "i18nValue": {"en_US": "HA2_subtypeDescription",
                                                              "zh_CN": "HA2_子类型描述",
                                                              "ja_JP": "HA2_サブタイプの説明",
                                                              "es_ES": "HA2_descripción del subtipo"}},
                                "contentId": "HA2_contentId",
                                "contentDesc": {"defaultValue": "Default_HA2_contentDescription",
                                                "i18nValue": {"en_US": "HA2_contentDescription",
                                                              "zh_CN": "HA2_内容描述",
                                                              "ja_JP": "HA2_コンテンツの説明",
                                                              "es_ES": "HA2_descripción del contenido"}},
                                "tag": {"HistoryAlert2Key1": "HistoryAlert2Value1",
                                        "HistoryAlert2Key2": "HistoryAlert2Value2",
                                        "HistoryAlert2Key3": "HistoryAlert2Value3"},
                                }]
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createHistoryAlertBatch_deviceStatus(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"historyAlertList": [{"assetId": "AvxV8hkR",
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
                                "severityId": "HA3_severityId",
                                "severityDesc": {"defaultValue": "Default_HA3_severityDescription",
                                                 "i18nValue": {"en_US": "HA3_severityDescription",
                                                               "zh_CN": "HA3_严重性 描述",
                                                               "ja_JP": "HA3_重大度説明",
                                                               "es_ES": "HA3_severidad Descripción"}},
                                "typeId": "HA3_typeId",
                                "typeDesc": {"defaultValue": "Default_HA3_typeDescription",
                                             "i18nValue": {"en_US": "HA3_typeDescription",
                                                           "zh_CN": "HA3_类型描述",
                                                           "ja_JP": "HA3_タイプの説明",
                                                           "es_ES": "HA3_descripción del tipo"}},
                                "subTypeId": "HA3_subTypeId",
                                "subTypeDesc": {"defaultValue": "Default_HA3_subtypeDescription",
                                                "i18nValue": {"en_US": "HA3_subtypeDescription",
                                                              "zh_CN": "HA3_子类型描述",
                                                              "ja_JP": "HA3_サブタイプの説明",
                                                              "es_ES": "HA3_descripción del subtipo"}},
                                "contentId": "HA3_contentId",
                                "contentDesc": {"defaultValue": "Default_HA3_contentDescription",
                                                "i18nValue": {"en_US": "HA3_contentDescription",
                                                              "zh_CN": "HA3_内容描述",
                                                              "ja_JP": "HA3_コンテンツの説明",
                                                              "es_ES": "HA3_descripción del contenido"}},
                                "tag": {"HistoryAlert3Key1": "HistoryAlert3Value1",
                                        "HistoryAlert3Key2": "HistoryAlert3Value2",
                                        "HistoryAlert3Key3": "HistoryAlert3Value3"},
                                },
                               {"assetId": "AvxV8hkR",
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
                                "severityId": "HA4_severityId",
                                "severityDesc": {"defaultValue": "Default_HA4_severityDescription",
                                                 "i18nValue": {"en_US": "HA4_severityDescription",
                                                               "zh_CN": "HA4_严重性 描述",
                                                               "ja_JP": "HA4_重大度説明",
                                                               "es_ES": "HA4_severidad Descripción"}},
                                "typeId": "HA4_typeId",
                                "typeDesc": {"defaultValue": "Default_HA4_typeDescription",
                                             "i18nValue": {"en_US": "HA4_typeDescription",
                                                           "zh_CN": "HA4_类型描述",
                                                           "ja_JP": "HA4_タイプの説明",
                                                           "es_ES": "HA4_descripción del tipo"}},
                                "subTypeId": "HA4_subTypeId",
                                "subTypeDesc": {"defaultValue": "Default_HA4_subtypeDescription",
                                                "i18nValue": {"en_US": "HA4_subtypeDescription",
                                                              "zh_CN": "HA4_子类型描述",
                                                              "ja_JP": "HA4_サブタイプの説明",
                                                              "es_ES": "HA4_descripción del subtipo"}},
                                "contentId": "HA4_contentId",
                                "contentDesc": {"defaultValue": "Default_HA4_contentDescription",
                                                "i18nValue": {"en_US": "HA4_contentDescription",
                                                              "zh_CN": "HA4_内容描述",
                                                              "ja_JP": "HA4_コンテンツの説明",
                                                              "es_ES": "HA4_descripción del contenido"}},
                                "tag": {"HistoryAlert4Key1": "HistoryAlert4Value1",
                                        "HistoryAlert4Key2": "HistoryAlert4Value2",
                                        "HistoryAlert4Key3": "HistoryAlert4Value3"},
                                }]
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
    

def createHistoryAlertBatch_mix(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"historyAlertList": [{"assetId": "AvxV8hkR",
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
                                "severityId": "HA5_severityId",
                                "severityDesc": {"defaultValue": "Default_HA5_severityDescription",
                                                 "i18nValue": {"en_US": "HA5_severityDescription",
                                                               "zh_CN": "HA5_严重性 描述",
                                                               "ja_JP": "HA5_重大度説明",
                                                               "es_ES": "HA5_severidad Descripción"}},
                                "typeId": "HA5_typeId",
                                "typeDesc": {"defaultValue": "Default_HA5_typeDescription",
                                             "i18nValue": {"en_US": "HA5_typeDescription",
                                                           "zh_CN": "HA5_类型描述",
                                                           "ja_JP": "HA5_タイプの説明",
                                                           "es_ES": "HA5_descripción del tipo"}},
                                "subTypeId": "HA5_subTypeId",
                                "subTypeDesc": {"defaultValue": "Default_HA5_subtypeDescription",
                                                "i18nValue": {"en_US": "HA5_subtypeDescription",
                                                              "zh_CN": "HA5_子类型描述",
                                                              "ja_JP": "HA5_サブタイプの説明",
                                                              "es_ES": "HA5_descripción del subtipo"}},
                                "contentId": "HA5_contentId",
                                "contentDesc": {"defaultValue": "Default_HA5_contentDescription",
                                                "i18nValue": {"en_US": "HA5_contentDescription",
                                                              "zh_CN": "HA5_内容描述",
                                                              "ja_JP": "HA5_コンテンツの説明",
                                                              "es_ES": "HA5_descripción del contenido"}},
                                "tag": {"HistoryAlert5Key1": "HistoryAlert5Value1",
                                        "HistoryAlert5Key2": "HistoryAlert5Value2",
                                        "HistoryAlert5Key3": "HistoryAlert5Value3"},
                                },
                               {"assetId": "AvxV8hkR",
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
                                "severityId": "HA6_severityId",
                                "severityDesc": {"defaultValue": "Default_HA6_severityDescription",
                                                 "i18nValue": {"en_US": "HA6_severityDescription",
                                                               "zh_CN": "HA6_严重性 描述",
                                                               "ja_JP": "HA6_重大度説明",
                                                               "es_ES": "HA6_severidad Descripción"}},
                                "typeId": "HA6_typeId",
                                "typeDesc": {"defaultValue": "Default_HA6_typeDescription",
                                             "i18nValue": {"en_US": "HA6_typeDescription",
                                                           "zh_CN": "HA6_类型描述",
                                                           "ja_JP": "HA6_タイプの説明",
                                                           "es_ES": "HA6_descripción del tipo"}},
                                "subTypeId": "HA6_subTypeId",
                                "subTypeDesc": {"defaultValue": "Default_HA6_subtypeDescription",
                                                "i18nValue": {"en_US": "HA6_subtypeDescription",
                                                              "zh_CN": "HA6_子类型描述",
                                                              "ja_JP": "HA6_サブタイプの説明",
                                                              "es_ES": "HA6_descripción del subtipo"}},
                                "contentId": "HA6_contentId",
                                "contentDesc": {"defaultValue": "Default_HA6_contentDescription",
                                                "i18nValue": {"en_US": "HA6_contentDescription",
                                                              "zh_CN": "HA6_内容描述",
                                                              "ja_JP": "HA6_コンテンツの説明",
                                                              "es_ES": "HA6_descripción del contenido"}},
                                "tag": {"HistoryAlert6Key1": "HistoryAlert6Value1",
                                        "HistoryAlert6Key2": "HistoryAlert6Value2",
                                        "HistoryAlert6Key3": "HistoryAlert6Value3"},
                                }]
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

