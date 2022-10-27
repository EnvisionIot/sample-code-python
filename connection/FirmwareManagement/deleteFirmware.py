"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteFirmwareFile
 * Author:  Dylan Yeo
 * Date:    18/2/22
 * Description: Delete a firmware
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/delete_firmware.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareManagement/Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 18/2/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def deleteFirmwareFile(accessKey, secretKey, orgId, url, firmwareId):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "delete", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
