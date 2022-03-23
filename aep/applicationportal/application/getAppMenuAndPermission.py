"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAppMenuAndPermission
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get the list of application menus and permissions
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/get_app_menu_and_permission.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAppMenuAndPermission(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/user/app/resource/info"
    params = {"accessKey": accessKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
