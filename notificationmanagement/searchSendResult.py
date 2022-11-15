"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchSendResult
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: When the above two interfaces are successfully invoked, the user receives the return result containing eventId, which can be used to search for the actual sent result of the message in this interface
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/notification-mgmt-api/en/2.3.0/api_reference/search_send_result.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def searchSendResult(accessKey, secretKey, orgId, url, eventId):
    accessURL = url + "/notification-center-service/v2.0/search/message"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"eventId": eventId}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
