"""
 * Copyright (C), 2015-2021, Envision
 * FileName: triggerFlowFromTask_V2_1
 * Author:  Dylan Yeo
 * Date:    14/03/22
 * Description: Manually trigger a workflow schedule (run a specified task and its downstream nodes only)
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/trigger_flow_from_task.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def triggerFlowFromTask_V2_1(accessKey, secretKey, orgId, url, userId, flowId, taskId, triggerTime):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "triggerFromTask", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"flowId": flowId,
            "taskId": taskId,
            "triggerTime": triggerTime
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




