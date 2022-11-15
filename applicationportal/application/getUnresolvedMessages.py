"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUnresolvedMessages
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get the list of unresolved messages that are reported for the applications
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/get_unresolved_messages.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getUnresolvedMessages(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/message/unresolved/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"accessKey": accessKey,
            "orgId": orgId,
            "pagination": { "pageNo":0,
                            "pageSize":5}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
