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

    body = {"processDefinitionId": "81dd4fd7-aa6b-11ec-ad0f-8e1ac2659f4c",
            "values": {"Key1":"Value1"},
            # Optional Parameters
            "name": "API_Python_ProcessInstance",
            #"formId": "",
            #"outcome": ""
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
