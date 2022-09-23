"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAlertContent
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Get an alert content based on orgId and contentId
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/get_alert_content.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getAlertContent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "get", "orgId": orgId, "contentId": "Python_Content_ID"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


