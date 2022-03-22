"""
 * Copyright (C), 2015-2021, Envision
 * FileName: writeMessage
 * Author:  Dylan Yeo
 * Date:    08/03/22
 * Description: Write message to data source through a specified channel
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/write_message.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def writeMessage(accessKey, secretKey, orgId, url, channelId, dataSourceName, data, sync):
    accessURL = url + '/data-federation/v2.0/channels/write/' + channelId + "/msg"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"dataSourceName": dataSourceName,
            "data": data,
            "sync": sync
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


