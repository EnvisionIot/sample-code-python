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


def BatchCreateDevice_MandatoryParams(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "batchCreate", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "deviceList":
            [
                {
                    "productKey": "yourProductKey1",
                    "deviceName":
                        {
                            "defaultValue": "Device Name",
                            "i18nValue":
                                {
                                    "zh_CN": "设备名称",
                                    "en_US": "Device Name"
                                }
                        },
                    "timezone": "+08:00"
                },
                {
                    "productKey": "yourProductKey2",
                    "deviceName":
                        {
                            "defaultValue": "Device Name 2",
                            "i18nValue":
                                {
                                    "zh_CN": "设备名称 2",
                                    "en_US": "Device Name 2"
                                }
                        },
                    "timezone": "+08:00"
                }
            ]
    }

    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    assetId = response["data"]["assetId"]
    deviceKey = response["data"]["deviceKey"]

    return assetId, deviceKey


def CreateDevice_OptionalParams(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "batchCreate", "orgId": orgId, }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "deviceList":
            [
                {
                    "productKey": "yourProductKey1",
                    "deviceName":
                        {
                            "defaultValue": "Device Name",
                            "i18nValue":
                                {
                                    "zh_CN": "设备名称",
                                    "en_US": "Device Name"
                                }
                        },
                    "timezone": "+08:00",
                    "deviceAttributes":
                        {
                            "serial": 111111
                        },
                    "deviceDesc": "Device description",
                    "deviceTags":
                        {
                            "tag1": "tag value"
                        }
                },
                {
                    "productKey": "yourProductKey2",
                    "deviceName":
                        {
                            "defaultValue": "Device Name 2",
                            "i18nValue":
                                {
                                    "zh_CN": "设备名称 2",
                                    "en_US": "Device Name 2"
                                }
                        },
                    "timezone": "+08:00",
                    "deviceAttributes":
                        {
                            "serial": 222222
                        },
                    "deviceDesc": "Device description 2",
                    "deviceTags":
                        {
                            "tag2": "tag value"
                        }
                }
            ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    assetId = response["data"]["assetId"]
    deviceKey = response["data"]["deviceKey"]

    return assetId, deviceKey
