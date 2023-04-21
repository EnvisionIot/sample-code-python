"""
 * Copyright (C), 2015-2021, Envision
 * FileName: resetPipelineOffset
 * Author:  Dylan Yeo
 * Date:    25/02/22
 * Description: Reset the Kafka Offset of a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/reset_pipeline_offset.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def resetPipelineOffset(accessKey: str, secretKey: str, orgId: str, url: str, pipelineId: str):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId + '/offset'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, method='POST')
    print(response)
    return response


