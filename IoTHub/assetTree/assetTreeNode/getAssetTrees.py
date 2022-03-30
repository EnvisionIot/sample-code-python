"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetTrees
 * Author:  Dylan Yeo
 * Date:    11/02/22
 * Description: Get the details of one or multiple asset trees based on a set of assetIds. If the assetId is not in the tree, no Key will be returned in data
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/get_asset_trees.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 11/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def GetAssetTrees(accessKey, secretKey, orgId, url):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "getAssetTree", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": ["AvxV8hkR"],
            "projection":["*.[*].treeId","*.[*].tags","*.[*].asset","*.[*].name"]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


