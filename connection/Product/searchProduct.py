"""
 * Copyright (C), 2015-2021, Envision
 * FileName: SearchProduct
 * Author:  Dylan Yeo
 * Date:    18/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_product.html
 * refer to the resources/IoTHub/ConnectServiceModel/Product/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 18/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def SearchProduct(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "search", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchProduct_Pagination(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "search", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"pagination": {
        "pageNo": 2,
        "pageSize": 25,
    }
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchProduct_expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "search", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)