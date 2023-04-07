"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listChannels
 * Author:  Dylan Yeo
 * Date:    08/03/22
 * Description: Start or stop a read channel or write channel
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/operate_channel.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def operateChannels(accessKey, secretKey, orgId, url, channelId, action):
    accessURL = url + '/data-federation/v2.0/channels/' + channelId
    params = {"orgId": orgId, "action": action}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def operateChannels_resource(accessKey, secretKey, orgId, url, channelId, action, resourceId="", resourceConfig="",ifMultiResourceAnalysis=None):
    accessURL = url + '/data-federation/v2.0/channels/' + channelId
    params = {"orgId": orgId, "action": action}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"resource": {"resourceId":resourceId,
                       "resourceConfig":resourceConfig,
                       "ifMultiResourceAnalysis":ifMultiResourceAnalysis}}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


