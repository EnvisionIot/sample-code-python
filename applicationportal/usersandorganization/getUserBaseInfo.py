"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUserBaseInfo
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Get basic information about a user, such as the user ID, based on the user’s email, account and domain, or phone number and phone area code
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_user_base_info.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getUserBaseInfo(accessKey, secretKey, orgId, url, email=None, name=None, domain=None, phoneArea=None, phone=None):
    accessURL = url + "/app-portal-service/v2.2/user/getUserBaseInfo"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "email": email,
            "name": name,
            "domain": domain,
            "phoneArea": phoneArea,
            "phone": phone}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
