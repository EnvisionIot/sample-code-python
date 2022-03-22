"""
 * Copyright (C), 2015-2021, Envision
 * FileName: refreshToken
 * Author:  Dylan Yeo
 * Date:    18/2/22
 * Description: Refresh the generated access token before it expires (the expiring time of the access token is 2 hours by default)
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/api/en/2.3.0/token/refresh_access_token.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
import time
import hashlib

currentTime = round(time.time()*1000.0)

def refreshToken(accessKey, secretKey, url, token):
    accessURL = url + '/apim-token-service/v2.0/token/refresh'
    params={}
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
          "timestamp": currentTime,
          "accessToken": token
          }

    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


