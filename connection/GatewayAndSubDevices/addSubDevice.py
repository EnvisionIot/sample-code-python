"""
 * Copyright (C), 2015-2021, Envision
 * FileName: AddSubDevice
 * Author:  Dylan Yeo
 * Date:    28/1/22
 * Description: Add new sub-devices to gateway device (creating a topological relationship)
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/add_sub_device.html
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


def AddSubDevice_assetId(accessKey, secretKey, orgId, url, Gateway_assetId):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "addSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"gateway": {"assetId": Gateway_assetId},
            "subDevices": [{"assetId": SubDevice_AssetId1}, {"assetId": SubDevice_AssetId2}]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def AddSubDevice_Keys(accessKey, secretKey, orgId, url, Gateway_productKey, Gateway_deviceKey):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "addSubDevice", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"gateway": {"productKey":Gateway_productKey, "deviceKey": Gateway_deviceKey},
            "subDevices": [{"productKey": SubDevice_ProductKey, "deviceKey": SubDevice_DeviceKey1},
                           {"productKey": SubDevice_ProductKey, "deviceKey": SubDevice_DeviceKey2}]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


