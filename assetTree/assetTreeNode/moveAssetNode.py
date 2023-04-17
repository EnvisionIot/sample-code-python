import poseidon.poseidon
from requests.models import PreparedRequest

def MoveAssetNode(accessKey, secretKey, orgId, url, assetId, treeId, parentAssetId, preAssetId):
    accessURL = url + '/asset-tree-service/v2.1/asset-nodes'
    params = {"action": "move", "orgId": orgId, "assetId": assetId,
              "treeId": treeId, "parentAssetId": parentAssetId, "preAssetId": preAssetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
