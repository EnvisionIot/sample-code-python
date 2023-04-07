"""
 * Copyright (C), 2015-2021, Envision
 * FileName: triggerFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    14/03/22
 * Description: Manually trigger a workflow schedule
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/trigger_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def triggerFlow(accessKey, secretKey, orgId, url, userId, flowId, triggerTime):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "trigger", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"flowId": flowId,
            "triggerTime": triggerTime
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




