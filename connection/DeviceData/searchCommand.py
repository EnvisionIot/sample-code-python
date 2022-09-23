"""
 * Copyright (C), 2015-2021, Envision
 * FileName: SearchCommand
 * Author:  Dylan Yeo
 * Date:    26/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_command.html
 * refer to the resources/ConnectServiceModel/DeviceData/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 26/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def SearchCommand_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "search", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "projection": ["commandId",
                       "orgId",
                       "productKey",
                       "deviceKey",
                       "assetId",
                       "createTime",
                       "createLocaltime",
                       "commandType",
                       "commandName",
                       "timeout",
                       "pendingTtl",
                       "state",
                       "tslIdentifier",
                       "inputData",
                       "outputData"],
        "pagination": {"pageNo": 1,
                       "pageSize": 50}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchCommand_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "search", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "projection": ["commandId",
                       "orgId",
                       "productKey",
                       "deviceKey",
                       "assetId",
                       "createTime",
                       "createLocaltime",
                       "commandType",
                       "commandName",
                       "timeout",
                       "pendingTtl",
                       "state",
                       "tslIdentifier",
                       "inputData",
                       "outputData"],
        "pagination": {"pageNo": 1,
                       "pageSize": 50},
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, assetId, expression):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "search", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": expression,
        "pagination": {"pageNo": 1,
                       "pageSize": 10}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, productKey, deviceKey, expression):
    accessURL = url + '/connect-service/v2.1/commands'
    params = {"action": "search", "orgId": orgId, "productKey": productKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": expression,
        "pagination": {"pageNo": 1,
                       "pageSize": 10}
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
