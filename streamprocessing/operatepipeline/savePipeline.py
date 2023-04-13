"""
 * Copyright (C), 2015-2021, Envision
 * FileName: savePipeline
 * Author:  Dylan Yeo
 * Date:    24/02/22
 * Description: Save the configuration of a specific stream processing pipeline
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/save_pipeline.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def savePipeline(accessKey, secretKey, orgId, url, pipelineId):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + pipelineId
    params = {"action": "save", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"version": "0.1.0",
          "name": "Python_PipelineTest2",
          "templateType": "5",
          "templateName": "Time Window Aggregation",
          "messageChannel": "0",
          "pipelineJson": {
              "piDetail": True,
              "points": [{
                  "minValue": "0",
                  "outputPointId": "Python_Demo_Model :: Int_MeasurementPoint",
                  "exceptionPolicy": "1",
                  "maxValue": "",
                  "minValueInclude": True,
                  "piDetailWindowSize": "FIVE_MINUTE",
                  "maxValueInclude": False,
                  "inputPointId": "Python_Demo_Model :: Int_MeasurementPoint",
                  "detailOutputPointId": "Python_Demo_Model :: Int_MeasurementPoint"
              }]
          }
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def createPipeline(accessKey, secretKey, orgId, url):
    accessURL = url + '/streaming/v2.0/streaming/pipeline/' + "null"
    params = {"action": "save", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"version": "0.1.0",
          "name": "Python_PipelineTest2",
          "templateType": "5",
          "templateName": "Time Window Aggregation",
          "messageChannel": "0",
          "pipelineJson": {
              "piDetail": True,
              "points": [{
                  "minValue": "0",
                  "outputPointId": "Python_Demo_Model :: Int_MeasurementPoint",
                  "exceptionPolicy": "1",
                  "maxValue": "",
                  "minValueInclude": True,
                  "piDetailWindowSize": "FIVE_MINUTE",
                  "maxValueInclude": False,
                  "inputPointId": "Python_Demo_Model :: Int_MeasurementPoint",
                  "detailOutputPointId": "Python_Demo_Model :: Int_MeasurementPoint"
              }]
          }
        }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
