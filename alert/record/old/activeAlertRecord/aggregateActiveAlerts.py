"""
 * Copyright (C), 2015-2021, Envision
 * FileName: aggregateActiveAlerts
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Calculate the number of active alerts
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/aggregate_active_alerts.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime


def aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, field):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "aggregate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"groupByField": field
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def aggregateActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, startTime=None, endTime=None):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "aggregate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"groupByField": "assetId",
          "startOccurTime": startTime,
          "endOccurTime": endTime
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "aggregate", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"groupByField": "assetId",
          "expression": expression
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)