"""
 * Copyright (C), 2015-2021, Envision
 * FileName: GetEvent
 * Author:  Dylan Yeo
 * Date:    26/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/get_event.html
 * refer to the resources/ConnectServiceModel/DeviceData/model_Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 26/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

eventId = "202201241563b1c05bdb379928d4e1ae082aca37"


def GetEvent(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "get", "orgId": orgId, "eventId": eventId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def GetEvent_ResolveName(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/events'
    params = {"action": "get", "orgId": orgId, "eventId": eventId, "resolveName": "true"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


