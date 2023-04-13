"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateActiveAlertTags
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description:  Update the tags of an active alert
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/update_active_alert_tags.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateActiveAlertTags(accessKey, secretKey, orgId, url, eventId):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "updateTags", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"eventId": eventId,
            "isPatchUpdate": True,
            "tags": {"NewActiveAlertKey1": "NewActiveAlertValue1",
                    "NewActiveAlertKey2": "NewActiveAlertValue2",
                    "NewActiveAlertKey3": "NewActiveAlertValue3"},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

