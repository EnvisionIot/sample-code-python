"""
 * Copyright (C), 2015-2021, Envision
 * FileName: ReplaceDevice
 * Author:  Dylan Yeo
 * Date:    21/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/replace_device.html
 * refer to the resources/IoTHub/ConnectServiceModel/Device/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 21/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

NewDeviceKey = 'The_NewDeviceKey.'

def ReplaceDevice_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "replaceDevice", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "newDeviceKey": NewDeviceKey
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def ReplaceDevice_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "replaceDevice", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "newDeviceKey": NewDeviceKey
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    return NewDeviceKey


def ReplaceDevice_ManualType(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, NewerDeviceKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "replaceDevice", "orgId": orgId, "productKey": ProductKey, "deviceKey": DeviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "newDeviceKey": NewerDeviceKey
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    return NewerDeviceKey