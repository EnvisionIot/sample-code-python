"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getOrganizationRoles
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Get all roles under an organization structure
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_organization_roles.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getOrganizationRoles(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/organization/role/list"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"locale": "en_US"}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)


