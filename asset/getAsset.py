"""
 * Copyright (C), 2015-2021, Envision
 * FileName: GetAsset
 * Author:  Dylan Yeo
 * Date:    04/02/22
 * Description: Get asset data by asset ID
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://https://support.envisioniot.com/docs/asset-api/en/2.3.0/get_asset.html
 * refer to the resources/AssetServiceModels/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 04/02/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def GetAsset(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/asset-service/v2.1/assets'
    params = {"action": "get", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


