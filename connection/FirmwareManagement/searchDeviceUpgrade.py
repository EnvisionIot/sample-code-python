"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchDeviceUpgrade
 * Author:  Dylan Yeo
 * Date:    18/2/22
 * Description: Search for the firmware and upgrade status of the device based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_device_upgrade.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareManagement/Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 18/2/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def searchDeviceUpgrade(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "searchDeviceUpgrade", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"pagination": {"pageNo": 1,
                         "pageSize": 5,
    }}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchDeviceUpgrade_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "searchDeviceUpgrade", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"expression": expression
          }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
