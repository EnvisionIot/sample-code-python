"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateAlertSeverity
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Update an alert severity
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/update_alert_severity.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateAlertSeverity(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-severities'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"severity": {"severityId": "Python_Severity_ID",
                       "severityDesc": {"defaultValue": "Default_Updated_Severity_Error",
                                        "i18nValue": {"en_US": "Updated_Severity_Error",
                                                      "zh_CN": "更新的严重性错误",
                                                      "ja_JP":"更新された重大度エラー",
                                                      "es_ES":"ErrorDeGravedadActualizado"}},
                       "tags": {"NewSeverityKey1": "NewSeverityValue1",
                                "NewSeverityKey2": "NewSeverityValue2",
                                "NewSeverityKey3": "NewSeverityValue3"}}
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

