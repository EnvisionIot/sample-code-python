"""
 * Copyright (C), 2015-2021, Envision
 * FileName: batchUpdateActiveAlertTags
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Batch update the tag data for the specified alerts in the current alert library. The returned structure will indicate the updated results of each alert. When an update error occurs for an alert, the error information will be recorded and the remaining update process will continue
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/batch_update_active_alert_tags.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def batchUpdateActiveAlertTags(accessKey, secretKey, orgId, url, eventId_list):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "batchUpdateTags", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"eventIds": eventId_list,
            "isPatchUpdate": True,
            "tags": {"NewActiveAlertKey1": "NewActiveAlertValue1",
                     "NewActiveAlertKey2": "NewActiveAlertValue2",
                     "NewActiveAlertKey3": "NewActiveAlertValue3"},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)