"""
 * Copyright (C), 2015-2021, Envision
 * FileName: cancelDownload
 * Author:  Dylan Yeo
 * Date:    09/03/22
 * Description: Cancel a file download task
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/cancel_download.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def cancelDownload(accessKey, secretKey, orgId, url, channelId, taskId):
    accessURL = url + "/data-federation/v2.0/channels/read/" + channelId + "/download/" + taskId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, method="DELETE")
    print(response)


