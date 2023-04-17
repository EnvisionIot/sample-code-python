"""
 * Copyright (C), 2015-2021, Envision
 * FileName: CreateProduct
 * Author:  Dylan Yeo
 * Date:    18/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/create_product.html
 * refer to the resources/IoTHub/ConnectServiceModel/Product/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 18/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def CreateProduct_Basic(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_Basic>",
        "biDirectionalAuth": False,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "Product_Name_Basic"},
        "productType": "Device"
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_biDirectionalAuth(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_biDirectionalAuth>",
        "biDirectionalAuth": True,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_biDirectionalAuth>"},
        "productType": "Device"
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_dataFormatCustom(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_dataFormatCustom>",
        "biDirectionalAuth": False,
        "modelId": modelId,
        "dataFormat": "Custom",
        "productName": {"defaultValue": "<Product_Name_dataFormatCustom>"},
        "productType": "Device"
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_localeName(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_localeName>",
        "biDirectionalAuth": False,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_localeName>",
                        "i18nValue": {"zh_CN": "Product_Name_简体中文", "en_US": "Product_Name_English",
                                      "ja_JP": "Product_Name_日本語", "es_ES": "Product_Name_Español"}},
        "productType": "Device"
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_productType_Gateway(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_productType_Gateway>",
        "biDirectionalAuth": False,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_productType_Gateway>"},
        "productType": "Gateway"
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_dynamicActivateEnabled(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_dynamicActivateEnabled>",
        "biDirectionalAuth": False,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_dynamicActivateEnabled>"},
        "productType": "Device",
        "dynamicActivateEnabled": True
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_productTags(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_productTags>",
        "biDirectionalAuth": False,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_productTags>"},
        "productType": "Device",
        "productTags": {"Key1": "Value1", "Key2": "Value2", "Key3": "Value3"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_defaultValidDay(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_defaultValidDay>",
        "biDirectionalAuth": True,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_defaultValidDay>"},
        "productType": "Device",
        "defaultValidDay": 10
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_maxValidDay(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_maxValidDay>",
        "biDirectionalAuth": True,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_maxValidDay>"},
        "productType": "Device",
        "maxValidDay": 750
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_deafaultandmaxValidDay(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_defaultandmaxValidDay>",
        "biDirectionalAuth": True,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_defaultandmaxValidDay>"},
        "productType": "Device",
        "defaultValidDay": 100,
        "maxValidDay": 200
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey


def CreateProduct_ForTesting(accessKey, secretKey, orgId, url, modelId):
    accessURL = url + '/connect-service/v2.1/products'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productDesc": "<Product_Description_ForProductTest>",
        "biDirectionalAuth": True,
        "modelId": modelId,
        "dataFormat": "Json",
        "productName": {"defaultValue": "<Product_Name_ProductTest>",
                        "i18nValue": {"zh_CN": "ProductTest_简体中文", "en_US": "ProductTest",
                                      "ja_JP": "ProductTest_日本語", "es_ES": "ProductTest_Español"}},
        "productType": "Device",
        "dynamicActivateEnabled": True,
        "productTags": {"SearchKey1": "SearchValue1", "SearchKey2": "SearchValue2", "SearchKey3": "SearchValue3"},
        "defaultValidDay": 365,
        "maxValidDay": 730
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    ProductKey = response["data"]
    return ProductKey
