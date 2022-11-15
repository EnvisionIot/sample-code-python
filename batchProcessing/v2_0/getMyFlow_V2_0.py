"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getMyFlow_V2_0
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Search workflows that meet the search criteria
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.0/get_my_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getMyFlow_V2_0(accessKey, secretKey, orgId, url, userId):
    accessURL = url + "/dataflow-batch-service/v2.0/flows"
    params = {"action": "getMyFlow", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getMyFlow_V2_0_searchValue(accessKey, secretKey, orgId, url, userId, searchValue):
    accessURL = url + "/dataflow-batch-service/v2.0/flows"
    params = {"action": "getMyFlow", "orgId": orgId, "userId": userId, "searchValue": searchValue}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


