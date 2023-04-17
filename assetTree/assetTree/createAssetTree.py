"""
 * Copyright (C), 2015-2021, Envision
 * FileName: CreateAssetTree
 * Author:  Dylan Yeo
 * Date:    08/02/22
 * Description: Create an asset tree as well as its root node
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/create_asset_tree.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 08/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def CreateAssetTree(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "create", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"asset": {"modelId": modelId,
                    "name": {"defaultValue": "Default_Demo_Python_Asset",
                            "i18nValue": {"zh_CN": "演示Python断言",
                                          "en_US": "Demo_Python_Asset",
                                          "ja_JP": "デモPythonアサート",
                                          "es_ES": "DeclaraciónDePythonDeDemostración"}},
                    "timezone": "+08:00",
                    "description": "AssetTree_Description",
                    "attributes": {"Int_Attribute": 1,
                                    "Float_Attribute": 1.23,
                                    "String_Attribute": "Asset"},
                    "tags": {"AssetKey1":"AssetValue1",
                             "AssetKey2":"AssetValue2",
                             "AssetKey3":"AssetValue3"}
                    },
          "tree": {"name": {"defaultValue": "Default_Demo_Python_AssetTree",
                            "i18nValue": {"zh_CN": "演示Python资产树",
                                          "en_US": "Demo_Python_AssetTree",
                                          "ja_JP": "デモPythonアセットツリー",
                                          "es_ES": "ÁrbolDeActivosDePythonDeDemostración"}},
                   "tags": {"AssetTreeKey1": "AssetTreeValue1",
                            "AssetTreeKey2": "AssetTreeValue2",
                            "AssetTreeKey3": "AssetTreeValue3"}
                   }
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    treeId = response["data"]
    return treeId

