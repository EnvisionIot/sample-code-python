"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createDownloadRequest
 * Author:  Dylan Yeo
 * Date:    09/03/22
 * Description: Create a file download task
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/download_request.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createDownloadRequest(accessKey, secretKey, orgId, url, channelId, taskName, sourceName, querySql, filePackageName, files=None, callbackURL=None, selfDefineQueuePara=None):
    accessURL = url + "/data-federation/v2.0/channels/read/" + channelId + "/download-request"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"taskName":taskName,
          "sourceName":sourceName,
          "querySql": querySql,
          "filePackageName": filePackageName,
          "files": files,
          "callbackURL": callbackURL,
          "selfDefineQueuePara": selfDefineQueuePara
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        taskId= response['data']['taskId']
    except:
        taskId= str(None)

    return taskId
