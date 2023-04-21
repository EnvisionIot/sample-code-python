"""
 * Copyright (C), 2015-2021, Envision
 * FileName: savePipeline
 * Author:  Dylan Yeo
 * Date:    24/02/22
 * Description: Save the configuration of a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/save_pipeline.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def savePipeline(accessKey: str, secretKey: str, orgId: str, url: str, pipelineId: str, 
        version: str, name: str, templateType: int, templateName: str, messageChannel: int, pipelineJson: str):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"action": "save", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"version": version,
          "name": name,
          "templateType": templateType,
          "templateName": templateName,
          "messageChannel": messageChannel,
          "pipelineJson": pipelineJson
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, method='POST')
    print(response)
    return response