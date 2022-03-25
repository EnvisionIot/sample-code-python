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

def sendTemplateMail(accessKey, secretKey, orgId, url):
    accessURL = url + "/notification-center-service/v2.0/template/email"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"variables": "",
            "templateCode": "AMC_MAIL_EN_STEP_NOTIFI",
            "toAddresses": "dylan.yeo@envision-digital.com",
            "senderCode": "operator@support.envisioniot.com",
            # optional parameters
            # "ccAddresses": "",
            # "priority": "",
            # "extras": ""
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
