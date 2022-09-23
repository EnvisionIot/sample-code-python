"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAlertContent
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Search for alert content based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/search_alert_content.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def searchAlertContent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
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


def searchAlertContent_modelId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"modelId": "Python_Demo_Model"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertContent_alertTypeId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertTypeId": "Python_Type_ID"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertContent_subAlertTypeId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"subAlertTypeId": "Python_Type_ID"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertContent_Expression(accessKey, secretKey, orgId, url, Expression):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"expression": Expression
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


