"""
 * Copyright (C), 2015-2021, Envision
 * FileName: writeChunkFile
 * Author:  Dylan Yeo
 * Date:    09/03/22
 * Description: Write file chunks to data source through a specified channel
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/write_chunk_file.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def writeChunkFile(accessKey, secretKey, orgId, url, channelId, dataSourceName, fileName, totalSize, chunkOffset, chunkSize, chunkData):
    accessURL = url + '/data-federation/v2.0/channels/write/' + channelId + "/chunk-file"
    params = {"orgId": orgId, "dataSourceName": dataSourceName}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"fileName": fileName,
            "totalSize": totalSize,
            "chunkOffset": chunkOffset,
            "chunkSize": chunkSize,
            "chunkData": chunkData
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


