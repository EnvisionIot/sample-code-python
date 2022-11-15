"""
 * Copyright (C), 2015-2021, Envision
 * FileName: sendTemplateSMS
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: This interface for operators by specified text messages sent a particular template text messages, custom template text of parameters for the caller to replace part of the text operators can increase the message signature, before the body of the request is sent successfully, SMS sending requests will be put into the message queue, users can receive a eventId, follow-up can be sent via eventId view the actual results
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/notification-mgmt-api/en/2.3.0/api_reference/send_template_sms.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

variables = {"SUMMARY": "Summary Content",
             "START_TIME": "Time",
             "STATUS": "Status",
             "DETAIL": "Details"}

def sendTemplateSMS(accessKey, secretKey, orgId, url):
    accessURL = url + "/notification-center-service/v2.0/template/sms"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"variables": variables,
            "templateCode": "AXS_SMS_CN_DAILY_REPORT",
            "phones": [{"area": "65",
                        "number": "91603123"}],
            "tunnelCode": "NOTICE_NEXMO",
            # optional parameters
            # "signatureCode": "",
            # "priority": "P2",
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
