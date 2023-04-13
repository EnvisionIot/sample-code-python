"""
 * Copyright (C), 2015-2021, Envision
 * FileName: startProcessInstance
 * Author:  Dylan Yeo
 * Date:    23/03/22
 * Description: Start a new process instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/start_process_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def startProcessInstance(accessKey, secretKey, url, accessToken):
    accessURL = url + "/enos-bpm-service/v2.0/work/process-instances"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"processDefinitionId": "312844b2-ab3d-11ec-8df5-120e04f331d8",
            "values": {"Key":"Value"},
            # Optional Parameters
            "name": "Python_ProcessInstance_ByAPI",
            #"formId": "",
            "outcome": "Key"
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
