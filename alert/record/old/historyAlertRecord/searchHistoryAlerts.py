"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchHistoryAlert
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description: Search for the past 3 months’ historical alerts
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/search_history_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime
from dateutil.relativedelta import relativedelta

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
startTime = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m-%d %H:%M:%S")

def searchHistoryAlerts(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "pagination": {"pageNo": 1,
                         "pageSize": 5}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_modelId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "modelId": "Python_Demo_Model"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_assetId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "assetId": "AvxV8hkR"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_measurepointId(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "measurepointId": "Int_MeasurementPoint"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_recoverTime(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "recoverStartTime": "2021-12-31 12:30:00",
          "recoverEndTime": current_local
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "expression": expression
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_Scope(accessKey, secretKey, orgId, url, treeId, assetId=None, includeDerivative=False):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "scope": {"treeId": treeId,
                    "fromAssetId": assetId,
                    "includeDerivative": includeDerivative}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchHistoryAlerts_RootAlert(accessKey, secretKey, orgId, url, rootAlertId, treeId=None):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"startOccurTime": startTime,
          "endOccurTime": current_local,
          "rootAlert": {"rootAlertId": rootAlertId,
                        "treeId": treeId}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)