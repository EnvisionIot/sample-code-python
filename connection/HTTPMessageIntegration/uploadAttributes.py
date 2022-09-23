"""
 * Copyright (C), 2015-2021, Envision
 * FileName: UploadAttributes
 * Author:  Dylan Yeo
 * Date:    3/2/22
 * Description: Upload the attribute data of a device or logic asset, including file-type data
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/upload_integration_attributes.html
 * refer to the resources/IoTHub/ConnectServiceModel/HTTPMessageIntegration
 *
 * @author dylan.yeo
 * @create 3/2/22
 * @since --
"""
import os
import pathlib
import sys

import requests
from requests.models import PreparedRequest
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://iot-http-integration-ppe1.envisioniot.com"

def UploadAttributes_assetId(orgId, token, assetId):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postAttribute", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    filepath = pathlib.Path(sys.path[1]) / "resources/IoTHub/ConnectServiceModel/HttpMessageIntegration/UploadFileSample.txt"

    file = open(filepath, 'rb')
    filesize = os.path.getsize(filepath)

    body = MultipartEncoder(fields={
        'Content-Disposition': 'form-data',
        'enos-message': """{'method': 'integration.attribute.post', 'id': 123, 'version': '1.1', 
                    'params': [{'assetId': 'G5M8Ojhd', 'attributes': {'Int_Attribute': 1, 'File_Attribute':'local://UploadFileSample.txt'}}],
                    'files': { 
                        'UploadFileSample.txt': {
                              'featureId': 'File_Attribute',
                              'originalFilename': 'UploadFileSample.txt',
                                'fileExt': '.txt',
                              'assetId' : 'G5M8Ojhd' ,
                              'md5': 'aa8ea05bdbcbadfcda7300c65c40859f',
                              'fileLength': 658
                            }
                            }
                    }""",
        'enos-file': ('UploadFileSample.txt', file, 'text/plain')
    }

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


def UploadAttributes_Keys(orgId, token, productKey, deviceKey):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postAttribute", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    filepath = pathlib.Path(sys.path[1]) / "resources/IoTHub/ConnectServiceModel/HttpMessageIntegration/UploadFileSample.txt"

    file = open(filepath, 'rb')
    filesize = os.path.getsize(filepath)

    body = MultipartEncoder(fields={
        'Content-Disposition': 'form-data',
        'enos-message': """{'method': 'integration.attribute.post', 'id': 123, 'version': '1.1',
                        'params': [{'productKey': '4kZqiPoC','deviceKey': 'RqMa4xiwqo', 'attributes': {'Int_Attribute': 1, 'File_Attribute':'local://SampleFileAttributes.txt'}}],
                        'files': { 
                            'SampleFileAttributes.txt': {
                                  'featureId': 'File_Attribute',
                                  'originalFilename': 'UploadFileSample.txt',
                                  'fileExt': '.txt',
                                  'productKey': '4kZqiPoC','deviceKey': 'RqMa4xiwqo',
                                  
                                  'fileLength': 658
                                }
                                }
                        }""",
        'enos-file': ('SampleFileAttributes.txt', file, 'text/plain')
    }
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


def UploadAttributes_multifiles(orgId, token, assetId):
    accessURL = url + '/connect-service/v2.1/integration'
    params = {"action": "postAttribute", "orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    filepath = pathlib.Path(sys.path[1]) // "resources/IoTHub/ConnectServiceModel/HttpMessageIntegration/UploadFileSample.txt"
    filepath2 = pathlib.Path(sys.path[1]) / "resources/ConnectServiceModel/HttpMessageIntegration/SampleFileAttributes.txt"

    file = open(filepath, 'rb')
    file2 = open(filepath2, 'rb')
    filesize = os.path.getsize(filepath)

    body = MultipartEncoder(fields={
        'Content-Disposition': 'form-data',
        'enos-message': """{'method': 'integration.attribute.post', 'id': 123, 'version': '1.1', 
                    'params': [{'assetId': 'G5M8Ojhd', 'attributes': {'Int_Attribute': 1, 'File_Attribute':'local://UploadFileSample.txt'}},
                               {'assetId': 'Re2qPON3', 'attributes': {'Int_Attribute': 1, 'File_Attribute':'local://SampleFileAttributes.txt'}}
                    ],
                    'files': { 
                        'UploadFileSample.txt': {
                              'featureId': 'File_Attribute',
                              'originalFilename': 'UploadFileSample.txt',
                                'fileExt': '.txt',
                              'assetId' : 'G5M8Ojhd' ,
                              
                              'fileLength': 658
                            },
                        'SampleFileAttributes.txt': {
                              'featureId': 'File_Attribute',
                              'originalFilename': 'SampleFileAttributes.txt',
                                'fileExt': '.txt',
                              'assetId' : 'Re2qPON3' ,
                              
                              'fileLength': 23
                            }    
                            }
                    }""",
        'enos-file': ('UploadFileSample.txt', file,'text/plain') #still cant upload multiple files


    }

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