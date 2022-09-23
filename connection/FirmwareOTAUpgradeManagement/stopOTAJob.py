"""
 * Copyright (C), 2015-2021, Envision
 * FileName: stopOTAJob
 * Author:  Dylan Yeo
 * Date:    21/2/22
 * Description: Stop an OTA job
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/stop_ota_job.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareOTAUpgradeManagement
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def stopOTAJob(accessKey, secretKey, orgId, url, jobId):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "stop", "orgId": orgId, "jobId": jobId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


