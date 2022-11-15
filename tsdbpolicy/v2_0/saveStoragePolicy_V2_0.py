"""
 * Copyright (C), 2015-2021, Envision
 * FileName: saveStoragePolicyV2_0
 * Author:  Dylan Yeo
 * Date:    28/02/22
 * Description: Update and save the configuration of the specified storage policy, including the data storage time and models and measurement points that are configured with it
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.0/save_storage_policy.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def saveStoragePolicy_V2_0(accessKey, secretKey, orgId, url, policyId, modelId, points):
    accessURL = url + '/tsdb-policy/v2.0/policies/' + policyId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"retention": "6M",
            "models": [{"modelId": modelId,
                        "points": points}]
            }

    header = {"Content-Type": "application/json"}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
