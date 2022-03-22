"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getJobDetails
 * Author:  Dylan Yeo
 * Date:    08/03/22
 * Description: Get the detailed information of a data reading job or a data writing job
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/get_job_details.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getJobDetails(accessKey, secretKey, orgId, url, channelId, jobId):
    accessURL = url + '/data-federation/v2.0/channels/read/' + channelId + '/jobs/' + jobId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


