"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAndAssociateAsset
 * Author:  Dylan Yeo
 * Date:    11/02/22
 * Description: Create an asset and link it to an asset tree
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/create_and_associate_asset.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 11/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def CreateAndAssociateAsset(accessKey, secretKey, orgId, url, modelId, treeId, parentAssetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "createAsset", "orgId": orgId, "treeId": treeId, "parentAssetId": parentAssetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"asset": {"modelId": modelId,
                    "name": {"defaultValue": "Default_Python_AssetNode",
                            "i18nValue": {"zh_CN": "Python断言节点",
                                          "en_US": "Python_AssetNode",
                                          "ja_JP": "Pythonアサートノード",
                                          "es_ES": "NodoDeAfirmaciónDePython"}},
                    "timezone": "+08:00",
                    "description": "AssetNode_Description",
                    "attributes": {"Int_Attribute": 1,
                                    "Float_Attribute": 1.23,
                                    "String_Attribute": "AssetNode"},
                    "tags": {"AssetNodeKey1":"AssetNodeValue1",
                             "AssetNodeKey2":"AssetNodeValue2",
                             "AssetNodeKey3":"AssetNodeValue3"}
                    }
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    assetId = response["data"]
    return assetId

