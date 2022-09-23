"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UpdateAsset
 * Author:  Dylan Yeo
 * Date:    04/02/22
 * Description: Update asset information
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://https://support.envisioniot.com/docs/asset-api/en/2.3.0/update_asset.html
 * refer to the resources/AssetServiceModels/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 04/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def UpdateAsset(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/asset-service/v2.1/assets'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"asset": {"assetId": assetId,
                      "name": {"defaultValue": "Python_Demo_Device",
                               "i18nValue": {"zh_CN": "Python 演示设备", "en_US": "Python_Demo_Device",
                                             "ja_JP": "Pythonデモデバイス",
                                             "es_ES": "DispositivoDeDemostraciónDePython"}},
                      "description": "Updated Description",
                      "timezone": "Asia/Shanghai",
                      # "timezone": "+08:00", #Alternative
                      "attributes": {"Int_Attribute": 246,
                                     "Float_Attribute": 123.456,
                                     "String_Attribute": "Update_Device"},
                      "tags": {"DeviceKey1": "DeviceValue1",
                               "DeviceKey2": "DeviceValue2",
                               "DeviceKey3": "DeviceValue3"}
                       }
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


