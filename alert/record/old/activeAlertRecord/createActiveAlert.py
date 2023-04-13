"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createActiveAlert
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Create an active alert. Except for the mandatory fields, there is no need to verify the legality of other parameters. The parameters used by users such as contentId will not be maintained on the EnOS platform
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_active_alert.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def createActiveAlert_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"activeAlert": {"assetId": "AvxV8hkR",
                          "modelId": "Python_Demo_Model",
                          "measurepointId": "Int_MeasurementPoint",
                          "value": 10,
                          "occurTime": current_utc,
                          # Optional Parameter
                          "localOccurTime": current_local,
                          "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                          "modelIdPath": "/Python_Demo_Model",
                          "severityId": "AA_severityId",
                          "severityDesc": {"defaultValue": "Default_AA_severityDescription",
                                           "i18nValue": {"en_US": "AA_severityDescription",
                                                         "zh_CN": "AA_严重性 描述",
                                                         "ja_JP": "AA_重大度説明",
                                                         "es_ES": "AA_severidad Descripción"}},
                          "typeId": "AA_typeId",
                          "typeDesc": {"defaultValue": "Default_AA_typeDescription",
                                       "i18nValue": {"en_US": "AA_typeDescription",
                                                     "zh_CN": "AA_类型描述",
                                                     "ja_JP": "AA_タイプの説明",
                                                     "es_ES": "AA_descripción del tipo"}},
                          "subTypeId": "AA_subTypeId",
                          "subTypeDesc": {"defaultValue": "Default_AA_subtypeDescription",
                                          "i18nValue": {"en_US": "AA_subtypeDescription",
                                                        "zh_CN": "AA_子类型描述",
                                                        "ja_JP": "AA_サブタイプの説明",
                                                        "es_ES": "AA_descripción del subtipo"}},
                          "contentId": "AA_contentId",
                          "contentDesc": {"defaultValue": "Default_AA_contentDescription",
                                          "i18nValue": {"en_US": "AA_contentDescription",
                                                        "zh_CN": "AA_内容描述",
                                                        "ja_JP": "AA_コンテンツの説明",
                                                        "es_ES": "AA_descripción del contenido"}},
                          "tag": {"ActiveAlertKey1": "ActiveAlertValue1",
                                  "ActiveAlertKey2": "ActiveAlertValue2",
                                  "ActiveAlertKey3": "ActiveAlertValue3"},
                          }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    alertId = response['data']
    return alertId


def createActiveAlert_deviceStatus(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"activeAlert": {"assetId": "AvxV8hkR",
                            "modelId": "Python_Demo_Model",
                            "deviceStatus": "offline",
                            "value": "offline",
                            "occurTime": current_utc,
                            # Optional Parameter
                            "localOccurTime": current_local,
                            "assetPath": ["LlrLCZqt:/AvxV8hkR/pqXwiK5U/LKnsI2hG", "treeId1:/assetId1/assetIdx"],
                            "modelIdPath": "/Python_Demo_Model",
                            "severityId": "AA_severityId",
                            "severityDesc": {"defaultValue": "Default_AA_severityDescription",
                                             "i18nValue": {"en_US": "AA_severityDescription",
                                                           "zh_CN": "AA_严重性 描述",
                                                           "ja_JP": "AA_重大度説明",
                                                           "es_ES": "AA_severidad Descripción"}},
                            "typeId": "AA_typeId",
                            "typeDesc": {"defaultValue": "Default_AA_typeDescription",
                                         "i18nValue": {"en_US": "AA_typeDescription",
                                                       "zh_CN": "AA_类型描述",
                                                       "ja_JP": "AA_タイプの説明",
                                                       "es_ES": "AA_descripción del tipo"}},
                            "subTypeId": "AA_subTypeId",
                            "subTypeDesc": {"defaultValue": "Default_AA_subtypeDescription",
                                            "i18nValue": {"en_US": "AA_subtypeDescription",
                                                          "zh_CN": "AA_子类型描述",
                                                          "ja_JP": "AA_サブタイプの説明",
                                                          "es_ES": "AA_descripción del subtipo"}},
                            "contentId": "AA_contentId",
                            "contentDesc": {"defaultValue": "Default_AA_contentDescription",
                                            "i18nValue": {"en_US": "AA_contentDescription",
                                                          "zh_CN": "AA_内容描述",
                                                          "ja_JP": "AA_コンテンツの説明",
                                                          "es_ES": "AA_descripción del contenido"}},
                            "tag": {"ActiveAlertKey1": "ActiveAlertValue1",
                                    "ActiveAlertKey2": "ActiveAlertValue2",
                                    "ActiveAlertKey3": "ActiveAlertValue3"},
                            }
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    alertId = response['data']
    return alertId

