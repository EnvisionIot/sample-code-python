"""
 * Copyright (C), 2015-2021, Envision
 * FileName: retryOTATask
 * Author:  Dylan Yeo
 * Date:    22/2/22
 * Description: Retry OTA tasks under the specified OTA job
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/retry_ota_task.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareOTAUpgradeManagement
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def retryOTATask(accessKey, secretKey, orgId, url, deviceKeys, jobId):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "retryTask", "orgId": orgId, "jobId": jobId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"deviceKeys":deviceKeys
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


