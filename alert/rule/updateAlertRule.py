"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateAlertRule
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Update an alert rule. Any parameter (that is not null) included the request body can be updated
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/update_alert_rule.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateAlertRule_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"ruleId": "Python_Rule_ID",
          "ruleDesc": {"defaultValue": "Updated_Default_Alert_Rule_Description",
                       "i18nValue": {"en_US": "Updated_Alert_Rule_Description",
                                     "zh_CN": "更新警报规则说明",
                                     "ja_JP": "アラートルールの説明を更新",
                                     "es_ES":"Descripción De La Regla De Alerta Actualizada"}},
          "tags": {"NewRuleKey1": "NewRuleValue1",
                   "NewRuleKey2": "NewRuleValue2",
                   "NewRuleKey3": "NewRuleValue3"},
          "severityId": "Python_Severity_ID",
          "contentId": "Python_Content_ID",
          "modelId": "Python_Demo_Model",
          "measurepointId": "Int_MeasurementPoint",
          # "deviceStatus": "offline", #Alternative (Use either "measurepointId" or "deviceStatus")
          "condition": "${Int_MeasurementPoint} < 100",
          "scope": [{"treeId": "all",
                     "assetId": "all"}],
          "isEnabled": True ,
          "isRoot": False,
          "triggeringDelayTimer": 120
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def updateAlertRule_deviceStatus(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"ruleId": "Python_Rule_ID",
          "ruleDesc": {"defaultValue": "Updated_Default_Alert_Rule_Description",
                       "i18nValue": {"en_US": "Updated_Alert_Rule_Description",
                                     "zh_CN": "更新警报规则说明",
                                     "ja_JP": "アラートルールの説明を更新",
                                     "es_ES":"Descripción De La Regla De Alerta Actualizada"}},
          "tags": {"NewRuleKey1": "NewRuleValue1",
                   "NewRuleKey2": "NewRuleValue2",
                   "NewRuleKey3": "NewRuleValue3"},
          "severityId": "Python_Severity_ID",
          "contentId": "Python_Content_ID",
          "modelId": "Python_Demo_Model",
          # "measurepointId": "Int_MeasurementPoint", # Alternative (Use either "measurepointId" or "deviceStatus")
          "deviceStatus": "offline",
          "condition": "${Int_MeasurementPoint} < 100",
          "scope": [{"treeId": "all",
                     "assetId": "all"}],
          "isEnabled": True ,
          "isRoot": False,
          "triggeringDelayTimer": 120
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


