"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteAssetNode
 * Author:  Dylan Yeo
 * Date:    11/02/22
 * Description: Remove an asset from an asset tree. The asset to be removed can be a device asset or a non-device (logical) asset
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/delete_asset_node.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 11/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def DeleteAssetNode_assetId(accessKey, secretKey, orgId, url, assetId, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "delete", "orgId": orgId, "treeId": treeId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def DeleteAssetNode_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "delete", "orgId": orgId, "treeId": treeId, "productKey":productKey, "deviceKey":deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
