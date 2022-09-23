"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchAssetPath
 * Author:  Dylan Yeo
 * Date:    14/02/22
 * Description: Search for paths on the asset tree. A path is a complete path from a superior asset node to a subordinate asset node, which can contain intermediate asset nodes
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/search_asset_path.html
 * refer to the resources/AssetTreeService
 *
 * @author dylan.yeo
 * @create 14/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def SearchAssetPath(accessKey, secretKey, orgId, url, treeId):
    accessURL = url + '/asset-tree-service/v2.1/asset-paths'
    params = {"action": "search", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"projection":["assetPaths",
                          "assets"],
            "pagination": {"pageNo": 1,
                           "pageSize": 10},
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchAssetPath_from(accessKey, secretKey, orgId, url, treeId, from_parameter):
    accessURL = url + '/asset-tree-service/v2.1/asset-paths'
    params = {"action": "search", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"from": from_parameter
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchAssetPath_to(accessKey, secretKey, orgId, url, treeId, to_parameter):
    accessURL = url + '/asset-tree-service/v2.1/asset-paths'
    params = {"action": "search", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"to": to_parameter
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchAssetPath_pathProjection(accessKey, secretKey, orgId, url, treeId, pathStatus):
    accessURL = url + '/asset-tree-service/v2.1/asset-paths'
    params = {"action": "search", "orgId": orgId, "treeId": treeId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"pathProjection": pathStatus
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)