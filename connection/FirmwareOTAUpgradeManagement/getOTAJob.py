"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getOTAJob
 * Author:  Dylan Yeo
 * Date:    21/2/22
 * Description: Get the details of an OTA job
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/get_ota_job.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareOTAUpgradeManagement
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getOTAJob(accessKey, secretKey, orgId, url, jobId):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "get", "orgId": orgId, "jobId": jobId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


