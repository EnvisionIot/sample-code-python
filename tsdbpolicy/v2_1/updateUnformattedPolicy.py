"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateUnformattedPolicy
 * Author:  Dylan Yeo
 * Date:    28/02/22
 * Description:  Update the data storage time of organization’s unformatted storage policy
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.1/get_unformatted_policy.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateUnformattedPolicy(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-policy/v2.1/policies/unformatted/update'
    params = {"orgId": orgId, "retention": "6M"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body ={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)