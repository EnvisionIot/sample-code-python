"""
 * Copyright (C), 2015-2021, Envision
 * FileName: CreateAssetTree
 * Author:  Dylan Yeo
 * Date:    08/02/22
 * Description: Create an asset tree and link an existing asset as the root node of the asset tree.
 *              The asset to be linked can be a device asset or a non-device (logical) asset.
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/create_asset_tree_and_associate_asset.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 08/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def CreateAssetTreeAndAssociateAsset_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "associate", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={ "tree": {"name": {"defaultValue": "Default_Demo_Python_AssetTree",
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

    TreeId = response["data"]
    return TreeId


def CreateAssetTreeAndAssociateAsset_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "associate", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={ "tree": {"name": {"defaultValue": "Default_Demo_Python_AssetTree",
                             "i18nValue": {"zh_CN": "演示Python资产树", "en_US": "Demo_Python_AssetTree",
                             "ja_JP": "デモPythonアセットツリー", "es_ES": "ÁrbolDeActivosDePythonDeDemostración"}},
                   "tags": {"AssetTreeKey1": "AssetTreeValue1",
                            "AssetTreeKey2": "AssetTreeValue2",
                            "AssetTreeKey3": "AssetTreeValue3"}
                   }
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    TreeId = response["data"]
    return TreeId



