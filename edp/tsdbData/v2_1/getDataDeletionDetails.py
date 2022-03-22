"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getDataDeletionDetails
 * Author:  Dylan Yeo
 * Date:    03/03/22
 * Description: Get the running result details of data deletion jobs (by specifying data deletion job ID)
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_data_deletion_details.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getDataDeletionDetails(accessKey, secretKey, orgId, url, queryId):
    accessURL = url + '/tsdb-service/v2.1/data/delete-detail'
    params = {"orgId": orgId,
              "queryId": queryId,
              "pageSize": 4,
              "pageNo": 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
