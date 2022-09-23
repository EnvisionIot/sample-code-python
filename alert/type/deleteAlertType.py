"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteAlertType
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Delete an alert type. It cannot be deleted if it is used by other rules
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/delete_alert_type.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def deleteAlertType(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-types'
    params = {"action": "delete", "orgId": orgId, "alertTypeId": "Python_Type_ID_Child"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

