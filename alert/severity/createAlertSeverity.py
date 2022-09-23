"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAlertSeverity
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Create a new alert severity
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_alert_severity
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createAlertSeverity(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-severities'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"severity": {"severityId": "Python_Severity_ID",
                       "severityDesc": {"defaultValue": "Default_Severity_Error",
                                        "i18nValue": {"en_US": "Severity_Error",
                                                      "zh_CN": "严重性错误",
                                                      "ja_JP":"重大度エラー",
                                                      "es_ES":"ErrorDeGravedad"}},
                       "tags": {"SeverityKey1": "SeverityValue1",
                                "SeverityKey2": "SeverityValue2",
                                "SeverityKey3": "SeverityValue3"}}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


