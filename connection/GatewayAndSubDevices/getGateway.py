"""
 * Copyright (C), 2015-2021, Envision
 * FileName: GetGateway
 * Author:  Dylan Yeo
 * Date:    28/1/22
 * Description:
 * History: Get the gateway information based on the specified sub-device
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/get_gateway.html
 * refer to the resources/IoTHub/ConnectServiceModel/GatewayAndSubDevice/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 28/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

ModelId = "Python_Demo_Model"
SubDevice_ProductKey = "pk1"

SubDevice_DeviceKey1 = "dk1"
SubDevice_AssetId1 = "assetId1"
SubDevice_DeviceKey2 = "dk2"
SubDevice_AssetId2 = "assetid2"


def GetGateway_assetId(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "getGateway", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"subDevice": {"assetId": SubDevice_AssetId2}
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def GetGateway_Keys(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/device-topos'
    params = {"action": "getGateway", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"subDevice": {"productKey": SubDevice_ProductKey, "deviceKey": SubDevice_DeviceKey1}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
