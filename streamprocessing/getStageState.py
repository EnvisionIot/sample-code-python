"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getStageState
 * Author:  Dylan Yeo
 * Date:    25/02/22
 * Description: Get the intermediate state data of a specified operator (stage) in a stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/get_stage_state.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getStageState(accessKey, secretKey, orgId, url, pipelineId, stageInstanceName, assetIds, pointIds):
    accessURL = url + '/streaming/v2.0/stage-state'
    params = {"action": "get", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"pipelineId": pipelineId,
          "stageInstanceName": stageInstanceName,
          "assetIds": assetIds,
          "pointIds": pointIds
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


