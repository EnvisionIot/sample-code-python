"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createFirmwareFile
 * Author:  Dylan Yeo
 * Date:    18/2/22
 * Description:
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/create_firmware.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareManagement/Python_Demo_Model.json
 *
 * @author dylan.yeo
 * @create 18/2/22
 * @since --
"""

import requests
from requests.models import PreparedRequest
from requests_toolbelt.multipart.encoder import MultipartEncoder
import time
import hashlib

import os
import pathlib
import sys

currentTime = round(time.time()*1000.0)

def createFirmwareFile(secretKey, orgId, url, productKey, token):
    accessURL = url + '/connect-service/v2.1/ota-firmwares'
    params = {"action": "create", "orgId": orgId, "productKey": productKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    filepath = pathlib.Path(sys.path[1]) /"resources/IoTHub/ConnectServiceModel/FirmwareManagement/SampleFirmwareFile.bin"
    print(filepath)

    file = open(filepath, 'rb')

    paramsData = "".join(x + y for x, y in params.items())
    print("paransData:", paramsData)

    signData = token + paramsData + str(currentTime) + secretKey
    print("signData:", signData)

    encode = signData.encode('UTF-8')
    print(encode)

    encryption = hashlib.sha256(encode)
    print(encryption)

    hexadecimal = encryption.hexdigest()
    print(hexadecimal)
    signature = hexadecimal.lower()

    body = MultipartEncoder(fields={
         'Content-Disposition': 'form-data',
          'metadata': """{'name': {'defaultValue': 'Python_Firmware_V1.2_Veri',
                        'i18nValue': {'zh_CN': 'Python_固件名称',
                                      'en_US': 'Python_Firmware_Name',
                                      'ja_JP': 'Python_ファームウェア名',
                                      'es_ES': 'Python_NombreDelFirmware'}},
                        'version': '1.2',
                        'signMethod': 'md5',
                        'sign': 'Python_Firmware_Signature',
                        'desc': 'Python_Firmware_Description',
                        'enableVerification': True
                        }""",

    })
    print(body)

    header = {"apim-accesstoken": token,
              "apim-signature": signature,
              "apim-timestamp": str(currentTime),
              "Content-Type": body.content_type
              }
    print(header)

    r = requests.post(req.url, headers=header, data=body)
    content = r.content
    response = content.decode("ASCII")
    print(response)

