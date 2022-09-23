"""
 * Copyright (C), 2015-2021, Envision
 * FileName: scrollAlerts
 * Author:  Dylan Yeo
 * Date:    18/02/22
 * Description: Search for active and history alerts. The first search returns a pageToken to be used for the next search, and all subsequent searches will return a different pageToken to be used for its next search.
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/scroll_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime
from dateutil.relativedelta import relativedelta

startTime = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m-%d %H:%M:%S") # 94 days from current date
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def scroll_pageToken(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
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


def scrollAlerts(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/alert-service/v2.1/alerts'
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


def scrollAlerts_instanceId(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "instanceId": "AvxV8hkR"
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollAlerts_metricId(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "metricId": "Int_MeasurementPoint",
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollAlerts_recoverTime(accessKey, secretKey, orgId, url):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "startRecoverTime": startTime,
            "endRecoverTime": current_local,
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollAlerts_active(accessKey, secretKey, orgId, url, activeStatus):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "active": activeStatus
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def scrollAlerts_Expression(accessKey, secretKey, orgId, url, expression):
    pageToken = scroll_pageToken(accessKey, secretKey, orgId, url)
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "scroll", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= { "startOccurTime": startTime,
            "endOccurTime": current_local,
            "scroll": {"pageToken": pageToken},
            "expression": expression
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

