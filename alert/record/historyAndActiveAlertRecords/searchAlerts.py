"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAlerts
 * Author:  Dylan Yeo
 * Date:    18/02/22
 * Description:  Search for active and history alerts, where the pages of the returned results do not have to be in order.
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/search_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime
from dateutil.relativedelta import relativedelta

current_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
startTime = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m-%d %H:%M:%S")

def searchAlerts(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {"startOccurTime": startTime,
           "endOccurTime": current_local,
           "pagination": {"pageNo": 1,
                          "pageSize": 5}
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlerts_instanceId(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {"startOccurTime": startTime,
           "endOccurTime": current_local,
           "instanceId": "ActiveAlert_instanceId"
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlerts_metricId(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {"startOccurTime": startTime,
           "endOccurTime": current_local,
           "metricId": "ActiveAlert_metricId"
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlerts_recoverTime(accessKey, secretKey, orgId, url):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {"startOccurTime": startTime,
           "endOccurTime": current_local,
           "startRecoverTime": startTime,
           "endRecoverTime":current_local
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlerts_active(accessKey, secretKey, orgId, url, activeStatus):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {"startOccurTime": startTime,
           "endOccurTime": current_local,
           "active": activeStatus
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlerts_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {"startOccurTime": startTime,
           "endOccurTime": current_local,
           "expression": expression
           }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)