"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createOTAJob
 * Author:  Dylan Yeo
 * Date:    21/2/22
 * Description: Create an OTA job for batch verification or upgrading
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/connection-api/en/2.3.0/create_ota_job.html
 * refer to the resources/IoTHub/ConnectServiceModel/FirmwareOTAUpgradeManagement
"""

import poseidon.poseidon
from requests.models import PreparedRequest
import time

start_timestamp = round(time.time()*1000)
hours = 60*60*3 #3 hours in seconds
end_timestamp = round((time.time() + hours)*1000)

def createOTAJob_verify(accessKey, secretKey, orgId, url, firmwareId, version, deviceKeys):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Verify_Job",
                     "i18nValue": {"zh_CN": "OTA_验证工作",
                                   "en_US": "OTA_Verify_Job",
                                   "ja_JP": "OTA_仕事を確認する",
                                   "es_ES": "OTA_Verificar_Trabajo"}},
            "type": "verify",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "deviceKeys": deviceKeys},
            #optional parameters
            "upgradeTimeout": "6000"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None


def createOTAJob_upgrade(accessKey, secretKey, orgId, url, firmwareId, version, deviceKeys):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Upgrade_Job",
                     "i18nValue": {"zh_CN": "OTA_升级工作",
                                   "en_US": "OTA_Upgrade_Job",
                                   "ja_JP": "OTA_アップグレードジョブ",
                                   "es_ES": "OTA_Actualizar_Trabajo"}},
            "type": "upgrade",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "deviceKeys": deviceKeys},
            "upgradePolicy": "snapshot",
            "enableUpgradeRequest": True,
            #optional parameters
            "upgradeTimeout": "600",
            "retryPolicy": {"enableRetry": True,
                            "retryInterval": "10",
                            "retryCount": 5},
            "schedulePolicy": {"isRepeatDaily": True,
                               "startTimestamp": start_timestamp,
                               "endTimestamp": end_timestamp,
                               "timezoneOffsetInMinutes": 60
                               },
            "maximumConcurrency": "10"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None



def createOTAJob_verify_attributes(accessKey, secretKey, orgId, url, firmwareId, version, attributes):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Verify_Job",
                     "i18nValue": {"zh_CN": "OTA_验证工作",
                                   "en_US": "OTA_Verify_Job",
                                   "ja_JP": "OTA_仕事を確認する",
                                   "es_ES": "OTA_Verificar_Trabajo"}},
            "type": "verify",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "attributes": attributes},
            #optional parameters
            "upgradeTimeout": "6000"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None


def createOTAJob_upgrade_attributes(accessKey, secretKey, orgId, url, firmwareId, version, attributes):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Upgrade_Job",
                     "i18nValue": {"zh_CN": "OTA_升级工作",
                                   "en_US": "OTA_Upgrade_Job",
                                   "ja_JP": "OTA_アップグレードジョブ",
                                   "es_ES": "OTA_Actualizar_Trabajo"}},
            "type": "upgrade",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "attributes": attributes},
            "upgradePolicy": "snapshot",
            "enableUpgradeRequest": True,
            # optional parameters
            "upgradeTimeout": "600",
            "retryPolicy": {"enableRetry": True,
                            "retryInterval": "10",
                            "retryCount": 5},
            "schedulePolicy": {"isRepeatDaily": True,
                               "startTimestamp": start_timestamp,
                               "endTimestamp": end_timestamp,
                               "timezoneOffsetInMinutes": 60
                               },
            "maximumConcurrency": "10"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None



def createOTAJob_verify_tags(accessKey, secretKey, orgId, url, firmwareId, version, tags):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Verify_Job",
                     "i18nValue": {"zh_CN": "OTA_验证工作",
                                   "en_US": "OTA_Verify_Job",
                                   "ja_JP": "OTA_仕事を確認する",
                                   "es_ES": "OTA_Verificar_Trabajo"}},
            "type": "verify",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "tags": tags},
            #optional parameters
            "upgradeTimeout": "6000"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None


def createOTAJob_upgrade_tags(accessKey, secretKey, orgId, url, firmwareId, version, tags):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Upgrade_Job",
                     "i18nValue": {"zh_CN": "OTA_升级工作",
                                   "en_US": "OTA_Upgrade_Job",
                                   "ja_JP": "OTA_アップグレードジョブ",
                                   "es_ES": "OTA_Actualizar_Trabajo"}},
            "type": "upgrade",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "tags": tags},
            "upgradePolicy": "snapshot",
            "enableUpgradeRequest": True,
            # optional parameters
            "upgradeTimeout": "600",
            "retryPolicy": {"enableRetry": True,
                            "retryInterval": "10",
                            "retryCount": 5},
            "schedulePolicy": {"isRepeatDaily": True,
                               "startTimestamp": start_timestamp,
                               "endTimestamp": end_timestamp,
                               "timezoneOffsetInMinutes": 60
                               },
            "maximumConcurrency": "10"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None


def createOTAJob_verify_assetTrees(accessKey, secretKey, orgId, url, firmwareId, version, treeId, includedNotes):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Verify_Job",
                     "i18nValue": {"zh_CN": "OTA_验证工作",
                                   "en_US": "OTA_Verify_Job",
                                   "ja_JP": "OTA_仕事を確認する",
                                   "es_ES": "OTA_Verificar_Trabajo"}},
            "type": "verify",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "assetTrees": [{"treeId": treeId,
                                            "includedNotes": includedNotes}]},
            #optional parameters
            "upgradeTimeout": "6000"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None


def createOTAJob_upgrade_assetTrees(accessKey, secretKey, orgId, url, firmwareId, version, treeId, includedNotes=None):
    accessURL = url + '/connect-service/v2.1/ota-jobs'
    params = {"action": "create", "orgId": orgId, "firmwareId": firmwareId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": {"defaultValue": "Python_OTA_Upgrade_Job",
                     "i18nValue": {"zh_CN": "OTA_升级工作",
                                   "en_US": "OTA_Upgrade_Job",
                                   "ja_JP": "OTA_アップグレードジョブ",
                                   "es_ES": "OTA_Actualizar_Trabajo"}},
            "type": "upgrade",
            "upgradeScope": {"type": "partial",
                             "versionNumbers": version,
                             "assetTrees": [{"treeId": treeId,
                                            "includedNotes": includedNotes}]},
            "upgradePolicy": "snapshot",
            "enableUpgradeRequest": True,
            # optional parameters
            "upgradeTimeout": "600",
            "retryPolicy": {"enableRetry": True,
                            "retryInterval": "10",
                            "retryCount": 5},
            "schedulePolicy": {"isRepeatDaily": True,
                               "startTimestamp": start_timestamp,
                               "endTimestamp": end_timestamp,
                               "timezoneOffsetInMinutes": 60
                               },
            "maximumConcurrency": "10"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        jobId = response["data"]["jobId"]
        return jobId
    except:
        jobId = None
