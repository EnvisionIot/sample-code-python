"""
 * Copyright (C), 2015-2021, Envision
 * FileName: updateAlertType
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Update an alert type. If the alert type already has a parent alert type, the parentTypeId cannot be updated
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/update_alert_type.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def updateAlertType(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-types'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"type": {"typeId": "Python_Type_ID",
                   "typeDesc": {"defaultValue": "Default_Updated_Alert_Type",
                                "i18nValue": {"en_US": "Updated_Alert_Type",
                                              "zh_CN": "更新的警报类型",
                                              "ja_JP":"アラートタイプを更新",
                                              "es_ES":"Tipo De Alerta Actualizado"}},
                   "tags": {"NewTypeKey1": "NewTypeValue1",
                            "NewTypeKey2": "NewTypeValue2",
                            "NewTypeKey3": "NewTypeValue3"}}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def updateAlertType_withParent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-types'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"type": {"typeId": "Python_Type_ID_Child",
                   "typeDesc": {"defaultValue": "Default_Updated_Alert_Type_Child",
                                "i18nValue": {"en_US": "Updated_Alert_Type_Child",
                                              "zh_CN": "更新的警报类型子级",
                                              "ja_JP":"アラートタイプの子を更新",
                                              "es_ES":"Niño De Tipo De Alerta Actualizado"}},
                   "tags": {"NewTypeKey1_Child": "NewTypeValue1_Child",
                            "NewTypeKey2_Child": "NewTypeValue2_Child",
                            "NewTypeKey3_Child": "NewTypeValue3_Child"},
                   "parentTypeId": "Python_Type_ID"}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

