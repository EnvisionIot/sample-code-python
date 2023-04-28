"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAlertRule
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Search for alert rules based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/search_alert_rule.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def searchAlertRule(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"pagination": {"pageNo": 1,
                           "pageSize": 10}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertRule_modelId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"modelId": "Python_Demo_Model"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertRule_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"measurepointId": "Int_MeasurementPoint"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertRule_Expression(accessKey, secretKey, orgId, url, Expression):
    accessURL = url + '/event-service/v2.1/alert-rules'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"expression": Expression
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


