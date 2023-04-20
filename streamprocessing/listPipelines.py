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

def listPipelines(accessKey: str, secretKey: str, orgId: str, url: str, pageSize: int=10, pageNo: int=1, isSystem: bool=False, ifReleased: bool=False):
    accessURL = url + '/streaming/v2.0/streaming/pipelines'
    params = {"orgId": orgId,
              "pageSize": pageSize,
              "pageNo": pageNo,
              "isSystem": isSystem,
              "ifReleased": ifReleased}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, method='GET')
    print(response)
    return response