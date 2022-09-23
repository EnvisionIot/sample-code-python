"""
 * Copyright (C), 2015-2021, Envision
 * FileName: CreateLogicalAsset
 * Author:  Dylan Yeo
 * Date:    04/02/22
 * Description: Create a logical asset
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-api/en/2.3.0/create_logical_asset.html
 * refer to the resources/AssetServiceModels/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 04/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def CreateLogicalAsset(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/asset-service/v2.1/logical-assets'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"assetInstance": {"modelId": modelId,
                            "name": {"defaultValue": "Demo_Python_Asset",
                                    "i18nValue": {"zh_CN": "演示Python断言", "en_US": "Asset_Demo_Python_Asset",
                                    "ja_JP": "デモPythonアサート", "es_ES": "DeclaraciónDePythonDeDemostración"}},
                            "timezone": "+08:00",
                            "description": "Asset_Description",
                            "attributes": {"Int_Attribute": 1,
                                           "Float_Attribute": 1.23,
                                           "String_Attribute": "Asset"},
                            "tags": {"AssetKey1":"AssetValue1",
                                     "AssetKey2":"AssetValue2",
                                     "AssetKey3":"AssetValue3"}
                            }
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    AssetId = response["data"]
    return AssetId


