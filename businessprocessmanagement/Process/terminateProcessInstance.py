"""
 * Copyright (C), 2015-2021, Envision
 * FileName: terminateProcessInstance
 * Author:  Dylan Yeo
 * Date:    23/03/22
 * Description: Terminate a process instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/terminate_process_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def terminateProcessInstance(accessKey, secretKey, url, accessToken, processInstanceId):
    accessURL = url + "/enos-bpm-service/v2.0/work/process-instances"
    params = {"action": "delete", "processInstanceId": processInstanceId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"deleteReason": "YourDeleteReason"}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
