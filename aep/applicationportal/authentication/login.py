"""
 * Copyright (C), 2015-2021, Envision
 * FileName: login
 * Author:  Dylan Yeo
 * Date:    16/03/22
 * Description: Log in to the account
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/authentication/login.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def login(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.2/login"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"account": "songxibin2013",
            "password": "Password1"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        accessToken = response["data"]["accessToken"]
    except:
        accessToken = None
    return accessToken

def login_admin(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.2/login"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"account": "cat01.enos",
            "password": "Cat@2020"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        accessToken = response["data"]["accessToken"]
    except:
        accessToken = None
    return accessToken