"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateAndTriggerFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    15/03/22
 * Description: Trigger workflow scheduling with updated parameters (the information of the original workflow is not changed; the updated parameters are only used to generate a workflow instance)
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/update_and_trigger_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateAndTriggerFlow(accessKey, secretKey, orgId, url, userId, flowId, triggerTime, parameters):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "updateAndTrigger", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"flowId": flowId,
            "triggerTime": triggerTime,
            "parameters": parameters}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




