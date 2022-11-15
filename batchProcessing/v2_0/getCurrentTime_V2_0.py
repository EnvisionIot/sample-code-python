"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getCurrentTime_V2_0
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Get the current time of the server
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.0/get_current_time.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getCurrentTime_V2_0(accessKey, secretKey, url):
    accessURL = url + "/dataflow-batch-service/v2.0/time"
    params = {"action": "getCurrentTime"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

