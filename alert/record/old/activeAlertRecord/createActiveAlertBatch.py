"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createActiveAlertBatch
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Batch create active alerts
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_active_alerts_in_batch.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime
import time


current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def createActiveAlertBatch_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"activeAlertList": [{"assetId": "AvxV8hkR",
                                 "modelId": "Python_Demo_Model",
                                 "measurepointId": "Int_MeasurementPoint",
                                 "value": 10,
                                 "occurTime": current_utc,
                                 # Optional Parameter
                                 "localOccurTime": current_local,
                                 "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                                 "modelIdPath": "/Python_Demo_Model",
                                 "severityId": "AA1_severityId",
                                 "severityDesc": {"defaultValue": "Default_AA1_severityDescription",
                                                  "i18nValue": {"en_US": "AA1_severityDescription",
                                                                "zh_CN": "AA1_严重性 描述",
                                                                "ja_JP": "AA1_重大度説明",
                                                                "es_ES": "AA1_severidad Descripción"}},
                                 "typeId": "AA1_typeId",
                                 "typeDesc": {"defaultValue": "Default_AA1_typeDescription",
                                              "i18nValue": {"en_US": "AA1_typeDescription",
                                                            "zh_CN": "AA1_类型描述",
                                                            "ja_JP": "AA1_タイプの説明",
                                                            "es_ES": "AA1_descripción del tipo"}},
                                 "subTypeId": "AA1_subTypeId",
                                 "subTypeDesc": {"defaultValue": "Default_AA1_subtypeDescription",
                                                 "i18nValue": {"en_US": "AA1_subtypeDescription",
                                                               "zh_CN": "AA1_子类型描述",
                                                               "ja_JP": "AA1_サブタイプの説明",
                                                               "es_ES": "AA1_descripción del subtipo"}},
                                 "contentId": "AA1_contentId",
                                 "contentDesc": {"defaultValue": "Default_AA1_contentDescription",
                                                 "i18nValue": {"en_US": "AA1_contentDescription",
                                                               "zh_CN": "AA1_内容描述",
                                                               "ja_JP": "AA1_コンテンツの説明",
                                                               "es_ES": "AA1_descripción del contenido"}},
                                 "tag": {"ActiveAlert1Key1": "ActiveAlert1Value1",
                                         "ActiveAlert1Key2": "ActiveAlert1Value2",
                                         "ActiveAlert1Key3": "ActiveAlert1Value3"},
                                 },
                                {"assetId": "AvxV8hkR",
                                 "modelId": "Python_Demo_Model",
                                 "measurepointId": "Int_MeasurementPoint",
                                 "value": 10,
                                 "occurTime": current_utc,
                                 # Optional Parameter
                                 "localOccurTime": current_local,
                                 "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                                 "modelIdPath": "/Python_Demo_Model",
                                 "severityId": "AA2_severityId",
                                 "severityDesc": {"defaultValue": "Default_AA2_severityDescription",
                                                  "i18nValue": {"en_US": "AA2_severityDescription",
                                                                "zh_CN": "AA2_严重性 描述",
                                                                "ja_JP": "AA2_重大度説明",
                                                                "es_ES": "AA2_severidad Descripción"}},
                                 "typeId": "AA2_typeId",
                                 "typeDesc": {"defaultValue": "Default_AA2_typeDescription",
                                              "i18nValue": {"en_US": "AA2_typeDescription",
                                                            "zh_CN": "AA2_类型描述",
                                                            "ja_JP": "AA2_タイプの説明",
                                                            "es_ES": "AA2_descripción del tipo"}},
                                 "subTypeId": "AA2_subTypeId",
                                 "subTypeDesc": {"defaultValue": "Default_AA2_subtypeDescription",
                                                 "i18nValue": {"en_US": "AA2_subtypeDescription",
                                                               "zh_CN": "AA2_子类型描述",
                                                               "ja_JP": "AA2_サブタイプの説明",
                                                               "es_ES": "AA2_descripción del subtipo"}},
                                 "contentId": "AA2_contentId",
                                 "contentDesc": {"defaultValue": "Default_AA2_contentDescription",
                                                 "i18nValue": {"en_US": "AA2_contentDescription",
                                                               "zh_CN": "AA2_内容描述",
                                                               "ja_JP": "AA2_コンテンツの説明",
                                                               "es_ES": "AA2_descripción del contenido"}},
                                 "tag": {"ActiveAlert2Key1": "ActiveAlert2Value1",
                                         "ActiveAlert2Key2": "ActiveAlert2Value2",
                                         "ActiveAlert2Key3": "ActiveAlert2Value3"},
                                 }]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    batchlist = response['data']
    alertIdlist = []

    for i in range(len(batchlist)):
        alertId = batchlist[i]['data']
        alertIdlist.append(alertId)

    print(alertIdlist)
    return alertIdlist


