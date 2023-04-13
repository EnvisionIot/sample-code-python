"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listFlowInstances_V2_1
 * Author:  Dylan Yeo
 * Date:    10/03/22
 * Description: Search workflow instances that meet the search criteria
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/list_flow_instances.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
import time

current_Time = round(time.time()*1000)

def listFlowInstances_V2_1(accessKey, secretKey, orgId, url, userId, schedule_type, owner, fromTriggerTime, toTriggerTime, status):
    accessURL = url + "/batch-processing-service/v2.1/flowInstances"
    params = {"action": "search", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"type": schedule_type,
            "owner": owner,
            "fromTriggerTime": fromTriggerTime,
            "toTriggerTime": toTriggerTime,
            "status": status,
            "pagination": {
                "pageNo": 1,
                "pageSize": 10,
                "sorters": [{
                    "field": "start_time",
                    "order": "DESC"
                }]}
            }
    # print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def listFlowInstances_V2_1_expression(accessKey, secretKey, orgId, url, userId, expression):
    accessURL = url + "/batch-processing-service/v2.1/flowInstances"
    params = {"action": "search", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"type": 1,
            "expression": expression,
            "owner": "dylan.yeo",
            "fromTriggerTime": "1640995200000",
            "toTriggerTime": current_Time,
            "status": "-1,0,1,2,3,4,5,6,7,8,9,10",
            "pagination": {
                "pageNo": 1,
                "pageSize": 10,
                "sorters": [{
                    "field": "start_time",
                    "order": "ASC"
                }]}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def listFlowInstances_V2_1_pagination(accessKey, secretKey, orgId, url, userId, pagination):
    accessURL = url + "/batch-processing-service/v2.1/flowInstances"
    params = {"action": "search", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"type": 1,
            "owner": "dylan.yeo",
            "fromTriggerTime": "1640995200000",
            "toTriggerTime": current_Time,
            "status": "-1,0,1,2,3,4,5,6,7,8,9,10",
            "pagination": pagination
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
