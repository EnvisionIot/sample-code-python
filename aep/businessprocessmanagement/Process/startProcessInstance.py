"""
 * Copyright (C), 2015-2021, Envision
 * FileName: startProcessInstance
 * Author:  Dylan Yeo
 * Date:    22/03/22
 * Description: Start a new process instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/start_process_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def startProcessInstance(accessKey, secretKey, url, accessToken):
    accessURL = url + "/enos-bpm-service/v2.0/work/process-instances"
    params = {"processInstanceId": "705061a4-a9ba-11ec-ad0f-8e1ac2659f4c"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
