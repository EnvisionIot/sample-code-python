"""
 * Copyright (C), 2015-2021, Envision
 * FileName: submitDataDeletionJob
 * Author:  Dylan Yeo
 * Date:    03/03/22
 * Description: Submit a data deletion job to delete the historical data of specified assets stored in TSDB
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/submit_data_deletion_job.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def submitDataDeletionJob(accessKey, secretKey, orgId, url, modelId, assetIds, pointId, startTime, endTime):
    accessURL = url + '/tsdb-service/v2.1/data/tsdb-delete'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointId": pointId,
            "startTime": startTime,
            "endTime": endTime
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    jobId=response['data']
    return jobId
