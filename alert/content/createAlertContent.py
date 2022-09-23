"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAlertContent
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Create a new alert content
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_alert_content.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createAlertContent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-contents'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"alertContent": {"contentId": "Python_Content_ID",
                           "contentDesc": {"defaultValue": "Default_Contents",
                                           "i18nValue": {"en_US": "Contents",
                                                         "zh_CN": "内容",
                                                         "ja_JP":"コンテンツ",
                                                         "es_ES":"Contenido"}},
                           "tags": {"ContentKey1": "ContentValue1",
                                    "ContentKey2": "ContentValue2",
                                    "ContentKey3": "ContentValue3"},
                           "modelId": "Python_Demo_Model",
                           "alertTypeId": "Python_Type_ID"}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


