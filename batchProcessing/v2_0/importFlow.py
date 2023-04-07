"""
 * Copyright (C), 2015-2021, Envision
 * FileName: importFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    10/03/22
 * Description: Import workflow configuration to create a workflow with the specified name under the specified directory
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/import_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def importFlow(accessKey, secretKey, orgId, url, userId, flowName, description, dirId):
    accessURL = url + "/dataflow-batch-service/v2.0/flows"
    params = {"action": "import", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body= {
        "flowJson": {
            "cron": "0 0 0 * * ? *",
            "desc": "",
            "name": "flowJson_nameV2_0",
            "type": 1,
            "cycle": "D",
            "tasks": [
                {
                    "cmd": "echo \"${REPLACE}\"",
                    "cron": "",
                    "name": "Task_Node_NameV2_0",
                    "type": "COMMAND",
                    "asLink": False,
                    "timeout": 300,
                    "resource": "default",
                    "syncType": 1,
                    "submitter": "",
                    "retryLimit": 3,
                    "filePackage": "",
                    "successCode": "0",
                    "priorityLevel": 0,
                    "retryInterval": 0
                }
            ],
            "owners": "dylan.yeo",
            "syncType": 1,
            "visitors": "dylan.yeo",
            "alertMode": 3,
            "flowLinks": [],
            "relations": [],
            "startTime": "2022-01-01",
            "submitter": "db_demomanager",
            "taskLinks": [],
            "parameters": "[{\"key\":\"REPLACE\",\"value\":\"lili\"}]",
            "linkRelations": []
        },
        "dirId": dirId,
        "flowName": flowName,
        "desc": description
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

