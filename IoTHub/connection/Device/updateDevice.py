"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UpdateDevice
 * Author:  Dylan Yeo
 * Date:    21/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/update_device.html
 * refer to the resources/IoTHub/ConnectServiceModel/Device/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 21/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def UpdateDevice_assetId_PatchUpdate(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "update", "orgId": orgId, "assetId": assetId, "IsPatchUpdate": True}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "timezone": "+12:00",
        "deviceName": {"defaultValue": "MyUpdatedDeviceName",
                       "i18nValue": {"zh_CN": "Device_我更新的设备名称", "en_US": "Device_MyUpdatedDeviceName",
                                     "ja_JP": "Device_更新したデバイス名", "es_ES": "Device_MiNombreDeDispositivoActualizado"}},
        "deviceAttributes": {"Attribute_Name": 999},
        "deviceDesc": "New Device Description",
        "deviceTags": {"NewDeviceKey10": "NewDeviceValue10", "NewDeviceKey20": "NewDeviceValue20",
                       "NewDeviceKey30": "NewDeviceValue30"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateDevice_Keys_PatchUpdate(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "update", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey, "IsPatchUpdate": True}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "timezone": "+12:00",
        "deviceName": {"defaultValue": "MyUpdatedDeviceName",
                       "i18nValue": {"zh_CN": "Device_我更新的设备名称", "en_US": "Device_MyUpdatedDeviceName",
                                     "ja_JP": "Device_更新したデバイス名", "es_ES": "Device_MiNombreDeDispositivoActualizado"}},
        "deviceAttributes": {"Attribute_Name": 999},
        "deviceDesc": "New Device Description",
        "deviceTags": {"NewDeviceKey10": "NewDeviceValue10", "NewDeviceKey20": "NewDeviceValue20",
                       "NewDeviceKey30": "NewDeviceValue30"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def UpdateDevice_assetId_NoPatchUpdate(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "update", "orgId": orgId, "assetId": assetId, "IsPatchUpdate": False}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "timezone": "+12:00",
        "deviceName": {"defaultValue": "MyUpdatedDeviceName",
                       "i18nValue": {"zh_CN": "Device_我更新的设备名称", "en_US": "Device_MyUpdatedDeviceName",
                                     "ja_JP": "Device_更新したデバイス名", "es_ES": "Device_MiNombreDeDispositivoActualizado"}},
        "deviceAttributes": {"Attribute_Name": 999},
        "deviceDesc": "New Device Description",
        "deviceTags": {"NewDeviceKey10": "NewDeviceValue10", "NewDeviceKey20": "NewDeviceValue20",
                       "NewDeviceKey30": "NewDeviceValue30"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def UpdateDevice_Keys_NoPatchUpdate(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "update", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey, "IsPatchUpdate": False}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "timezone": "+12:00",
        "deviceName": {"defaultValue": "MyUpdatedDeviceName",
                       "i18nValue": {"zh_CN": "Device_我更新的设备名称", "en_US": "Device_MyUpdatedDeviceName",
                                     "ja_JP": "Device_更新したデバイス名", "es_ES": "Device_MiNombreDeDispositivoActualizado"}},
        "deviceAttributes": {"Attribute_Name": 999},
        "deviceDesc": "New Device Description",
        "deviceTags": {"NewDeviceKey10": "NewDeviceValue10", "NewDeviceKey20": "NewDeviceValue20",
                       "NewDeviceKey30": "NewDeviceValue30"}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)