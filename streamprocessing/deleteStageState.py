"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteStageState
 * Author:  Dylan Yeo
 * Date:    25/02/22
 * Description: Delete the intermediate state data of a specified operator (stage) in a stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/delete_stage_state.html

"""

import poseidon.poseidon
from requests.models import PreparedRequest

def deleteStageState(accessKey: str, secretKey: str, orgId: str, url: str, pipelineId: str, stageInstanceName: str, assetIds: str, pointIds: str):
    accessURL = url + '/streaming/v2.0/stage-state'
    params = {"action": "delete", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"pipelineId": pipelineId,
          "stageInstanceName": stageInstanceName,
          "assetIds": assetIds,
          "pointIds": pointIds
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, method='POST')
    print(response)
    return response


