"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UpdateAssetTree
 * Author:  Dylan Yeo
 * Date:    08/02/22
 * Description: Update the information of an asset tree
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/update_asset_tree.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 08/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def UpdateAssetTree(accessKey, secretKey, orgId, url, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "update", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"treeUpdateInfo":{"treeId":treeId,
                            "name": {"defaultValue": "Default_Updated_Python_AssetTree",
                            "i18nValue": {"zh_CN": "更新Python资产树",
                                          "en_US": "Updated_Python_AssetTree",
                                          "ja_JP": "更新されたPythonアセットツリー",
                                          "es_ES": "ÁrbolDeActivosDePythonActualizado"}},
                            "tags": {"NewAssetTreeKey1": "NewAssetTreeValue1",
                                     "NewAssetTreeKey2": "NewAssetTreeValue2",
                                     "NewAssetTreeKey3": "NewAssetTreeValue3"}
         }}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)



