"""
 * Copyright (C), 2015-2021, Envision
 * FileName: CancelCommand
 * Author:  Dylan Yeo
 * Date:    28/1/22
 * Description: Search for sub-devices under the specified gateway
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_sub_device.html
 * refer to the resources/IoTHub/ConnectServiceModel/GatewayAndSubDevice/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 28/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

ModelId = "Python_Demo_Model"
SubDevice_ProductKey = "4kZqiPoC"

SubDevice_DeviceKey1 = "ma60hFFTeL"
SubDevice_AssetId1 = "OPVD7NPz"
SubDevice_DeviceKey2 = "GW46kFBhkA"
SubDevice_AssetId2 = "Nmw9npSq"

SubDevice_AttributeName = "Date_Attribute"
SubDevice_AttributeValue = "2022-01-01"



def SearchSubDevice_assetId(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"gateway": {"assetId": Gateway_assetId},
            "projection": ["orgId",
                           "assetId",
                           "modelId",
                           "modelIdPath",
                           "productKey",
                           "productName",
                           "productType",
                           "dataFormat",
                           "deviceKey",
                           "deviceName",
                           "deviceSecret",
                           "deviceDesc",
                           "timezone",
                           "deviceAttributes",
                           "deviceTags",
                           "mirrorSource",
                           "firmwareVersion",
                           "createTime",
                           "status",
                           "activeTime",
                           "lastOnlineTime",
                           "lastOfflineTime",
                           "measurepointLastUpdate",
                           "eventLastUpdate",
                           "attributeLastUpdate",
                           "featureLastUpdate"],
            "pagination": {"pageNo": 1,
                           "pageSize": 5}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "projection": ["orgId",
                          "assetId",
                          "modelId",
                          "modelIdPath",
                          "productKey",
                          "productName",
                          "productType",
                          "dataFormat",
                          "deviceKey",
                          "deviceName",
                          "deviceSecret",
                          "deviceDesc",
                          "timezone",
                          "deviceAttributes",
                          "deviceTags",
                          "mirrorSource",
                          "firmwareVersion",
                          "createTime",
                          "status",
                          "activeTime",
                          "lastOnlineTime",
                          "lastOfflineTime",
                          "measurepointLastUpdate",
                          "eventLastUpdate",
                          "attributeLastUpdate",
                          "featureLastUpdate"],
            "pagination": {"pageNo": 1,
                           "pageSize": 5}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_assetId, expression):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey, expression):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_modelId(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "modelId = '" + ModelId + "'"
    # expression = "modelId in ('" + ModelId + "')"
    # expression = "modelId in (\"" + ModelId + "\")"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_modelId(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "modelId = '" + ModelId + "'"
    # expression = "modelId in ('" + ModelId + "')"
    # expression = "modelId in (\"" + ModelId + "\")"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceProductKey(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "productKey = '" + SubDevice_ProductKey + "'"
    # expression = "productKey in ('" + SubDevice_ProductKey + "')"
    # expression = "productKey in (\"" + SubDevice_ProductKey + "\")"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceProductKey(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "productKey = '" + SubDevice_ProductKey + "'"
    # expression = "productKey in ('" + SubDevice_ProductKey + "')"
    # expression = "productKey in (\"" + SubDevice_ProductKey + "\")"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceDeviceKey(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceKey = '" + SubDevice_DeviceKey1 + "'"
    # expression = "deviceKey in ('" + SubDevice_DeviceKey1 + "')"
    # expression = "deviceKey in (\"" + SubDevice_DeviceKey1 + "\")"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceDeviceKey(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceKey = '" + SubDevice_DeviceKey2 + "'"
    # expression = "deviceKey in ('" + SubDevice_DeviceKey2 + "')"
    # expression = "deviceKey in (\"" + SubDevice_DeviceKey2 + "\")"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceAssetId(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "assetId = '" + SubDevice_AssetId1 + "'"
    # expression = "assetId in ('" + SubDevice_AssetId1 + "')"
    # expression = "assetId in (\"" + SubDevice_AssetId1 + "\")"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceAssetId(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "assetId = '" + SubDevice_AssetId2 + "'"
    # expression = "assetId in ('" + SubDevice_AssetId2 + "')"
    # expression = "assetId in (\"" + SubDevice_AssetId2 + "\")"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceDeviceAttributes(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceAttributes." + SubDevice_AttributeName + "='" + SubDevice_AttributeValue + "'"
    # expression = "exists(deviceAttributes." + SubDevice_AttributeName + ")"
    # expression = "not exists(deviceAttributes." + "Random_AttributeName" + ")"
    # expression = "deviceAttributes." + SubDevice_AttributeName + " in ('" + SubDevice_AttributeValue + "')"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceDeviceAttributes(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceAttributes." + SubDevice_AttributeName + "='" + SubDevice_AttributeValue + "'"
    # expression = "exists(deviceAttributes." + SubDevice_AttributeName + ")"
    # expression = "not exists(deviceAttributes." + "Random_AttributeName" + ")"
    # expression = "deviceAttributes." + SubDevice_AttributeName + " in ('" + SubDevice_AttributeValue + "')"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceDeviceTags(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceTags.SubDevice1Key1 = 'SubDevice1Value1'"
    # expression = "exists(deviceTags.SubDevice1Key1)"
    # expression = "not exists(deviceTags.SubDevice1Key1)"
    # expression = "deviceTags.SubDevice1Key1 in ('SubDevice1Value1')"
    # expression = "deviceTags.SubDevice1Key1 = 'SubDevice1Value1' and deviceTags.SubDevice1Key2 = 'SubDevice1Value2'"
    # expression = "deviceTags.SubDevice1Key1 = 'SubDevice1Value1' and deviceTags.SubDevice1Key2 = 'SubDevice1Value2' and deviceTags.SubDevice1Key3 = 'SubDevice1Value3'"
    # expression = "deviceTags.SubDevice1Key1 = 'SubDevice1Value1' or deviceTags.SubDevice2Key1 = 'SubDevice2Value1'"
    # expression = "exists(deviceTags.SubDevice1Key1) and exists(deviceTags.SubDevice1Key3)"
    # expression = "exists(deviceTags.SubDevice1Key1) or exists(deviceTags.SubDevice1Key3)"
    # expression = "deviceTags.SubDevice1Key1 in ('SubDevice1Value1') and deviceTags.SubDevice1Key3 in ('SubDevice1Value3')"
    # expression = "modelId = 'Python_Demo_Model' and deviceTags.SubDevice1Key3 = 'SubDevice1Value3'"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceDeviceTags(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceTags.SubDevice2Key1 = 'SubDevice2Value1'"
    # expression = "exists(deviceTags.SubDevice2Key1)"
    # expression = "not exists(deviceTags.SubDevice2Key1)"
    # expression = "deviceTags.SubDevice2Key1 in ('SubDevice2Value1')"
    # expression = "deviceTags.SubDevice2Key1 = 'SubDevice2Value1' and deviceTags.SubDevice2Key2 = 'SubDevice2Value2'"
    # expression = "deviceTags.SubDevice2Key1 = 'SubDevice2Value1' and deviceTags.SubDevice2Key2 = 'SubDevice2Value2' and deviceTags.SubDevice2Key3 = 'SubDevice2Value3'"
    # expression = "deviceTags.SubDevice2Key1 = 'SubDevice2Value1' or deviceTags.SubDevice1Key1 = 'SubDevice1Value1'"
    # expression = "exists(deviceTags.SubDevice2Key1) and exists(deviceTags.SubDevice2Key3)"
    # expression = "exists(deviceTags.SubDevice2Key1) or exists(deviceTags.SubDevice2Key3)"
    # expression = "deviceTags.SubDevice2Key1 in ('SubDevice2Value1') and deviceTags.SubDevice2Key3 in ('SubDevice2Value3')"
    # expression = "modelId = 'Python_Demo_Model' and deviceTags.SubDevice2Key3 = 'SubDevice2Value3'"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceDeviceName(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceName like 'Python_SubDevice1_Default'"
    # expression = "deviceName.default like 'Python_SubDevice1_Default'"
    # expression = "deviceName.default like 'SubDevice1'"
    # expression = "deviceName.en_US like 'Python_SubDevice1'"
    # expression = "deviceName.zh_CN like 'Python子设备1'"
    # expression = "deviceName.zh_CN like '子设备1'"
    # expression = "deviceName.ja_JP like 'Pythonサブデバイス1'"
    # expression = "deviceName.ja_JP like 'サブデバイス1'"
    # expression = "deviceName.es_ES like 'SubDispositivoPython1'"
    # expression = "deviceName.es_ES like 'Python1'"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceDeviceName(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "deviceName like 'Python_SubDevice2_Default'"
    # expression = "deviceName.default like 'Python_SubDevice2_Default'"
    # expression = "deviceName.default like 'SubDevice2'"
    # expression = "deviceName.en_US like 'Python_SubDevice2'"
    # expression = "deviceName.zh_CN like 'Python子设备2'"
    # expression = "deviceName.zh_CN like '子设备2'"
    # expression = "deviceName.ja_JP like 'Pythonサブデバイス2'"
    # expression = "deviceName.ja_JP like 'サブデバイス2'"
    # expression = "deviceName.es_ES like 'SubDispositivoPython2'"
    # expression = "deviceName.es_ES like 'Python2'"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_assetId_SubDeviceStatus(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "status = 'inactive'"
    # expression = "status = 'online'"
    # expression = "status = 'offline'"
    # expression = "status = 'disable'"
    # expression = "status = 'mirror'"

    body = {"gateway": {"assetId": Gateway_assetId},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchSubDevice_Keys_SubDeviceStatus(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "searchSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    expression = "status = 'inactive'"
    # expression = "status = 'online'"
    # expression = "status = 'offline'"
    # expression = "status = 'disable'"
    # expression = "status = 'mirror'"

    body = {"gateway": {"productKey": Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)