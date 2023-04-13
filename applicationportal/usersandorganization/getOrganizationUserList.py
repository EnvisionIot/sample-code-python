"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getOrganizationUserList
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Authorize an application to get a list of all the users under a specified organization (OU) without logging in to the Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_ou_user_list.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getOrganizationUserList(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/organization/roster"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"orgId": orgId,
            "pagination": {"pageNo": 0,
                           "pageSize": 10}
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


