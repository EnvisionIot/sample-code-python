"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listPipeline
 * Author:  Dylan Yeo
 * Date:    25/02/22
 * Description: Get the list of stream processing pipelines in the organization by pages
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/list_pipelines.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def listPipeline(accessKey, secretKey, orgId, url,):
    accessURL = url + '/streaming/v2.0/streaming/pipelines'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def listPipeline_optionalParameters(accessKey, secretKey, orgId, url):
    accessURL = url + '/streaming/v2.0/streaming/pipelines'
    params = {"orgId": orgId,
              "pageSize": "5",
              "pageNo": "1",
              "isSystem": False,
              "ifReleased": True}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
