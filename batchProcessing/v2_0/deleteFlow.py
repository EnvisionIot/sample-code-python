"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteFlow_V2_0
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Delete a specified workflow
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.0/delete_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def deleteFlow(accessKey, secretKey, orgId, url, userId, flowId):
    accessURL = url + "/dataflow-batch-service/v2.0/flows"
    params = {"action": "delete", "orgId": orgId, "userId": userId, "flowId": flowId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

