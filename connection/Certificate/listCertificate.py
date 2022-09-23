"""
 * Copyright (C), 2015-2021, Envision
 * FileName: ListCertificate
 * Author:  Dylan Yeo
 * Date:    27/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/list_cert.html
 * refer to the resources/IoTHub/ConnectServiceModel/Certificate
 *
 * @author dylan.yeo
 * @create 27/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def ListCertificate_assetId(accessKey, secretKey, orgId, url, assetId):
    accessURL = url + '/connect-service/v2.0/certificates'
    params = {"action": "list", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def ListCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, deviceKey):
    accessURL = url + '/connect-service/v2.0/certificates'
    params = {"action": "list", "orgId": orgId, "productKey": ProductKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)