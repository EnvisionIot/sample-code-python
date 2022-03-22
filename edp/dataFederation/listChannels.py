"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listChannels
 * Author:  Dylan Yeo
 * Date:    08/03/22
 * Description: Get the list of channels (Read and Write) to which the application is authorized
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/list_channels
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def listChannels(accessKey, secretKey, orgId, url, channelType=None):
    accessURL = url + '/data-federation/v2.0/channels'
    params = {"orgId": orgId, "channelType": channelType}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


