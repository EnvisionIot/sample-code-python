"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUnformattedPolicy
 * Author:  Dylan Yeo
 * Date:    28/02/22
 * Description:  Get information of organization’s unformatted storage policy, including storage policy ID, update time and retention
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.1/get_unformatted_policy.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getUnformattedPolicy(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-policy/v2.1/policies/unformatted/detail'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body ={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)