"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getToken
 * Author:  Dylan Yeo
 * Date:    3/2/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/api/en/2.3.0/token/get_access_token.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
import time
import hashlib

currentTime = round(time.time()*1000.0)

def GetToken(accessKey, secretKey, url):
    accessURL = url + '/apim-token-service/v2.0/token/get'
    params={}
    # params = {"action": "get"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    concat = accessKey + str(currentTime) + secretKey
    print(concat)

    encode = concat.encode()
    print(encode)

    encryption = hashlib.sha256(encode)
    print(encryption)

    hexadecimal = encryption.hexdigest()
    print(hexadecimal)


    body={"appKey": accessKey,
          "encryption": hexadecimal.lower(),
          "timestamp": currentTime
          }

    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    Token = response["data"]["accessToken"]
    return Token


