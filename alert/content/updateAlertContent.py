"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateAlertContent
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Update an alert content
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/update_alert_content.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateAlertContent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertContent": {"contentId": "Python_Content_ID",
                           "contentDesc": {"defaultValue": "Updated_Default_Contents",
                                           "i18nValue": {"en_US": "Updated_Contents",
                                                         "zh_CN": "更新内容",
                                                         "ja_JP":"更新された内容",
                                                         "es_ES":"Contenidos Actualizados"}},
                           "tags": {"NewContentKey1": "NewContentValue1",
                                    "NewContentKey2": "NewContentValue2",
                                    "NewContentKey3": "NewContentValue3"},
                           "modelId": "Python_Demo_Model",
                           "alertTypeId": "Python_Type_ID"}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