def createActiveAlertBatch_deviceStatus(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"activeAlertList": [{"assetId": "AvxV8hkR",
                                 "modelId": "Python_Demo_Model",
                                 "deviceStatus": "offline",
                                 "value": "offline",
                                 "occurTime": current_utc,
                                 # Optional Parameter
                                 "localOccurTime": current_local,
                                 "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                                 "modelIdPath": "/Python_Demo_Model",
                                 "severityId": "AA3_severityId",
                                 "severityDesc": {"defaultValue": "Default_AA3_severityDescription",
                                                  "i18nValue": {"en_US": "AA3_severityDescription",
                                                                "zh_CN": "AA31_严重性 描述",
                                                                "ja_JP": "AA3_重大度説明",
                                                                "es_ES": "AA3_severidad Descripción"}},
                                 "typeId": "AA3_typeId",
                                 "typeDesc": {"defaultValue": "Default_AA3_typeDescription",
                                              "i18nValue": {"en_US": "AA3_typeDescription",
                                                            "zh_CN": "AA3_类型描述",
                                                            "ja_JP": "AA3_タイプの説明",
                                                            "es_ES": "AA3_descripción del tipo"}},
                                 "subTypeId": "AA3_subTypeId",
                                 "subTypeDesc": {"defaultValue": "Default_AA3_subtypeDescription",
                                                 "i18nValue": {"en_US": "AA3_subtypeDescription",
                                                               "zh_CN": "AA3_子类型描述",
                                                               "ja_JP": "AA3_サブタイプの説明",
                                                               "es_ES": "AA3_descripción del subtipo"}},
                                 "contentId": "AA3_contentId",
                                 "contentDesc": {"defaultValue": "Default_AA3_contentDescription",
                                                 "i18nValue": {"en_US": "AA3_contentDescription",
                                                               "zh_CN": "AA3_内容描述",
                                                               "ja_JP": "AA3_コンテンツの説明",
                                                               "es_ES": "AA3_descripción del contenido"}},
                                 "tag": {"ActiveAlert3Key1": "ActiveAlert3Value1",
                                         "ActiveAlert3Key2": "ActiveAlert3Value2",
                                         "ActiveAlert3Key3": "ActiveAlert3Value3"},
                                 },
                                {"assetId": "AvxV8hkR",
                                 "modelId": "Python_Demo_Model",
                                 "deviceStatus": "offline",
                                 "value": "offline",
                                 "occurTime": current_utc,
                                 # Optional Parameter
                                 "localOccurTime": current_local,
                                 "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                                 "modelIdPath": "/Python_Demo_Model",
                                 "severityId": "AA4_severityId",
                                 "severityDesc": {"defaultValue": "Default_AA4_severityDescription",
                                                  "i18nValue": {"en_US": "AA4_severityDescription",
                                                                "zh_CN": "AA4_严重性 描述",
                                                                "ja_JP": "AA4_重大度説明",
                                                                "es_ES": "AA4_severidad Descripción"}},
                                 "typeId": "AA4_typeId",
                                 "typeDesc": {"defaultValue": "Default_AA4_typeDescription",
                                              "i18nValue": {"en_US": "AA4_typeDescription",
                                                            "zh_CN": "AA4_类型描述",
                                                            "ja_JP": "AA4_タイプの説明",
                                                            "es_ES": "AA4_descripción del tipo"}},
                                 "subTypeId": "AA4_subTypeId",
                                 "subTypeDesc": {"defaultValue": "Default_AA4_subtypeDescription",
                                                 "i18nValue": {"en_US": "AA4_subtypeDescription",
                                                               "zh_CN": "AA4_子类型描述",
                                                               "ja_JP": "AA4_サブタイプの説明",
                                                               "es_ES": "AA4_descripción del subtipo"}},
                                 "contentId": "AA4_contentId",
                                 "contentDesc": {"defaultValue": "Default_AA4_contentDescription",
                                                 "i18nValue": {"en_US": "AA4_contentDescription",
                                                               "zh_CN": "AA4_内容描述",
                                                               "ja_JP": "AA4_コンテンツの説明",
                                                               "es_ES": "AA4_descripción del contenido"}},
                                 "tag": {"ActiveAlert4Key1": "ActiveAlert4Value1",
                                         "ActiveAlert4Key2": "ActiveAlert4Value2",
                                         "ActiveAlert4Key3": "ActiveAlert4Value3"},
                                 }]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    batchlist = response['data']
    alertIdlist = []

    for i in range(len(batchlist)):
        alertId = batchlist[i]['data']
        alertIdlist.append(alertId)

    print(alertIdlist)
    return alertIdlist


def createActiveAlertBatch_mix(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"activeAlertList": [{"assetId": "AvxV8hkR",
                                 "modelId": "Python_Demo_Model",
                                 "measurepointId": "Int_MeasurementPoint",
                                 "value": 10,
                                 "occurTime": current_utc,
                                 # Optional Parameter
                                 "localOccurTime": current_local,
                                 "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                                 "modelIdPath": "/Python_Demo_Model",
                                 "severityId": "AA5_severityId",
                                 "severityDesc": {"defaultValue": "Default_AA5_severityDescription",
                                                  "i18nValue": {"en_US": "AA5_severityDescription",
                                                                "zh_CN": "AA51_严重性 描述",
                                                                "ja_JP": "AA5_重大度説明",
                                                                "es_ES": "AA5_severidad Descripción"}},
                                 "typeId": "AA5_typeId",
                                 "typeDesc": {"defaultValue": "Default_AA5_typeDescription",
                                              "i18nValue": {"en_US": "AA5_typeDescription",
                                                            "zh_CN": "AA5_类型描述",
                                                            "ja_JP": "AA5_タイプの説明",
                                                            "es_ES": "AA5_descripción del tipo"}},
                                 "subTypeId": "AA5_subTypeId",
                                 "subTypeDesc": {"defaultValue": "Default_AA5_subtypeDescription",
                                                 "i18nValue": {"en_US": "AA5_subtypeDescription",
                                                               "zh_CN": "AA5_子类型描述",
                                                               "ja_JP": "AA5_サブタイプの説明",
                                                               "es_ES": "AA5_descripción del subtipo"}},
                                 "contentId": "AA5_contentId",
                                 "contentDesc": {"defaultValue": "Default_AA5_contentDescription",
                                                 "i18nValue": {"en_US": "AA5_contentDescription",
                                                               "zh_CN": "AA5_内容描述",
                                                               "ja_JP": "AA5_コンテンツの説明",
                                                               "es_ES": "AA5_descripción del contenido"}},
                                 "tag": {"ActiveAlert5Key1": "ActiveAlert5Value1",
                                         "ActiveAlert5Key2": "ActiveAlert5Value2",
                                         "ActiveAlert5Key3": "ActiveAlert5Value3"},
                                 },
                                {"assetId": "AvxV8hkR",
                                 "modelId": "Python_Demo_Model",
                                 "deviceStatus": "offline",
                                 "value": "offline",
                                 "occurTime": current_utc,
                                 # Optional Parameter
                                 "localOccurTime": current_local,
                                 "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                                 "modelIdPath": "/Python_Demo_Model",
                                 "severityId": "AA6_severityId",
                                 "severityDesc": {"defaultValue": "Default_AA6_severityDescription",
                                                  "i18nValue": {"en_US": "AA6_severityDescription",
                                                                "zh_CN": "AA6_严重性 描述",
                                                                "ja_JP": "AA6_重大度説明",
                                                                "es_ES": "AA6_severidad Descripción"}},
                                 "typeId": "AA6_typeId",
                                 "typeDesc": {"defaultValue": "Default_AA6_typeDescription",
                                              "i18nValue": {"en_US": "AA6_typeDescription",
                                                            "zh_CN": "AA6_类型描述",
                                                            "ja_JP": "AA6_タイプの説明",
                                                            "es_ES": "AA6_descripción del tipo"}},
                                 "subTypeId": "AA6_subTypeId",
                                 "subTypeDesc": {"defaultValue": "Default_AA6_subtypeDescription",
                                                 "i18nValue": {"en_US": "AA6_subtypeDescription",
                                                               "zh_CN": "AA6_子类型描述",
                                                               "ja_JP": "AA6_サブタイプの説明",
                                                               "es_ES": "AA6_descripción del subtipo"}},
                                 "contentId": "AA6_contentId",
                                 "contentDesc": {"defaultValue": "Default_AA6_contentDescription",
                                                 "i18nValue": {"en_US": "AA6_contentDescription",
                                                               "zh_CN": "AA6_内容描述",
                                                               "ja_JP": "AA6_コンテンツの説明",
                                                               "es_ES": "AA6_descripción del contenido"}},
                                 "tag": {"ActiveAlert6Key1": "ActiveAlert6Value1",
                                         "ActiveAlert6Key2": "ActiveAlert6Value2",
                                         "ActiveAlert6Key3": "ActiveAlert6Value3"},
                                 }]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    batchlist = response['data']
    alertIdlist = []

    for i in range(len(batchlist)):
        alertId = batchlist[i]['data']
        alertIdlist.append(alertId)

    print(alertIdlist)
    return alertIdlist
