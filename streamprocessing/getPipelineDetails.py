"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getPipelineDetails
 * Author:  Dylan Yeo
 * Date:    25/02/22
 * Description: Get the details of a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/get_pipeline_details.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getPipelineDetails(accessKey, secretKey, orgId, url, pipelineId):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"orgId": orgId, "ifReleased": False}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


