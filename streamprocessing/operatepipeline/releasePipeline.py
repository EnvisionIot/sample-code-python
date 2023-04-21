"""
 * Copyright (C), 2015-2021, Envision
 * FileName: releasePipeline
 * Author:  Dylan Yeo
 * Date:    24/02/22
 * Description: Release a specific stream processing pipeline online
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/release_pipeline.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def releasePipeline(accessKey: str, secretKey: str, orgId: str, url: str, pipelineId: str):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"action": "release", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, method='POST')
    print(response)
    return response



