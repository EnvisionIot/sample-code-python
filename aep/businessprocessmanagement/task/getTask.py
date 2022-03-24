"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getTask
 * Author:  Dylan Yeo
 * Date:    23/03/22
 * Description: Get the details of a task
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/task/get_task.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getTask(accessKey, secretKey, url, accessToken, taskId):
    accessURL = url + "/enos-bpm-service/v2.0/work/tasks"
    params = {"taskId": taskId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)