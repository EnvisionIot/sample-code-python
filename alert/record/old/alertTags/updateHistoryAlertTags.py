"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateHistoryAlert
 * Author:  Dylan Yeo
 * Date:    17/02/22
 * Description: Update the tags of a history alert
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/update_history_alert_tags.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateHistoryAlertTags(accessKey, secretKey, orgId, url, eventId):
    accessURL = url + '/event-service/v2.1/history-alerts'
    params = {"action": "updateTags", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"eventId": eventId,
            "isPatchUpdate": True,
            "tags": {"NewHistoryAlertKey1": "NewHistoryAlertValue1",
                    "NewHistoryAlertKey2": "NewHistoryAlertValue2",
                    "NewHistoryAlertKey3": "NewHistoryAlertValue3"},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
