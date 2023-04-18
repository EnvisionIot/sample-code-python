"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UpdateLogicalAsset
 * Author:  Dylan Yeo
 * Date:    04/02/22
 * Description: Update all or selected details of a logical asset
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://https://support.envisioniot.com/docs/asset-api/en/2.3.0/update_logical_asset.html
 * refer to the resources/AssetServiceModels/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 04/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def UpdateLogicalAsset(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/asset-service/v2.1/logical-assets'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": True}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetUpdateVo": {"assetId": assetId,
                              "name": {"defaultValue": "Default_Updated_Python_Asset",
                                       "i18nValue": {"zh_CN": "更新的python资产", "en_US": "Updated_Python_Asset",
                                                     "ja_JP": "更新されたPythonアセット",
                                                     "es_ES": "ActivoDePythonActualizado"}},
                              "description": "Updated Asset Description",
                              "timezone": "Asia/Shanghai",
                              # "timezone": "+08:00", #Alternative
                              "attributes": {"Int_Attribute": 999,
                                             "Float_Attribute": 123.456,
                                             "String_Attribute": "Update_Asset"},
                              "tags": {"AssetKey1": "Updated_AssetValue1",
                                       "AssetKey2": "Updated_AssetValue2",
                                       "AssetKey3": "Updated_AssetValue3",
                                       "AssetKey4": "New_AssetValue4"}
                              }
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
