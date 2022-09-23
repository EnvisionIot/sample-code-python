"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAlertType
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Search for alert types based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_alert_type.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def searchAlertType(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-types/search'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"pagination": {"pageNo": 1,
                           "pageSize": 10}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchAlertType_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/event-service/v2.1/alert-types/search'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)