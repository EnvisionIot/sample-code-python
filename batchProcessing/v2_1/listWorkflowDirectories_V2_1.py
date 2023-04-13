"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listWorkflowDirectories_V2_1
 * Author:  Dylan Yeo
 * Date:    10/03/22
 * Description: Get all the content in the workflow directory of the current organization (OU), including workflow files and sub-directories
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/list_workflow_dirs.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def listWorkFlowDirectories_V2_1(accessKey, secretKey, orgId, url, userId):
    accessURL = url + "/batch-processing-service/v2.1/directories"
    params = {"action": "listWorkFlowDirs", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

