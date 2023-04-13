"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUserDomain
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Get the domain information of a user using the email address
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_user_domain.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getUserDomain(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.2/user/domain"
    params = {"email": "songxibin2013@gmail.com"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


