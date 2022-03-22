"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchOTATask
 * Author:  Dylan Yeo
 * Date:    21/2/22
 * Description: Search for OTA tasks based on the search criteria
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/search_ota_job.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareOTAUpgradeManagement
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def searchOTATask(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "searchTask", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"pagination": {"pageNo": 1,
                         "pageSize": 5}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchOTATask_Expression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "searchTask", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)