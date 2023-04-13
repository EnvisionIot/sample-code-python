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

def DownloadFile_assetId(orgId, token, assetId):
    accessURL = url + '/connect-service/v2.1/files'
    params = {"action": "download", "orgId": orgId, "assetId": assetId,
              "fileUri": "enos-connect://2963ede9f0800000.txt", "category": "feature"
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"apim-accesstoken": token
              }
    print(header)

    r = requests.get(req.url, headers=header)
    content = r.content
    response = content.decode("UTF-8")
    print(response)


def DownloadFile_Keys(orgId, token, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/files'
    params = {"action": "download", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey,
              "fileUri": "enos-connect://2963ede9f0800000.txt", "category": "feature"
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"apim-accesstoken": token
              }
    print(header)

    r = requests.get(req.url, headers=header)
    content = r.content
    response = content.decode("UTF-8")
    print(response)




