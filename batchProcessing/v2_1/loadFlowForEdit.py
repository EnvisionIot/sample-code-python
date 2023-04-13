"""
 * Copyright (C), 2015-2021, Envision
 * FileName: loadFlowForEdit_V2_1
 * Author:  Dylan Yeo
 * Date:    14/03/22
 * Description: Load the specified workflow to a temporary workflow to get the workflow information
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/load_flow_for_edit.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def loadFlowForEdit(accessKey, secretKey, orgId, url, userId, flowId):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "loadForEdit", "orgId": orgId, "userId": userId, "flowId": flowId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

