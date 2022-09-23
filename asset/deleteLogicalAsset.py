"""
 * Copyright (C), 2015-2021, Envision
 * FileName: DeleteLogicalAsset
 * Author:  Dylan Yeo
 * Date:    04/02/22
 * Description: Delete a specified logical asset
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://https://support.envisioniot.com/docs/asset-api/en/2.3.0/delete_logical_asset.html
 * refer to the resources/AssetServiceModels/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 04/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def DeleteLogicalAsset(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/asset-service/v2.1/logical-assets'
    params = {"action": "delete", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetId": assetId}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


