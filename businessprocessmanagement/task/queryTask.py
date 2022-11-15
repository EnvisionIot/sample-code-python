"""
 * Copyright (C), 2015-2021, Envision
 * FileName: queryTask
 * Author:  Dylan Yeo
 * Date:    23/03/22
 * Description: Query the list of tasks
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/task/query_task.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def queryTask(accessKey, secretKey, url, accessToken):
    accessURL = url + "/enos-bpm-service/v2.0/work/tasks/query"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"taskStatus": "inProgress",
            #optional parameters
            # "processInstanceId": "54366b8f-ab3d-11ec-8df5-120e04f331d8",
            # "processName": "Python_ProcessInstance",
            # "taskName": "Python Task 1",
            "pagination": {"current": 0,
                           "pageSize": 5,
                           # "sorts": [{"field": "createdTime",
                           #            "order": "DESC"}]
                           }
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
