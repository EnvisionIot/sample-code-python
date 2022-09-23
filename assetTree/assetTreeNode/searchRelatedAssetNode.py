"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchRelatedAssetNode
 * Author:  Dylan Yeo
 * Date:    14/02/22
 * Description: Search for assets under the specified asset tree based on the relationship with a known asset
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/search_related_asset_node.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 14/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def SearchRelatedAssetNode(accessKey, secretKey, orgId, url, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "searchRelatedAsset", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"projection":["createTime",
                          "modelId",
                          "assetId",
                          "timezone",
                          "name",
                          "description",
                          "attributes",
                          "inValid",
                          "label",
                          "modelIdPath",
                          "tags"],
            "pagination": {"pageNo": 1,
                           "pageSize": 10},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, treeId, filter):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "searchRelatedAsset", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"filter": filter
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)