"""
 * Copyright (C), 2015-2021, Envision
 * FileName: associateAsset
 * Author:  Dylan Yeo
 * Date:    11/02/22
 * Description: Link an existing asset to an asset tree. The asset to be linked can be a device asset or a non-device (logical) asset
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/associate_asset.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 11/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def AssociateAsset_assetId(accessKey, secretKey, orgId, url, assetId, treeId, parentAssetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "associateAsset", "orgId": orgId, "assetId": assetId,
              "treeId": treeId, "parentAssetId": parentAssetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def AssociateAsset_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey, treeId, parentAssetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "associateAsset", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey,
              "treeId": treeId, "parentAssetId": parentAssetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

