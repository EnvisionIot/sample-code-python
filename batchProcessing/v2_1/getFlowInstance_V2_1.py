"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getFlowInstance_V2_1
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Get the information of a specified workflow instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/get_flow_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getFlowInstance_V2_1(accessKey, secretKey, orgId, url, userId, flowInstId):
    accessURL = url + "/batch-processing-service/v2.1/flowInstances"
    params = {"action": "get", "orgId": orgId, "userId": userId, "flowInstId": flowInstId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

