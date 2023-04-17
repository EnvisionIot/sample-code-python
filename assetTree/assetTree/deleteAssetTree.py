"""
 * Copyright (C), 2015-2021, Envision
 * FileName: DeleteAssetTree
 * Author:  Dylan Yeo
 * Date:    08/02/22
 * Description: Delete an asset tree
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/delete_asset_tree.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 08/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def DeleteAssetTree(accessKey, secretKey, orgId, url, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "delete", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)




