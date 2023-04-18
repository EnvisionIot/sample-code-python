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
import requests

url = "https://iot-http-integration-ppe1.envisioniot.com"

def DeleteFile_assetId(accessKey, secretKey, orgId, token, assetId):
    accessURL = url + '/connect-service/v2.1/files'
    params = {"action": "delete", "orgId": orgId, "assetId": assetId,
              "fileUri": "enos-connect://2963f0ba2d000000.txt"
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"apim-accesstoken": token
              }
    print(header)

    body={}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)

def DeleteFile_Keys(accessKey, secretKey, orgId, token, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/files'
    params = {"action": "delete", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey,
              "fileUri": "enos-connect://2963f0b9df000000.txt"
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"apim-accesstoken": token
              }
    print(header)

    body = {}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)



