"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchActiveAlerts
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Search for active alerts based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/aggregate_active_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime


def searchActiveAlerts(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"pagination": {"pageNo": 1,
                           "pageSize": 5}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_modelId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": "Python_Demo_Model"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_assetId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetId": "AvxV8hkR"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"measurepointId": "Int_MeasurementPoint"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, startTime=None, endTime=None):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": endTime
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"expression": expression
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_Scope(accessKey, secretKey, orgId, url, treeId, assetId=None, includeDerivative=False):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"scope": {"treeId": treeId,
                    "fromAssetId": assetId,
                    "includeDerivative": includeDerivative}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchActiveAlerts_RootAlert(accessKey, secretKey, orgId, url, rootAlertId, treeId=None):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"rootAlert": {"rootAlertId": rootAlertId,
                        "treeId": treeId}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)