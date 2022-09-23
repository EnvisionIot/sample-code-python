"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchFirmwareFile
 * Author:  Dylan Yeo
 * Date:    18/2/22
 * Description: Search for firmware files under an OU based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_firmware.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareManagement/Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 18/2/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def searchFirmwareFile(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"pagination": {"pageNo": 1,
                         "pageSize": 5,
    }}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "search", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"expression": expression
          }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
