"""
 * Copyright (C), 2015-2021, Envision
 * FileName: SetMeasurementPoint
 * Author:  Dylan Yeo
 * Date:    21/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/set_measurepoint.html
 * refer to the resources/ConnectServiceModel/DeviceData/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 21/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def SetMeasurementPoint_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "setMeasurepoint", "orgId": orgId, "assetId": assetId,
              "measurepointId": "Int_MeasurementPoint",  # Set MeasurementPoints Identifier
              "pendingTtl": 172800,  # Set cache storage time 0 - 172800 seconds, [Optional: Default = 0 seconds]
              "timeout": 30  # Set timeout period 1 - 60 seconds, [Optional: Default = 30 seconds]
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"value": 5000  # Set value of measurepointId
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:  # in case of any error and unable to retrieve data
        commandId = response["data"]["commandId"]
    except:
        commandId = str(None)
    print("commandId: " + commandId)
    return (commandId)


def SetMeasurementPoint_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "setMeasurepoint", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey,
              "measurepointId": "Float_MeasurementPoint",  # Set MeasurementPoints Identifier
              "pendingTtl": 172800,  # Set cache storage time 0 - 172800 seconds, [Optional: Default = 0 seconds]
              "timeout": 60  # Set timeout period 1 - 60 seconds, [Optional: Default = 30 seconds]
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"value": 15.5  # Set value of measurepointId
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:  # in case of any error and unable to retrieve data
        commandId = response["data"]["commandId"]
    except:
        commandId = str(None)
    print("commandId: " + commandId)
    return (commandId)
