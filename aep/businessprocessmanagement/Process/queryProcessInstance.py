"""
 * Copyright (C), 2015-2021, Envision
 * FileName: queryProcessInstance
 * Author:  Dylan Yeo
 * Date:    22/03/22
 * Description: Query the list of process instances
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/query_process_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
import time

current_time = round(time.time()*1000)

def queryProcessInstance(accessKey, secretKey, url, accessToken):
    accessURL = url + "/enos-bpm-service/v2.0/work/process-instances/queryList"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"processStatus": "inProgress",
            # Optional Parameters
            "processName": "Python_ProcessInstance",
            # "processInstanceId": "54366b8f-ab3d-11ec-8df5-120e04f331d8",
            # "startedBefore": current_time,
            # "startedAfter": "1647302400000",
            # "startBy": "u16473063753681521",
            "pagination":  {"current": 0,
                            "pageSize": 5,
                            "sorts": [{"field": "createdTime",
                                       "order": "ASC"}]
                                       }
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
