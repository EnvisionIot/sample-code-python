"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAlert
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description: Create an alert record
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/create_alert.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def createAlert_ActiveAlert(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertVo": {"eventType": "3",
                      "instanceId": "AvxV8hkR",  #assetId
                      "metricId": "Int_MeasurementPoint",
                      "occurTime": current_utc,
                      "recoverTime": current_utc,
                      "value": "ActiveAlert_metricvalue",
                      # Optional Parameter
                      "orgId": orgId,
                      "localOccurTime": current_local,
                      "localRecoverTime": current_local,
                      "recoverReason": "Your_Recover_Reason",
                      "severityId": "AA_newver_severityId",
                      "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                       "i18nValue": {"en_US": "AA_newver_severityDescription",
                                                     "zh_CN": "AA_newver_严重性 描述",
                                                     "ja_JP": "AA_newver_重大度説明",
                                                     "es_ES": "AA_newver_severidad Descripción"}},
                      "typeId": "AA_newver_typeId",
                      "typeDesc": {"defaultValue": "Default_AA_newver_typeDescription",
                                   "i18nValue": {"en_US": "AA_newver_typeDescription",
                                                 "zh_CN": "AA_newver_类型描述",
                                                 "ja_JP": "AA_newver_タイプの説明",
                                                 "es_ES": "AA_newver_descripción del tipo"}},
                      "parentTypeId": "AA_newver_parentTypeId",
                      "parentTypeDesc": {"defaultValue": "Default_AA_newver_parentTypeDescription",
                                         "i18nValue": {"en_US": "AA_newver_parentTypeDescription",
                                                       "zh_CN": "AA_newver_父类型描述",
                                                       "ja_JP": "AA_newver_親タイプの説明",
                                                       "es_ES": "AA_newver_descripción del tipo padre"}},
                      "contentId": "AA_newver_contentId",
                      "content": {"defaultValue": "Default_AA_newver_contentDescription",
                                  "i18nValue": {"en_US": "AA_newver_contentDescription",
                                                "zh_CN": "AA_newver_内容",
                                                "ja_JP": "AA_newver_ルールの説明",
                                                "es_ES": "AA_newver_descripción de la regla"}},
                      "ruleId": "AA_newver_ruleId",
                      "ruleDesc": {"defaultValue": "Default_AA_newver_ruleDescription",
                                   "i18nValue": {"en_US": "AA_newver_typeDescription",
                                                 "zh_CN": "AA_newver_类型描述",
                                                 "ja_JP": "AA_newver_タイプの説明",
                                                 "es_ES": "AA_newver_descripción del tipo"}},
                      "tags": {"ActiveAlert_newverKey1": "ActiveAlert_newverValue1",
                              "ActiveAlert_newverKey2": "ActiveAlert_newverValue2",
                              "ActiveAlert_newverKey3": "ActiveAlert_newverValue3"},
                      "ruleTags": {"ActiveAlertRuletagKey1": "ActiveAlertRuletagValue1",
                                  "ActiveAlertRuletagKey2": "ActiveAlertRuletagValue2",
                                  "ActiveAlertRuletagKey3": "ActiveAlertRuletagValue3"},
                      "metrictags": {"ActiveAlertMetricTagKey1": "ActiveAlertMetricTagValue1",
                                     "ActiveAlertMetricTagKey2": "ActiveAlertMetricTagValue2",
                                     "ActiveAlertMetricTagKey3": "ActiveAlertMetricTagValue3"},
                      "inhibited": True
                      }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createAlert_HistoryAlert(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertVo": {"eventType": "2",
                      "instanceId": "AvxV8hkR",  #assetId
                      "metricId": "Int_MeasurementPoint", #measurementPoint
                      "occurTime": current_utc,
                      "value": "HistoryAlert_metricvalue",
                      # Optional Parameter
                      "orgId": orgId,
                      "localOccurTime": current_local,
                      "recoverTime": current_utc,
                      "localRecoverTime": current_local,
                      "recoverReason": "Your_Recover_Reason",
                      "severityId": "HA_newver_severityId",
                      "severityDesc": {"defaultValue": "Default_Alert_severityDescription",
                                       "i18nValue": {"en_US": "HA_newver_severityDescription",
                                                     "zh_CN": "HA_newver_严重性 描述",
                                                     "ja_JP": "HA_newver_重大度説明",
                                                     "es_ES": "HA_newver_severidad Descripción"}},
                      "typeId": "HA_newver_typeId",
                      "typeDesc": {"defaultValue": "Default_HA_newver_typeDescription",
                                   "i18nValue": {"en_US": "HA_newver_typeDescription",
                                                 "zh_CN": "HA_newver_类型描述",
                                                 "ja_JP": "HA_newver_タイプの説明",
                                                 "es_ES": "HA_newver_descripción del tipo"}},
                      "parentTypeId": "HA_newver_parentTypeId",
                      "parentTypeDesc": {"defaultValue": "Default_HA_newver_parentTypeDescription",
                                         "i18nValue": {"en_US": "HA_newver_parentTypeDescription",
                                                       "zh_CN": "HA_newver_父类型描述",
                                                       "ja_JP": "HA_newver_親タイプの説明",
                                                       "es_ES": "HA_newver_descripción del tipo padre"}},
                      "contentId": "AA_newver_contentId",
                      "content": {"defaultValue": "Default_HA_newver_contentDescription",
                                  "i18nValue": {"en_US": "HA_newver_contentDescription",
                                                "zh_CN": "HA_newver_规则说明",
                                                "ja_JP": "HA_newver_ルールの説明",
                                                "es_ES": "HA_newver_descripción de la regla"}},
                      "ruleId": "HA_newver_ruleId",
                      "ruleDesc": {"defaultValue": "Default_HA_newver_ruleDescription",
                                   "i18nValue": {"en_US": "HA_newver_typeDescription",
                                                 "zh_CN": "HA_newver_类型描述",
                                                 "ja_JP": "HA_newver_タイプの説明",
                                                 "es_ES": "HA_newver_descripción del tipo"}},
                      "tags": {"HistoryAlert_newverKey1": "HistoryAlert_newverValue1",
                              "HistoryAlert_newverKey2": "HistoryAlert_newverValue2",
                              "HistoryAlert_newverKey3": "HistoryAlert_newverValue3"},
                      "ruleTags": {"HistoryAlertRuletagKey1": "HistoryAlertRuletagValue1",
                                  "HistoryAlertRuletagKey2": "HistoryAlertRuletagValue2",
                                  "HistoryAlertRuletagKey3": "HistoryAlertRuletagValue3"},
                      "metrictags": {"HistoryAlertMetricTagKey1": "HistoryAlertMetricTagValue1",
                                     "HistoryAlertMetricTagKey2": "HistoryAlertMetricTagValue2",
                                     "HistoryAlertMetricTagKey3": "HistoryAlertMetricTagValue3"},
                      "inhibited": False
                      }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

