"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getManageableUserList
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: List all users that can be managed under the current account
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_manag_user_list.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getManageableUserList(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/organization/user/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"pagination": {"pageNo": 0,
                            "pageSize": 10}}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)


