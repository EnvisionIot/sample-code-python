"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getMyFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Search workflows that meet the search criteria
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/get_my_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getMyFlow(accessKey, secretKey, orgId, url, userId):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "getMyFlow", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getMyFlowExpression(accessKey, secretKey, orgId, url, userId, expression):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "getMyFlow", "orgId": orgId, "userId": userId, "expression": expression}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)