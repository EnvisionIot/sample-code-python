"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getPipelineOffsetAndLag
 * Author:  Dylan Yeo
 * Date:    25/02/22
 * Description: Get the Kafka Offset and Lag of a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/get_pipeline_offset_lag.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getPipelineOffsetAndLag(accessKey: str, secretKey: str, orgId: str, url: str, pipelineId: str):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId + '/offset-lag'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, method='GET')
    print(response)
    return response


