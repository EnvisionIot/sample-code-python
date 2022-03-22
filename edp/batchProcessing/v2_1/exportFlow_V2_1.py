"""
 * Copyright (C), 2015-2021, Envision
 * FileName: exportFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Export a workflow configuration
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/export_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def exportFlow_V2_1(accessKey, secretKey, orgId, url, userId, flowId):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "export", "orgId": orgId, "userId": userId, "flowId": flowId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

