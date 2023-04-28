"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAlertType
 * Author:  Dylan Yeo
 * Date:    15/02/22
 * Description: Create a new alert type
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/create_alert_type.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createAlertType(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-types'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"type": {"typeId": "Python_Type_ID",
                   "typeDesc": {"defaultValue": "Default_Alert_Type",
                                "i18nValue": {"en_US": "Alert_Type",
                                              "zh_CN": "警报类型",
                                              "ja_JP":"アラートタイプ",
                                              "es_ES":"Tipo De Alerta"}},
                   "tags": {"TypeKey1": "TypeValue1",
                            "TypeKey2": "TypeValue2",
                            "TypeKey3": "TypeValue3"}}
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createAlertType_addParent(accessKey, secretKey, orgId, url):
    accessURL = url + '/event-service/v2.1/alert-types'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"type": {"typeId": "Python_Type_ID_Child",
                   "typeDesc": {"defaultValue": "Default_Alert_Type_Child",
                                "i18nValue": {"en_US": "Alert_Type_Child",
                                              "zh_CN": "警报类型的孩子",
                                              "ja_JP":"アラートタイプの子",
                                              "es_ES":"Tipo De Alerta Niño"}},
                   "tags": {"TypeKey1_Child": "TypeValue1_Child",
                            "TypeKey2_Child": "TypeValue2_Child",
                            "TypeKey3_Child": "TypeValue3_Child"},
                   "parentTypeId": "Python_Type_ID"
                   }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

