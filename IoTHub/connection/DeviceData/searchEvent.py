"""
 * Copyright (C), 2015-2021, Envision
 * FileName: SearchEvent
 * Author:  Dylan Yeo
 * Date:    26/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_event.html
 * refer to the resources/ConnectServiceModel/DeviceData/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 26/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def SearchEvent(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "pagination": {"pageNo": 1,
                       "pageSize": 25},
        "resolveName": True
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_productKey(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"productKey": productKey
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_deviceKey(accessKey, secretKey, orgId, url, deviceKey):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"deviceKey": deviceKey
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetId": assetId
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_tslEventKey(accessKey, secretKey, orgId, url, EventKey):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"tslEventKey": EventKey
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_tslEventType(accessKey, secretKey, orgId, url, EventType):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"tslEventType": EventType
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_startTime(accessKey, secretKey, orgId, url, startTime):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"startTime": startTime
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_endTime(accessKey, secretKey, orgId, url, endTime):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"endTime": endTime
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchEvent_expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "productKey = '4kZqiPoC'"
    # expression = "productKey in ('4kZqiPoC')"
    # expression = "deviceKey = 'RqMa4xiwqo'"
    # expression = "deviceKey in ('RqMa4xiwqo')"
    # expression = "assetId ='G5M8Ojhd'"
    # expression = "assetId in ('G5M8Ojhd')"
    # expression = "tslEventKey = 'Event1'"
    # expression = "tslEventKey in ('Event1')"
    # expression = "tslEventType = 'INFO'"
    # expression = "tslEventType in ('INFO')"
    # expression = "productKey = '4kZqiPoC' and deviceKey = 'RqMa4xiwqo'"
    # expression = "tslEventKey = 'Event1' or tslEventType = 'WARNING'"

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)