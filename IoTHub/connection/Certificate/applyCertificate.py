"""
 * Copyright (C), 2015-2021, Envision
 * FileName: ApplyCertificate
 * Author:  Dylan Yeo
 * Date:    27/1/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/apply_cert.html
 * refer to the resources/IoTHub/ConnectServiceModel/Certificate
 *
 * @author dylan.yeo
 * @create 27/1/22
 * @since --
"""

import poseidon.poseidon
from requests.models import PreparedRequest

#assetId for Python_Demo_Gateway = zhD6Kpfs

def ApplyCertificate_assetId(accessKey, secretKey, orgId, url, assetId, csr):
    accessURL = url + '/connect-service/v2.0/certificates'
    params = {"action": "apply", "orgId": orgId, "assetId": assetId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={
        "csr": csr,
        "validDay": 1,
        "issueAuthority": "RSA"
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def ApplyCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, deviceKey, csr):
    accessURL = url + '/connect-service/v2.0/certificates'
    params = {"action": "apply", "orgId": orgId, "productKey": ProductKey, "deviceKey": deviceKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "csr": csr,
        "validDay": 100,
        "issueAuthority": "RSA"
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url,body)
    print(response)