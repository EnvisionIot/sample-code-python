"""
 * Copyright (C), 2015-2021, Envision
 * FileName: RevokeCertficate
 * Author:  Dylan Yeo
 * Date:    27/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/delete_cert.html
 * refer to the resources/IoTHub/ConnectServiceModel/Certificate
 *
 * @author dylan.yeo
 * @create 27/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def RevokeCertificate_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.0/certificates'
    params = {"action": "revoke", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "certSn": 54367,
        "reason": 4,
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def RevokeCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, deviceKey):
    accessURL = url + '/connect-service/v2.0/certificates'
    params = {"action": "revoke", "orgId": orgId, "productKey": ProductKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "certSn": 54376,
        "reason": 9,
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)