"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listDeviceCurrentFirmware
 * Author:  Dylan Yeo
 * Date:    18/2/22
 * Description: List the firmware versions of all devices under the specified product
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/list_firmware_version.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareManagement/Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 18/2/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def listDeviceCurrentFirmware(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "listVersion", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
