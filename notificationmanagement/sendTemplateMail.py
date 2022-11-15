"""
 * Copyright (C), 2015-2021, Envision
 * FileName: sendTemplateMail
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: This interface can send a specific template message through a designated mailbox. There are custom parameters in the template message that can be replaced by the caller. When the request is successfully sent, the message sending request will be put into a message queue, and the user can receive an eventId, through which the actual sending result can be viewed later
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/notification-mgmt-api/en/2.3.0/api_reference/send_template_mail.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

variables= {"USER": "User_Name",
            "CURRENT_STEP": "Current_Step",
            "NEXT_STEP": "Next_Step",
            "URL_LINK": "URL_LINK",
            "ORGANIZATION": "Org_Name",
            "SITE": "Site",
            "REMARK": "Insert_Remarks"}

def sendTemplateMail(accessKey, secretKey, orgId, url):
    accessURL = url + "/notification-center-service/v2.0/template/email"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"variables": variables,
            "templateCode": "AMC_MAIL_EN_STEP_NOTIFI",
            "toAddresses": ["dylan.yeo@envision-digital.com"],
            "senderCode": "EnOS_Cloud",
            # optional parameters
            # "ccAddresses": "",
            # "priority": "P2",
            # "extras": ""
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
