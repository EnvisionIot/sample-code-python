"""
 * Copyright (C), 2015-2021, Envision
 * FileName: GetAssetTree
 * Author:  Dylan Yeo
 * Date:    08/02/22
 * Description: Get the details of an asset tree using an asset tree ID
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/get_asset_tree.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 08/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def GetAssetTree(accessKey, secretKey, orgId, url, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "get", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

    assetId = response["data"]["asset"]["assetId"]
    return assetId

