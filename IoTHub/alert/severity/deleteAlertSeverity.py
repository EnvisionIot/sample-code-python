"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteAlertSeverity
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Delete an alert severity. It cannot be deleted if it is used by other rules
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/delete_alert_severity.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def deleteAlertSeverity(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-severities'
    params = {"action": "delete", "orgId": orgId, "severityId": "Severity_ID"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

