"""
 * Copyright (C), 2015-2021, Envision
 * FileName: CreateDevice
 * Author:  Dylan Yeo
 * Date:    21/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https:// support.envisioniot.com/docs/connection-api/en/2.3.0/create_device.html
 * refer to the resources/IoTHub/ConnectServiceModel/Device/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 21/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def CreateDevice_MandatoryParams(accessKey, secretKey, orgId, url, ProductKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productKey": ProductKey,
        "timezone": "+08:00",
        "deviceName": {"defaultValue":"Device"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    assetId = response["data"]["assetId"]
    deviceKey = response["data"]["deviceKey"]

    return assetId, deviceKey


def CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "create", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "productKey": ProductKey,
        "timezone": "+08:00",
        "deviceName": {"defaultValue":"MyDeviceName", "i18nValue": {"zh_CN": "Device_我的设备名称", "en_US": "Device_MyDeviceName",
                                      "ja_JP": "Device_私のデバイス名", "es_ES": "Device_NombreDeMiDispositivo"}},
        # deviceAttribute Format : {<Attribute Identifier Name>: <Value according to data type>}
        "deviceAttributes": {"Attribute_Name" : 100},
        "deviceKey": "Any_DeviceKey.",
        "deviceDesc": "Standard Device Description",
        "deviceTags": {"DeviceKey1": "DeviceValue1", "DeviceKey2": "DeviceValue2", "DeviceKey3": "DeviceValue3"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    assetId = response["data"]["assetId"]
    deviceKey = response["data"]["deviceKey"]

    return assetId, deviceKey

