"""
 * Copyright (C), 2015-2021, Envision
 * FileName: stopPipeline
 * Author:  Dylan Yeo
 * Date:    24/02/22
 * Description: Stop a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/stop_pipeline.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def stopPipeline(accessKey, secretKey, orgId, url, pipelineId):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"action": "stop", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)



