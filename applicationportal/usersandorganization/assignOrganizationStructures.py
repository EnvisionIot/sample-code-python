"""
 * Copyright (C), 2015-2021, Envision
 * FileName: assignOrganizationStructures
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Assign an organization structure to the user without logging in to Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/assign_org_structures.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def assignOrganizationStructures(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/structure/appendStructures"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "userId": "u16473063753681521",
            "structureIds": ["sg16000557456141", "sg16256613934031600"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
