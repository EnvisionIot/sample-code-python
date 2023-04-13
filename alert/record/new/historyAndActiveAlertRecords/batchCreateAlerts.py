"""
 * Copyright (C), 2015-2021, Envision
 * FileName: batchCreateAlerts
 * Author:  Dylan Yeo
 * Date:    18/02/22
 * Description: Batch create alert records, up to 1000 items at a time
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/batch_create_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def batchCreateAlert_ActiveAlert(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertVoList": [{"eventType": "3",
                           "instanceId": "AvxV8hkR",  # assetId
                           "metricId": "Int_MeasurementPoint",
                           "occurTime": current_utc,
                           "recoverTime": current_utc,
                           "value": "ActiveAlert_metricvalue",
                           # Optional Parameter
                           "orgId": orgId,
                           "localOccurTime": current_local,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_Recover_Reason",
                           "severityId": "AA1_newver_severityId",
                           "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                            "i18nValue": {"en_US": "AA1_newver_severityDescription",
                                                          "zh_CN": "AA1_newver_严重性 描述",
                                                          "ja_JP": "AA1_newver_重大度説明",
                                                          "es_ES": "AA1_newver_severidad Descripción"}},
                           "typeId": "AA1_newver_typeId",
                           "typeDesc": {"defaultValue": "Default_AA1_newver_typeDescription",
                                        "i18nValue": {"en_US": "AA1_newver_typeDescription",
                                                      "zh_CN": "AA1_newver_类型描述",
                                                      "ja_JP": "AA1_newver_タイプの説明",
                                                      "es_ES": "AA1_newver_descripción del tipo"}},
                           "parentTypeId": "AA1_newver_parentTypeId",
                           "parentTypeDesc": {"defaultValue": "Default_AA1_newver_parentTypeDescription",
                                              "i18nValue": {"en_US": "AA1_newver_parentTypeDescription",
                                                            "zh_CN": "AA1_newver_父类型描述",
                                                            "ja_JP": "AA1_newver_親タイプの説明",
                                                            "es_ES": "AA1_newver_descripción del tipo padre"}},
                           "contentId": "AA1_newver_contentId",
                           "content": {"defaultValue": "Default_AA1_newver_contentDescription",
                                       "i18nValue": {"en_US": "AA1_newver_contentDescription",
                                                     "zh_CN": "AA1_newver_内容",
                                                     "ja_JP": "AA1_newver_ルールの説明",
                                                     "es_ES": "AA1_newver_descripción de la regla"}},
                           "ruleId": "AA1_newver_ruleId",
                           "ruleDesc": {"defaultValue": "Default_AA1_newver_ruleDescription",
                                        "i18nValue": {"en_US": "AA1_newver_typeDescription",
                                                      "zh_CN": "AA1_newver_类型描述",
                                                      "ja_JP": "AA1_newver_タイプの説明",
                                                      "es_ES": "AA1_newver_descripción del tipo"}},
                           "tags": {"ActiveAlert1_newverKey1": "ActiveAlert1_newverValue1",
                                    "ActiveAlert1_newverKey2": "ActiveAlert1_newverValue2",
                                    "ActiveAlert1_newverKey3": "ActiveAlert1_newverValue3"},
                           "ruleTags": {"ActiveAlert1RuletagKey1": "ActiveAlert1RuletagValue1",
                                        "ActiveAlert1RuletagKey2": "ActiveAlert1RuletagValue2",
                                        "ActiveAlert1RuletagKey3": "ActiveAlert1RuletagValue3"},
                           "metrictags": {"ActiveAlert1MetricTagKey1": "ActiveAlert1MetricTagValue1",
                                          "ActiveAlert1MetricTagKey2": "ActiveAlert1MetricTagValue2",
                                          "ActiveAlert1MetricTagKey3": "ActiveAlert1MetricTagValue3"},
                           "inhibited": False
                           },
                          {"eventType": "3",
                           "instanceId": "AvxV8hkR",  # assetId
                           "metricId": "Int_MeasurementPoint",
                           "occurTime": current_utc,
                           "recoverTime": current_utc,
                           "value": "ActiveAlert_metricvalue",
                           # Optional Parameter
                           "orgId": orgId,
                           "localOccurTime": current_local,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_Recover_Reason",
                           "severityId": "AA2_newver_severityId",
                           "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                            "i18nValue": {"en_US": "AA2_newver_severityDescription",
                                                          "zh_CN": "AA2_newver_严重性 描述",
                                                          "ja_JP": "AA2_newver_重大度説明",
                                                          "es_ES": "AA2_newver_severidad Descripción"}},
                           "typeId": "AA2_newver_typeId",
                           "typeDesc": {"defaultValue": "Default_AA2_newver_typeDescription",
                                        "i18nValue": {"en_US": "AA2_newver_typeDescription",
                                                      "zh_CN": "AA2_newver_类型描述",
                                                      "ja_JP": "AA2_newver_タイプの説明",
                                                      "es_ES": "AA2_newver_descripción del tipo"}},
                           "parentTypeId": "AA2_newver_parentTypeId",
                           "parentTypeDesc": {"defaultValue": "Default_AA2_newver_parentTypeDescription",
                                              "i18nValue": {"en_US": "AA2_newver_parentTypeDescription",
                                                            "zh_CN": "AA2_newver_父类型描述",
                                                            "ja_JP": "AA2_newver_親タイプの説明",
                                                            "es_ES": "AA2_newver_descripción del tipo padre"}},
                           "contentId": "AA2_newver_contentId",
                           "content": {"defaultValue": "Default_AA2_newver_contentDescription",
                                       "i18nValue": {"en_US": "AA2_newver_contentDescription",
                                                     "zh_CN": "AA2_newver_内容",
                                                     "ja_JP": "AA2_newver_ルールの説明",
                                                     "es_ES": "AA2_newver_descripción de la regla"}},
                           "ruleId": "AA2_newver_ruleId",
                           "ruleDesc": {"defaultValue": "Default_AA2_newver_ruleDescription",
                                        "i18nValue": {"en_US": "AA2_newver_typeDescription",
                                                      "zh_CN": "AA2_newver_类型描述",
                                                      "ja_JP": "AA2_newver_タイプの説明",
                                                      "es_ES": "AA2_newver_descripción del tipo"}},
                           "tags": {"ActiveAlert2_newverKey1": "ActiveAlert2_newverValue1",
                                    "ActiveAlert2_newverKey2": "ActiveAlert2_newverValue2",
                                    "ActiveAlert2_newverKey3": "ActiveAlert2_newverValue3"},
                           "ruleTags": {"ActiveAlert2RuletagKey1": "ActiveAlert2RuletagValue1",
                                        "ActiveAlert2RuletagKey2": "ActiveAlert2RuletagValue2",
                                        "ActiveAlert2RuletagKey3": "ActiveAlert2RuletagValue3"},
                           "metrictags": {"ActiveAlert2MetricTagKey1": "ActiveAlert2MetricTagValue1",
                                          "ActiveAlert2MetricTagKey2": "ActiveAlert2MetricTagValue2",
                                          "ActiveAlert2MetricTagKey3": "ActiveAlert2MetricTagValue3"},
                           "inhibited": False
                           }]
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def batchCreateAlert_HistoryAlert(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertVoList": [{"eventType": "2",
                           "instanceId": "AvxV8hkR",  # assetId
                           "metricId": "Int_MeasurementPoint",  # measurementPoint
                           "occurTime": current_utc,
                           "value": "HistoryAlert_metricvalue",
                           # Optional Parameter
                           "orgId": orgId,
                           "localOccurTime": current_local,
                           "recoverTime": current_utc,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_Recover_Reason",
                           "severityId": "HA1_newver_severityId",
                           "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                            "i18nValue": {"en_US": "HA1_newver_severityDescription",
                                                          "zh_CN": "HA1_newver_严重性 描述",
                                                          "ja_JP": "HA1_newver_重大度説明",
                                                          "es_ES": "HA1_newver_severidad Descripción"}},
                           "typeId": "HA1_newver_typeId",
                           "typeDesc": {"defaultValue": "Default_HA1_newver_typeDescription",
                                        "i18nValue": {"en_US": "HA1_newver_typeDescription",
                                                      "zh_CN": "HA1_newver_类型描述",
                                                      "ja_JP": "HA1_newver_タイプの説明",
                                                      "es_ES": "HA1_newver_descripción del tipo"}},
                           "parentTypeId": "HA1_newver_parentTypeId",
                           "parentTypeDesc": {"defaultValue": "Default_HA1_newver_parentTypeDescription",
                                              "i18nValue": {"en_US": "HA1_newver_parentTypeDescription",
                                                            "zh_CN": "HA1_newver_父类型描述",
                                                            "ja_JP": "HA1_newver_親タイプの説明",
                                                            "es_ES": "HA1_newver_descripción del tipo padre"}},
                           "contentId": "AA_newver_contentId",
                           "content": {"defaultValue": "Default_HA1_newver_contentDescription",
                                       "i18nValue": {"en_US": "HA1_newver_contentDescription",
                                                     "zh_CN": "HA1_newver_规则说明",
                                                     "ja_JP": "HA1_newver_ルールの説明",
                                                     "es_ES": "HA1_newver_descripción de la regla"}},
                           "ruleId": "HA1_newver_ruleId",
                           "ruleDesc": {"defaultValue": "Default_HA1_newver_ruleDescription",
                                        "i18nValue": {"en_US": "HA1_newver_typeDescription",
                                                      "zh_CN": "HA1_newver_类型描述",
                                                      "ja_JP": "HA1_newver_タイプの説明",
                                                      "es_ES": "HA1_newver_descripción del tipo"}},
                           "tags": {"HistoryAlert1_newverKey1": "HistoryAlert1_newverValue1",
                                    "HistoryAlert1_newverKey2": "HistoryAlert1_newverValue2",
                                    "HistoryAlert1_newverKey3": "HistoryAlert1_newverValue3"},
                           "ruleTags": {"HistoryAlert1RuletagKey1": "HistoryAlert1RuletagValue1",
                                        "HistoryAlert1RuletagKey2": "HistoryAlert1RuletagValue2",
                                        "HistoryAlert1RuletagKey3": "HistoryAlert1RuletagValue3"},
                           "metrictags": {"HistoryAlert1MetricTagKey1": "HistoryAlert1MetricTagValue1",
                                          "HistoryAlert1MetricTagKey2": "HistoryAlert1MetricTagValue2",
                                          "HistoryAlert1MetricTagKey3": "HistoryAlert1MetricTagValue3"},
                           "inhibited": False
                           },
                          {"eventType": "2",
                           "instanceId": "AvxV8hkR",  # assetId
                           "metricId": "Int_MeasurementPoint",  # measurementPoint
                           "occurTime": current_utc,
                           "value": "HistoryAlert_metricvalue",
                           # Optional Parameter
                           "orgId": orgId,
                           "localOccurTime": current_local,
                           "recoverTime": current_utc,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_Recover_Reason",
                           "severityId": "HA2_newver_severityId",
                           "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                            "i18nValue": {"en_US": "HA2_newver_severityDescription",
                                                          "zh_CN": "HA2_newver_严重性 描述",
                                                          "ja_JP": "HA2_newver_重大度説明",
                                                          "es_ES": "HA2_newver_severidad Descripción"}},
                           "typeId": "HA2_newver_typeId",
                           "typeDesc": {"defaultValue": "Default_HA2_newver_typeDescription",
                                        "i18nValue": {"en_US": "HA2_newver_typeDescription",
                                                      "zh_CN": "HA2_newver_类型描述",
                                                      "ja_JP": "HA2_newver_タイプの説明",
                                                      "es_ES": "HA2_newver_descripción del tipo"}},
                           "parentTypeId": "HA2_newver_parentTypeId",
                           "parentTypeDesc": {"defaultValue": "Default_HA2_newver_parentTypeDescription",
                                              "i18nValue": {"en_US": "HA2_newver_parentTypeDescription",
                                                            "zh_CN": "HA2_newver_父类型描述",
                                                            "ja_JP": "HA2_newver_親タイプの説明",
                                                            "es_ES": "HA2_newver_descripción del tipo padre"}},
                           "contentId": "AA_newver_contentId",
                           "content": {"defaultValue": "Default_HA2_newver_contentDescription",
                                       "i18nValue": {"en_US": "HA2_newver_contentDescription",
                                                     "zh_CN": "HA2_newver_规则说明",
                                                     "ja_JP": "HA2_newver_ルールの説明",
                                                     "es_ES": "HA2_newver_descripción de la regla"}},
                           "ruleId": "HA2_newver_ruleId",
                           "ruleDesc": {"defaultValue": "Default_HA2_newver_ruleDescription",
                                        "i18nValue": {"en_US": "HA2_newver_typeDescription",
                                                      "zh_CN": "HA2_newver_类型描述",
                                                      "ja_JP": "HA2_newver_タイプの説明",
                                                      "es_ES": "HA2_newver_descripción del tipo"}},
                           "tags": {"HistoryAlert2_newverKey1": "HistoryAlert2_newverValue1",
                                    "HistoryAlert2_newverKey2": "HistoryAlert2_newverValue2",
                                    "HistoryAlert2_newverKey3": "HistoryAlert2_newverValue3"},
                           "ruleTags": {"HistoryAlert2RuletagKey1": "HistoryAlert2RuletagValue1",
                                        "HistoryAlert2RuletagKey2": "HistoryAlert2RuletagValue2",
                                        "HistoryAlert2RuletagKey3": "HistoryAlert2RuletagValue3"},
                           "metrictags": {"HistoryAlert2MetricTagKey1": "HistoryAlert2MetricTagValue1",
                                          "HistoryAlert2MetricTagKey2": "HistoryAlert2MetricTagValue2",
                                          "HistoryAlert2MetricTagKey3": "HistoryAlert2MetricTagValue3"},
                           "inhibited": False
                           }]
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def batchCreateAlert_mix(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "batchCreate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertVoList": [{"eventType": "3",
                           "instanceId": "AvxV8hkR",  # assetId
                           "metricId": "Int_MeasurementPoint",
                           "occurTime": current_utc,
                           "recoverTime": current_utc,
                           "value": "ActiveAlert_metricvalue",
                           # Optional Parameter
                           "orgId": orgId,
                           "localOccurTime": current_local,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_Recover_Reason",
                           "severityId": "AA3_newver_severityId",
                           "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                            "i18nValue": {"en_US": "AA3_newver_severityDescription",
                                                          "zh_CN": "AA3_newver_严重性 描述",
                                                          "ja_JP": "AA3_newver_重大度説明",
                                                          "es_ES": "AA3_newver_severidad Descripción"}},
                           "typeId": "AA3_newver_typeId",
                           "typeDesc": {"defaultValue": "Default_AA3_newver_typeDescription",
                                        "i18nValue": {"en_US": "AA3_newver_typeDescription",
                                                      "zh_CN": "AA3_newver_类型描述",
                                                      "ja_JP": "AA3_newver_タイプの説明",
                                                      "es_ES": "AA3_newver_descripción del tipo"}},
                           "parentTypeId": "AA3_newver_parentTypeId",
                           "parentTypeDesc": {"defaultValue": "Default_AA3_newver_parentTypeDescription",
                                              "i18nValue": {"en_US": "AA3_newver_parentTypeDescription",
                                                            "zh_CN": "AA3_newver_父类型描述",
                                                            "ja_JP": "AA3_newver_親タイプの説明",
                                                            "es_ES": "AA3_newver_descripción del tipo padre"}},
                           "contentId": "AA3_newver_contentId",
                           "content": {"defaultValue": "Default_AA3_newver_contentDescription",
                                       "i18nValue": {"en_US": "AA3_newver_contentDescription",
                                                     "zh_CN": "AA3_newver_内容",
                                                     "ja_JP": "AA3_newver_ルールの説明",
                                                     "es_ES": "AA3_newver_descripción de la regla"}},
                           "ruleId": "AA3_newver_ruleId",
                           "ruleDesc": {"defaultValue": "Default_AA3_newver_ruleDescription",
                                        "i18nValue": {"en_US": "AA3_newver_typeDescription",
                                                      "zh_CN": "AA3_newver_类型描述",
                                                      "ja_JP": "AA3_newver_タイプの説明",
                                                      "es_ES": "AA3_newver_descripción del tipo"}},
                           "tags": {"ActiveAlert3_newverKey1": "ActiveAlert3_newverValue1",
                                    "ActiveAlert3_newverKey2": "ActiveAlert3_newverValue2",
                                    "ActiveAlert3_newverKey3": "ActiveAlert3_newverValue3"},
                           "ruleTags": {"ActiveAlert3RuletagKey1": "ActiveAlert3RuletagValue1",
                                        "ActiveAlert3RuletagKey2": "ActiveAlert3RuletagValue2",
                                        "ActiveAlert3RuletagKey3": "ActiveAlert3RuletagValue3"},
                           "metrictags": {"ActiveAlert3MetricTagKey1": "ActiveAlert3MetricTagValue1",
                                          "ActiveAlert3MetricTagKey2": "ActiveAlert3MetricTagValue2",
                                          "ActiveAlert3MetricTagKey3": "ActiveAlert3MetricTagValue3"},
                           "inhibited": False
                           },
                          {"eventType": "2",
                           "instanceId": "AvxV8hkR",  # assetId
                           "metricId": "Int_MeasurementPoint",  # measurementPoint
                           "occurTime": current_utc,
                           "value": "HistoryAlert_metricvalue",
                           # Optional Parameter
                           "orgId": orgId,
                           "localOccurTime": current_local,
                           "recoverTime": current_utc,
                           "localRecoverTime": current_local,
                           "recoverReason": "Your_Recover_Reason",
                           "severityId": "HA3_newver_severityId",
                           "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                            "i18nValue": {"en_US": "HA3_newver_severityDescription",
                                                          "zh_CN": "HA3_newver_严重性 描述",
                                                          "ja_JP": "HA3_newver_重大度説明",
                                                          "es_ES": "HA3_newver_severidad Descripción"}},
                           "typeId": "HA3_newver_typeId",
                           "typeDesc": {"defaultValue": "Default_HA3_newver_typeDescription",
                                        "i18nValue": {"en_US": "HA3_newver_typeDescription",
                                                      "zh_CN": "HA3_newver_类型描述",
                                                      "ja_JP": "HA3_newver_タイプの説明",
                                                      "es_ES": "HA3_newver_descripción del tipo"}},
                           "parentTypeId": "HA3_newver_parentTypeId",
                           "parentTypeDesc": {"defaultValue": "Default_HA3_newver_parentTypeDescription",
                                              "i18nValue": {"en_US": "HA3_newver_parentTypeDescription",
                                                            "zh_CN": "HA3_newver_父类型描述",
                                                            "ja_JP": "HA3_newver_親タイプの説明",
                                                            "es_ES": "HA3_newver_descripción del tipo padre"}},
                           "contentId": "AA_newver_contentId",
                           "content": {"defaultValue": "Default_HA3_newver_contentDescription",
                                       "i18nValue": {"en_US": "HA3_newver_contentDescription",
                                                     "zh_CN": "HA3_newver_规则说明",
                                                     "ja_JP": "HA3_newver_ルールの説明",
                                                     "es_ES": "HA3_newver_descripción de la regla"}},
                           "ruleId": "HA3_newver_ruleId",
                           "ruleDesc": {"defaultValue": "Default_HA3_newver_ruleDescription",
                                        "i18nValue": {"en_US": "HA3_newver_typeDescription",
                                                      "zh_CN": "HA3_newver_类型描述",
                                                      "ja_JP": "HA3_newver_タイプの説明",
                                                      "es_ES": "HA3_newver_descripción del tipo"}},
                           "tags": {"HistoryAlert3_newverKey1": "HistoryAlert3_newverValue1",
                                    "HistoryAlert3_newverKey2": "HistoryAlert3_newverValue2",
                                    "HistoryAlert3_newverKey3": "HistoryAlert3_newverValue3"},
                           "ruleTags": {"HistoryAlert3RuletagKey1": "HistoryAlert3RuletagValue1",
                                        "HistoryAlert3RuletagKey2": "HistoryAlert3RuletagValue2",
                                        "HistoryAlert3RuletagKey3": "HistoryAlert3RuletagValue3"},
                           "metrictags": {"HistoryAlert3MetricTagKey1": "HistoryAlert3MetricTagValue1",
                                          "HistoryAlert3MetricTagKey2": "HistoryAlert3MetricTagValue2",
                                          "HistoryAlert3MetricTagKey3": "HistoryAlert3MetricTagValue3"},
                           "inhibited": False
                           }]
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)