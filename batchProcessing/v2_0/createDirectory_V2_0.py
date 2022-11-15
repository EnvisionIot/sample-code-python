"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createDirectory_V2_1
 * Author:  Dylan Yeo
 * Date:    10/03/22
 * Description: Create a directory
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/create_directory.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createDirectory_V2_0(accessKey, secretKey, orgId, url, userId, parentId, dirName):
    accessURL = url + "/dataflow-batch-service/v2.0/directories"
    params = {"action": "create", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"parentId": parentId,
          "dirName" :dirName,
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

