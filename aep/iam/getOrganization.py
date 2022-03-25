"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getOrganization
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: Get the organization’s information
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/iam-api/en/2.3.0/get_org.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getOrganization(accessKey, secretKey, orgId, url, sessoinId):
    accessURL = url + "/enos-iam-service/v2.0/organization/info"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": sessoinId}
    print(header)

    body = {"id": orgId}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)