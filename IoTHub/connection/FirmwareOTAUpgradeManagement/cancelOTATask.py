"""
 * Copyright (C), 2015-2021, Envision
 * FileName: cancelOTATask
 * Author:  Dylan Yeo
 * Date:    22/2/22
 * Description: Cancel OTA tasks under the specified OTA job
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/cancel_ota_task.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareOTAUpgradeManagement
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def cancelOTATask(accessKey, secretKey, orgId, url, deviceKeys, jobId):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "cancelTask", "orgId": orgId, "jobId": jobId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"deviceKeys":deviceKeys
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


