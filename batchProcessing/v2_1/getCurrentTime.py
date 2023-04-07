"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getCurrentTime_V2_1
 * Author:  Dylan Yeo
 * Date:    11/03/22
 * Description: Get the current time of the server
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/get_current_time.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getCurrentTime(accessKey, secretKey, url):
    accessURL = url + "/batch-processing-service/v2.1/time"
    params = {"action": "getCurrentTime"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

