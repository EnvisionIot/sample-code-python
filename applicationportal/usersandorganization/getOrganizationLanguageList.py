"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getOrganizationLanguageList
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Get the list of languages available for an organization
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_organization_lang_list.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getOrganizationLanguageList(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/organization/language/get"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


