"""
 * Copyright (C), 2015-2021, Envision
 * FileName: GetDeviceStatistics
 * Author:  Dylan Yeo
 * Date:    21/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/get_device_stats.html
 * refer to the resources/IoTHub/ConnectServiceModel/Device/model_python_4attri_model.json
 *
 * @author dylan.yeo
 * @create 21/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def GetDeviceStatistics(accessKey, secretKey, orgId, url):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "getStats", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def GetDeviceStatistics_ProductKey(accessKey, secretKey, orgId, url, productKey):
    accessURL = url + '/connect-service/v2.1/devices'
    params = {"action": "getStats", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
