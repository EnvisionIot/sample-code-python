"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateMessages
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Update the status of the message
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/update_messages.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def updateMessages(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.2/message/update"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"messages": [{"messageId": "test_messageId",
                          "accessKey": accessKey,
                          "state": "1"}]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
