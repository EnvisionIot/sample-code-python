"""
 * Copyright (C), 2015-2021, Envision
 * FileName: batchUpdateAlertTags
 * Author:  Dylan Yeo
 * Date:    18/02/22
 * Description: Batch update the tags for the specified history and active alerts. The returned structure describes the update results of each alert. If an error message occurs, the error message will be recorded and the rest of the update will continue
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/batch_update_alert_tags.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def batchUpdateAlertTags(accessKey, secretKey, orgId, url, alertId_list):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "batchUpdateTags", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"alertIds": alertId_list,
            "isPatchUpdate": True,
            "tags": {"NewActiveAlert_newverKey1": "NewActiveAlert_newverValue1",
                     "NewActiveAlert_newverKey2": "NewActiveAlert_newverValue2",
                     "NewActiveAlert_newverKey3": "NewActiveAlert_newverValue3"},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)