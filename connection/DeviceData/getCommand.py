"""
 * Copyright (C), 2015-2021, Envision
 * FileName: GetCommand
 * Author:  Dylan Yeo
 * Date:    26/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/get_command.html
 * refer to the resources/ConnectServiceModel/DeviceData/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 26/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def GetCommand_assetId(accessKey, secretKey, orgId, url, assetId, commandId):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "get", "orgId": orgId, "assetId": assetId, "commandId": commandId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def GetCommand_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey, commandId):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "get", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey, "commandId": commandId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

