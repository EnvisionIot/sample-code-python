import poseidon.poseidon
from requests.models import PreparedRequest


def AssociateAssetBatch_assetId(accessKey, secretKey, orgId, url, treeId, parentAssetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "associateAssetBatch", "orgId": orgId,
              "treeId": treeId, "parentAssetId": parentAssetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "assetIdentifiersVoList": [
            {
                "deviceKey": "yourDeviceKey1",
                "productKey": "yourProductKey1"
            },
            {
                "deviceKey": "yourDeviceKey2",
                "productKey": "yourProductKey2"
            }
        ]
    }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def AssociateAssetBatch_Keys(accessKey, secretKey, orgId, url, treeId, parentAssetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "associateAsset", "orgId": orgId,
              "treeId": treeId, "parentAssetId": parentAssetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "assetIdentifiersVoList": [
            {
                "assetId": "yourAssetId1"
            },
            {
                "assetId": "yourAssetId2"
            }
        ]
    }
    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
