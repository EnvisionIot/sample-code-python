"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAlertSeverity
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Search for alert severity based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/search_alert_severity.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def searchAlertSeverity(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-severities'
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


def searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/event-service/v2.1/alert-severities'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


