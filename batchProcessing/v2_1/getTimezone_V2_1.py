"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getTimezone_V2_1
 * Author:  Dylan Yeo
 * Date:    14/03/22
 * Description: Get the timezone where the server is located
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/get_time_zone.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getTimezone_V2_1(accessKey, secretKey, url):
    accessURL = url + "/batch-processing-service/v2.1/time"
    params = {"action": "getTimeZone"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

