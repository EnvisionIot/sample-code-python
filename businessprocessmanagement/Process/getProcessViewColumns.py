"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getProcessViewColumns
 * Author:  Dylan Yeo
 * Date:    22/03/22
 * Description: Get the information of process view columns
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/get_process_view_columns.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getProcessViewColumns(accessKey, secretKey, url, accessToken, displayViewKey):
    accessURL = url + "/enos-bpm-service/v2.0/work/display-view/" + displayViewKey +"/columns"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
