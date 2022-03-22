"""
 * Copyright (C), 2015-2021, Envision
 * FileName: pausePipeline
 * Author:  Dylan Yeo
 * Date:    24/02/22
 * Description: Pause a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/pause_pipeline.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def pausePipeline(accessKey, secretKey, orgId, url, pipelineId):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"action": "pause", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)



