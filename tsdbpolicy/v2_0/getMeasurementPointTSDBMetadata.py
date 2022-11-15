"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getMeasurementPointTSDBMetadata
 * Author:  Dylan Yeo
 * Date:    28/02/22
 * Description: Get the TSDB storage policy corresponding to the model measurement point. A measurement point may have multiple storage policies, depending on its data type and usage. This API returns all the TSDB storage policy metadata in the current organization for the specified measurement point
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.0/get_points_tsdb_meta_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getMeasurementPointTSDBMetadata(accessKey, secretKey, orgId, url, modelIds):
    accessURL = url + '/tsdb-policy/v2.0/policies'
    params = {"orgId": orgId, "modelIds": modelIds}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getMeasurementPointTSDBMetadata_measurepoints(accessKey, secretKey, orgId, url, modelIds, measurepoints):
    accessURL = url + '/tsdb-policy/v2.0/policies'
    params = {"orgId": orgId, "modelIds": modelIds, "measurepoints": measurepoints}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)