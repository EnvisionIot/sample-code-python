"""
 * Copyright (C), 2015-2021, Envision
 * FileName: DeleteProduct
 * Author:  Dylan Yeo
 * Date:    18/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/delete_product.html
 * refer to the resources/IoTHub/ConnectServiceModel/Product/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 18/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def DeleteProduct(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "delete", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
