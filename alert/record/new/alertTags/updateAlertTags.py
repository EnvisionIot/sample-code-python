"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateAlertTags
 * Author:  Dylan Yeo
 * Date:    18/02/22
 * Description:  Update history and active alert tags
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/update_alert_tags.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateAlertTags(accessKey, secretKey, orgId, url, alertId):
    accessURL = url + '/alert-service/v2.1/alerts'
    params = {"action": "updateTags", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"alertId": alertId,
            "isPatchUpdate": True,
            "tags": {"NewActiveAlert_newverKey1": "NewActiveAlert_newverValue1",
                     "NewActiveAlert_newverKey2": "NewActiveAlert_newverValue2",
                     "NewActiveAlert_newverKey3": "NewActiveAlert_newverValue3"},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

