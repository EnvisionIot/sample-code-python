"""
 * Copyright (C), 2015-2021, Envision
 * FileName: sendTemplateMail
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: Log in to EnOS
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/notification-mgmt-api/en/2.3.0/api_reference/send_template_mail.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def sendTemplateMail(accessKey, secretKey, url):
    accessURL = url + "/notification-center-service/v2.0/template/email"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"variables": 0,
            "templateCode": "",
            "toAddresses": "",
            "senderCode": ""
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
