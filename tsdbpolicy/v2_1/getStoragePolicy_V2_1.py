"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getStoragePolicyV2_1
 * Author:  Dylan Yeo
 * Date:    28/02/22
 * Description: Get the detailed information of the specified storage policy with the storage policy ID, including the storage policy name, stored data type, storage time, and models and measurement points (with data compression configuration) that are configured with the storage policy
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.1/get_storage_policy.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getStoragePolicy_V2_1(accessKey, secretKey, orgId, url, policyId):
    accessURL = url + '/tsdb-policy/v2.1/policies/' + policyId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)