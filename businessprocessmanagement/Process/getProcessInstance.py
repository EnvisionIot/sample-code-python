"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getProcessInstance
 * Author:  Dylan Yeo
 * Date:    22/03/22
 * Description: Get the details of a process instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/get_process_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getProcessInstance(accessKey, secretKey, url, accessToken, processInstanceId):
    accessURL = url + "/enos-bpm-service/v2.0/work/process-instances"
    params = {"processInstanceId": processInstanceId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
