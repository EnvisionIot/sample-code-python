"""
 * Copyright (C), 2015-2021, Envision
 * FileName: completeTask
 * Author:  Dylan Yeo
 * Date:    23/03/22
 * Description: Claim a task
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/task/claim_task.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def completeTask(accessKey, secretKey, url, accessToken):
    accessURL = url + "/enos-bpm-service/v2.0/work/tasks/complete"
    params = {"taskId": "1e105814-aa91-11ec-ad0f-8e1ac2659f4c"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"values": {"SingleLine_Variable":"SingleLine_Answer"},
            "outcome": "outcome?"}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, headers=header)
    print(response)
