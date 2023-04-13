"""
 * Copyright (C), 2015-2021, Envision
 * FileName: closeActiveAlert
 * Author:  Dylan Yeo
 * Date:    16/02/22
 * Description: Close an active alert. A closed active alert will become a history alert
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/alert-api/en/2.3.0/close_active_alert.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
from datetime import datetime
import time

current_time = round(time.time()*1000)
current_local = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def closeActiveAlert(accessKey, secretKey, orgId, url, eventId):
    accessURL = url + '/event-service/v2.1/active-alerts'
    params = {"action": "close", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"eventId": eventId,
          "recoverTime": current_time,
          #optional parameters
          "localRecoverTime": current_local,
          "recoverReason": "Your_Recover_Reason"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


