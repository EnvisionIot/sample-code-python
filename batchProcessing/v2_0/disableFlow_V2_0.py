"""
 * Copyright (C), 2015-2021, Envision
 * FileName: disableFlow_V2_0
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Stop the scheduling of a specified workflow
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.0/disable_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def disableFlow_V2_0(accessKey, secretKey, orgId, url, userId, flowId):
    accessURL = url + "/dataflow-batch-service/v2.0/flows"
    params = {"action": "disable", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"flowId": flowId}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

