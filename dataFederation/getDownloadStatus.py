"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getDownloadStatus
 * Author:  Dylan Yeo
 * Date:    09/03/22
 * Description: Get the status of a file download task
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/download_status.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getDownloadStatus(accessKey, secretKey, orgId, url, channelId, taskId):
    accessURL = url + "/data-federation/v2.0/channels/read/" + channelId + "/download/" + taskId + "/status"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


