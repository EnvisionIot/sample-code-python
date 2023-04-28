"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteAlertContent
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Delete an alert content. It cannot be deleted if it is used by other rules
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/delete_alert_content.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def deleteAlertContent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "delete", "orgId": orgId, "alertContentId": "Python_Content_ID"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


