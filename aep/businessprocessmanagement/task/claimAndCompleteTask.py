"""
 * Copyright (C), 2015-2021, Envision
 * FileName: claimAndCompleteTask
 * Author:  Dylan Yeo
 * Date:    23/03/22
 * Description: Claim a task
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/task/claim_and_complete_task.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def claimAndCompleteTask(accessKey, secretKey, url, accessToken, taskId):
    accessURL = url + "/enos-bpm-service/v2.0/work/tasks/" + taskId + "/claim-complete"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"values": {"SingleLine_Variable":"SingleLine_AnswerOnAPI"},
            "outcome": "Key"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
