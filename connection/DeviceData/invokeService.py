"""
 * Copyright (C), 2015-2021, Envision
 * FileName: InvokeService
 * Author:  Dylan Yeo
 * Date:    26/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/invoker_service.html
 * refer to the resources/ConnectServiceModel/DeviceData/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 26/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def InvokeService_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "invokeService", "orgId": orgId, "assetId": assetId,
              "serviceId": "Service1", # Set Service Identifier
              "pendingTtl": 10,  # Set cache storage time 0 - 172800 seconds, [Optional: Default = 0 seconds]
              "timeout": 30}  # Set timeout period 1 - 60 seconds, [Optional: Default = 30 seconds]
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body ={"inputData": {"Service1Parameter1": 20, "Service1Parameter2": 40}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def InvokeService_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "invokeService", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey,
              "serviceId": "Service2",  # Set Service Identifier
              "pendingTtl": 10,  # Set cache storage time 0 - 172800 seconds, [Optional: Default = 0 seconds]
              "timeout": 30}  # Set timeout period 1 - 60 seconds, [Optional: Default = 30 seconds]
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"inputData": {"Service2Parameter1":100}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

