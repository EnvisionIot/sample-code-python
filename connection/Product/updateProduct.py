"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UpdateProduct
 * Author:  Dylan Yeo
 * Date:    18/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/update_product.html
 * refer to the resources/IoTHub/ConnectServiceModel/Product/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 18/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def UpdateProduct_productDesc(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_ForSearchProduct>"
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateProduct_biDirectionalAuth(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "biDirectionalAuth": True
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateProduct_dynamicActivateEnabled(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "dynamicActivateEnabled": True
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateProduct_productName(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productName": {"defaultValue": "<Product_Name_SearchProductTest2>",
                        "i18nValue": {"zh_CN": "SearchProductTest_简体中文2", "en_US": "SearchProductTest2",
                                      "ja_JP": "SearchProductTest_日本語2", "es_ES": "SearchProductTest_Español2"}}
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateProduct_productTags(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productTags": {"SearchKey100": "SearchValue100"}
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def UpdateProduct_defaultValidDay(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "biDirectionalAuth": True,
        "defaultValidDay": "730"
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateProduct_maxValidDay(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "biDirectionalAuth": True,
        "maxValidDay": "1460"
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateProduct(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "update", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_ForSearchProduct10>",
        "biDirectionalAuth": True,
        "dynamicActivateEnabled": True,
        "productName": {"defaultValue": "<Product_Name_SearchProductTest10>",
                        "i18nValue": {"zh_CN": "SearchProductTest10_简体中文", "en_US": "SearchProductTest10",
                                      "ja_JP": "SearchProductTest10_日本語", "es_ES": "SearchProductTest10_Español"}},
        "productTags": {"SearchKey10": "SearchValue10", "SearchKey20": "SearchValue20", "SearchKey30": "SearchValue30"},
        "defaultValidDay": "3640",
        "maxValidDay": "3650"
        
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)



