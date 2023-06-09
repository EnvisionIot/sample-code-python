"""
 * Copyright (C), 2015-2021, Envision
 * FileName: enableFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Start the scheduling of a specified workflow
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/enable_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def enableFlow(accessKey, secretKey, orgId, url, userId, flowId):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "enable", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"flowId": flowId}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

