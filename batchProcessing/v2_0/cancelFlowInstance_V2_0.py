"""
 * Copyright (C), 2015-2021, Envision
 * FileName: cancelFlowInstance_V2_0
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Cancel the running of a specified workflow instance
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.0/cancel_flow_instance.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def cancelFlowInstance_V2_0(accessKey, secretKey, orgId, url, userId, flowInstanceId):
    accessURL = url + "/dataflow-batch-service/v2.0/flowInstances"
    params = {"action": "cancel", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"flowInstId": flowInstanceId
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

