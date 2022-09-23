"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAssetNode
 * Author:  Dylan Yeo
 * Date:    14/02/22
 * Description: Search for assets based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/search_asset_node.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 14/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def SearchAssetNode(accessKey, secretKey, orgId, url):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "searchAsset", "orgId": orgId}
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


def SearchAssetNode_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "searchAsset", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchAssetNode_Filter(accessKey, secretKey, orgId, url, filter):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "searchAsset", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"filter": filter
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)