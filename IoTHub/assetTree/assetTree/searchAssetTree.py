"""
 * Copyright (C), 2015-2021, Envision
 * FileName: SearchAssetTree
 * Author:  Dylan Yeo
 * Date:    08/02/22
 * Description: Search for asset trees based on the query criterion
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/search_asset_tree.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 08/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def SearchAssetTree(accessKey, secretKey, orgId, url):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"projection":["treeId",
                          "tags",
                          "asset",
                          "name"],
            "pagination": {"pageNo": 1,
                           "pageSize": 5},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def SearchAssetTree_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchAssetTree_Filter(accessKey, secretKey, orgId, url):
    accessURL = url + '/asset-tree-service/v2.1/asset-trees'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)


    body = {"projection":["treeId",
                          "tags",
                          "asset",
                          "name"],
            "pagination": {"pageNo": 1,
                           "pageSize": 5},
            "filter": {"tags":{"NewAssetTreeKey1": "NewAssetTreeValue1"}}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




