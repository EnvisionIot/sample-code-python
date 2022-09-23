"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UploadEvents
 * Author:  Dylan Yeo
 * Date:    3/2/22
 * Description: Upload the event data of a device or logic asset, including file-type data
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/upload_integration_events.html
 * refer to the resources/IoTHub/ConnectServiceModel/HTTPMessageIntegration
 *
 * @author dylan.yeo
 * @create 3/2/22
 * @since --
"""

import requests
from requests.models import PreparedRequest
from requests_toolbelt.multipart.encoder import MultipartEncoder
import time

url = "https://iot-http-integration-ppe1.envisioniot.com"

currentTime = str(round(time.time()*1000.0))

def UploadEvents_assetId(orgId, token, assetId):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postEvent", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = MultipartEncoder(fields={
        "Content-Disposition": "form-data",
        "enos-message": "{'method': 'integration.event.post', "
                        "'version': '1.1', " #'id': 123, 
                        "'params': [{'assetId':" + assetId + ", "
                                     "'time':" + currentTime + ", "
                                     "'events': {'tempBelow10': {'temperature': 12}"
                                     
                                                "}"
                                     "}]"
                        "}"}
        )
    print(body)

    header = {"apim-accesstoken": token,
              "Content-Type": body.content_type
              }
    print(header)

    r = requests.post(req.url, headers=header, data=body)
    content = r.content
    response = content.decode("ASCII")
    print(response)


def UploadEvents_Keys(orgId, token, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postEvent", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = MultipartEncoder(fields={
        "Content-Disposition": "form-data",
        "enos-message": "{'method': 'integration.event.post', "
                        "'version': '1.1', "  # 'id': 123, 
                        "'params': [{'productKey':" + productKey + ", "
                                    "'deviceKey':" + deviceKey + ", "
                                    "'time':" + currentTime + ", "
                                    "'events': {'tempBelow10': {'temperature': 9}"

                                                "}"
                                    "}]"
                        "}"}
    )
    print(body)

    header = {"apim-accesstoken": token,
              "Content-Type": body.content_type
              }
    print(header)

    r = requests.post(req.url, headers=header, data=body)
    content = r.content
    response = content.decode("ASCII")
    print(response)





