"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteAlertRule
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Delete an alert rule
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/delete_alert_rule.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def deleteAlertRule(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "delete", "orgId": orgId, "ruleId": "Python_Rule_ID"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def deleteAlertRule_ruleId(accessKey, secretKey, orgId, url, ruleId):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "delete", "orgId": orgId, "ruleId": ruleId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


