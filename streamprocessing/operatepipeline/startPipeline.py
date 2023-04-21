"""
 * Copyright (C), 2015-2021, Envision
 * FileName: startPipeline
 * Author:  Dylan Yeo
 * Date:    24/02/22
 * Description: Start a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/start_pipeline.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def startPipeline(accessKey: str, secretKey: str, orgId: str, url: str, pipelineId: str, 
        executionMode: int, kafkaRate: int, resourceConfig: dict):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"action": "start", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"executionMode": executionMode,
          "kafkaRate": kafkaRate,
          "resourceConfig": resourceConfig
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, method='POST')
    print(response)
    return response


