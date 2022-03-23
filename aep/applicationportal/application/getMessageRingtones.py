"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getMessageRingtones
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get the list of ringtones for configuring the message
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/get_message_ringtones.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getMessageRingtones(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.2/message/enum/ringtones"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
