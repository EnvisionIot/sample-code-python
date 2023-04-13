"""
 * Copyright (C), 2015-2021, Envision
 * FileName: saveFlow_V2_0
 * Author:  Dylan Yeo
 * Date:    15/03/22
 * Description: Save the information of the current workflow
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.0/save_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def saveFlow(accessKey, secretKey, orgId, url, userId):
    accessURL = url + "/dataflow-batch-service/v2.0/flows"
    params = {"action": "save", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"id": "13811",
            "type": 1,
            "name": "Python_SaveFlow2_0",
            "freq": "0 0 0 * * ? *",
            "cycle": "D",
            "alertMode": 3,
            "doAs": "db_demomanager",
            "owners": "dylan.yeo",
            "desc": "saveFlow_Testing2_0",
            "startTime": "2022-03-15",
            "visitors": "dylan.yeo",
            "active": 1,
            "queue": "",
            "parameters": "[]",
            "tasks": [{"taskId": "613317",
                       "nodeId": "t_613317",
                       "taskName": "SaveFlow_TaskNodeShell2_0",
                       "x": 0.0132,
                       "y": 0.008100000381469727}],
            "flows": [{"flowId": "13775",
                       "nodeId": "t_13775",
                       "flowName": "Python_FlowName2_0",
                       "isVirtual": True,
                       "x": 0.0186,
                       "y": 0.0016999999046325683}],
            "relations": [{"cycleGap": "D0",
                           "source": "t_13775",
                           "rerun": True,
                           "target": "t_613317"}]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




