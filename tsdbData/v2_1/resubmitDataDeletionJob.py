"""
 * Copyright (C), 2015-2021, Envision
 * FileName: resubmitDataDeletionJob
 * Author:  Dylan Yeo
 * Date:    03/03/22
 * Description: When a data deletion job fails, resubmit the job by specifying the data deletion job ID
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/resubmit_data_deletion_job.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def resubmitDataDeletionJob(accessKey, secretKey, orgId, url, jobId):
    accessURL = url + '/tsdb-service/v2.1/data/resubmit'
    params = {"orgId": orgId,
              "JobId": jobId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, method="PUT")
    print(response)
