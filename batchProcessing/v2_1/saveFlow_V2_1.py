"""
 * Copyright (C), 2015-2021, Envision
 * FileName: saveFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    15/03/22
 * Description: Save the information of the current workflow
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/trigger_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def saveFlow_V2_1(accessKey, secretKey, orgId, url, userId):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "save", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"id": "13810",
            "type": 1,
            "name": "Python_SaveFlow2_1",
            "freq": "0 0 0 * * ? *",
            "cycle": "D",
            "alertMode": 3,
            "doAs": "db_demomanager",
            "owners": "dylan.yeo",
            "desc": "saveFlow_Testing2_1",
            "startTime": "2022-03-15",
            "visitors": "dylan.yeo",
            "active": 1,
            "queue": "",
            "parameters": "[]",
            "tasks": [{"taskId": "613318",
                       "nodeId": "t_613318",
                       "taskName": "SaveFlow_TaskNodeShell2_1",
                       "x": 0.0132,
                       "y": 0.008100000381469727}],
            "flows": [{"flowId": "13774",
                       "nodeId": "t_13774",
                       "flowName": "Python_FlowName2_1",
                       "isVirtual": True,
                       "x": 0.0186,
                       "y": 0.0016999999046325683}],
            "relations": [{"cycleGap": "D0",
                           "source": "t_13774",
                           "rerun": True,
                           "target": "t_613318"}]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




