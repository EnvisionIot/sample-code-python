"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAlertRule
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Create an alert rule
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_alert_rule.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createAlertRule(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"ruleId": "Python_Rule_ID",
          "ruleDesc": {"defaultValue": "Default_Alert_Rule_Description",
                       "i18nValue": {"en_US": "Alert_Rule_Description",
                                     "zh_CN": "警报规则说明",
                                     "ja_JP": "アラートルールの説明",
                                     "es_ES":"Descripción De La Regla De Alerta"}},
          "tags": {"RuleKey1": "RuleValue1",
                   "RuleKey2": "RuleValue2",
                   "RuleKey3": "RuleValue3"},
          "severityId": "Python_Severity_ID",
          "contentId": "Python_Content_ID",
          "modelId": "Python_Demo_Model",
          "measurepointId": "Int_MeasurementPoint",
          # "deviceStatus": "offline", # Alternative (Use either "measurepointId" or "deviceStatus")
          "condition": "${Int_MeasurementPoint} < 100",
          "scope": [{"treeId": "all",
                     "assetId": "all"}],
          "isEnabled": True,
          "isRoot": False,
          "triggeringDelayTimer": 120
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createAlertRule_measurepointIdCondition(accessKey, secretKey, orgId, url, ruleId, measurepointId, condition):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"ruleId": ruleId,
          "ruleDesc": {"defaultValue": "Default_Alert_Rule_Description",
                       "i18nValue": {"en_US": "Alert_Rule_Description",
                                     "zh_CN": "警报规则说明",
                                     "ja_JP": "アラートルールの説明",
                                     "es_ES":"Descripción De La Regla De Alerta"}},
          "tags": {"RuleKey1": "RuleValue1",
                   "RuleKey2": "RuleValue2",
                   "RuleKey3": "RuleValue3"},
          "severityId": "Python_Severity_ID",
          "contentId": "Python_Content_ID",
          "modelId": "Python_Demo_Model",
          "measurepointId": measurepointId,
          "condition": condition,
          "scope": [{"treeId": "all",
                     "assetId": "all"}],
          "isEnabled": True,
          "isRoot": False,
          "triggeringDelayTimer": 120
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createAlertRule_deviceStatusCondition(accessKey, secretKey, orgId, url, ruleId, condition):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"ruleId": ruleId,
          "ruleDesc": {"defaultValue": "Default_Alert_Rule_Description",
                       "i18nValue": {"en_US": "Alert_Rule_Description",
                                     "zh_CN": "警报规则说明",
                                     "ja_JP": "アラートルールの説明",
                                     "es_ES":"Descripción De La Regla De Alerta"}},
          "tags": {"RuleKey1": "RuleValue1",
                   "RuleKey2": "RuleValue2",
                   "RuleKey3": "RuleValue3"},
          "severityId": "Python_Severity_ID",
          "contentId": "Python_Content_ID",
          "modelId": "Python_Demo_Model",
          "deviceStatus": "offline",
          "condition": condition,
          "scope": [{"treeId": "all",
                     "assetId": "all"}],
          "isEnabled": True,
          "isRoot": False,
          "triggeringDelayTimer": 120
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createAlertRule_scope(accessKey, secretKey, orgId, url, ruleId, treeId, assetId):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"ruleId": ruleId,
          "ruleDesc": {"defaultValue": "Default_Alert_Rule_Description",
                       "i18nValue": {"en_US": "Alert_Rule_Description",
                                     "zh_CN": "警报规则说明",
                                     "ja_JP": "アラートルールの説明",
                                     "es_ES":"Descripción De La Regla De Alerta"}},
          "tags": {"RuleKey1": "RuleValue1",
                   "RuleKey2": "RuleValue2",
                   "RuleKey3": "RuleValue3"},
          "severityId": "Python_Severity_ID",
          "contentId": "Python_Content_ID",
          "modelId": "Python_Demo_Model",
          "measurepointId": "Int_MeasurementPoint",
          # "deviceStatus": "offline", # Alternative (Use either "measurepointId" or "deviceStatus")
          "condition": "${Int_MeasurementPoint} < 100",
          "scope": [{"treeId": treeId,
                     "assetId": assetId}],
          "isEnabled": True,
          "isRoot": False,
          "triggeringDelayTimer": 120
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
