"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UploadMeasurementPoints
 * Author:  Dylan Yeo
 * Date:    3/2/22
 * Description: Upload the measurement point data of a device or logic asset, including file-type data
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/upload_integration_measurepoints.html
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

def UploadMeasurementPoints_assetId(orgId, token, assetId):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postMeasurepoint", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = MultipartEncoder(fields={
        "Content-Disposition": "form-data",
        "enos-message": "{'method': 'integration.measurepoint.post', "
                        "'version': '1.1', " #'id': 123, 
                        "'params': [{'assetId':" + assetId + ", "
                                     "'time':" + currentTime + ", "
                                     "'measurepoints': {'Int_Output':1000"
                                     
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


def UploadMeasurementPoints_Keys(orgId, token, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postMeasurepoint", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = MultipartEncoder(fields={
        "Content-Disposition": "form-data",
        "enos-message": "{'method': 'integration.measurepoint.post', "
                        "'version': '1.1', "  # 'id': 123, 
                        "'params': [{'productKey':" + productKey + ", "
                                    "'deviceKey':" + deviceKey + ", "
                                    "'time':" + currentTime + ", "
                                    "'measurepoints': {'Float_MeasurementPoint': 2.2"

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


def UploadMeasurementPoints(orgId, token, assetId, measurepoints, value, time):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postMeasurepoint", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = MultipartEncoder(fields={
        "Content-Disposition": "form-data",
        "enos-message": "{'method': 'integration.measurepoint.post', "
                        "'version': '1.1', "  # 'id': 123, 
                        "'params': [{'assetId':" + assetId + ", "
                                    "'time':" + time + ", "
                                    "'measurepoints': {" + measurepoints + ":" + value + "}"
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


