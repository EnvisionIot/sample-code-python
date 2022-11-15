"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listJobs
 * Author:  Dylan Yeo
 * Date:    08/03/22
 * Description: Get the data reading jobs or data writing jobs of a specified channel
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/list_jobs.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def listJobs(accessKey, secretKey, orgId, url, channelId):
    accessURL = url + '/data-federation/v2.0/channels/read/' + channelId + '/jobs'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


