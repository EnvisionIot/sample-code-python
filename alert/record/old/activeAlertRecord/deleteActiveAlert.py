"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteActiveAlert
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Delete an active alert
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/delete_active_alert.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def deleteActiveAlert(accessKey, secretKey, orgId, url, eventId):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "delete", "orgId": orgId, "eventId": eventId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


