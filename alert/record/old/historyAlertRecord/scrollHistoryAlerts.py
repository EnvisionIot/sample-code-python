"""
 * Copyright (C), 2015-2021, Envision
 * FileName: scrollHistoryAlerts
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description: Search for the past 3 months’ historical alerts. The first search returns a pageToken to be used for the next search, and all subsequent searches will return a different pageToken to be used for its next search
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/scroll_history_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime
from dateutil.relativedelta import relativedelta

startTime = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m-%d %H:%M:%S") # 3 months ago from current date
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def scroll_pageToken(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageSize":10}
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    pageToken = response['data']['pageToken']
    print("pageToken:", pageToken)
    return pageToken


def scrollHistoryAlerts(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_modelId(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "modelId": "Python_Demo_Model"
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_assetId(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "assetId": "AvxV8hkR"
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_measurepointsId(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "measurepointsId": "Int_MeasurementPoint"
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_recoverTime(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "recoverStartTime": "2021-12-31 12:30:00",
            "recoverEndTime": current_local,
            "scroll": {"pageToken": pageToken}
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, expression):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_RootAlert(accessKey, secretKey, orgId, url, rootAlertId, treeId=None):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "rootAlert": {"rootAlertId": rootAlertId,
                          "treeId": treeId}
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollHistoryAlerts_Scope(accessKey, secretKey, orgId, url, treeId, assetId=None, includeDerivative=False):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "scope": {"treeId": treeId,
                    "fromAssetId": assetId,
                    "includeDerivative": includeDerivative}
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
