"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getTaskInstanceLog_V2_1
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Get the log of a specified task instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/get_task_instance_log.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getTaskInstanceLog_V2_1(accessKey, secretKey, orgId, url, userId, taskInstId, maxLength):
    accessURL = url + "/batch-processing-service/v2.1/taskInstances"
    params = {"action": "getLog", "orgId": orgId, "userId": userId, "taskInstId": taskInstId, "maxLength": maxLength}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
