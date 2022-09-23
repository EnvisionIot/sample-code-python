# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Product Key can be found on EnOS Portal (Go to Products under Product Key)
ProductKey = "Bgg1fqZS"

# Device Key can be found on EnOS Portal (Go to Device Assets under Device Key)
DeviceKey = "wnUdCMJf5a"
DeviceKey2 = "INQCUhOavq"
DeviceKey3 = "YrY9DbaHiU"

# AssetId can be found on EnOS Portal (Go to Device Assets under Asset ID)
AssetId = "mF2Xz3jp"
AssetId2 = "nHMUggwB"
AssetId3 = "uiVmGf0P"

# Firmware Id can be found by running searchFirmwareFile.py API and getting FirmwareId from response returned
firmwareId_v1_0 = "6214661271125f2bf2b3f78f"
firmwareId_v1_1 = "62146418d9c7f104ffad7f36"
firmwareId_v1_2_veri = "6214873771125f2bf2b3f799"

# Job Id can be found by running searchOTAJob API (or its other counterparts) as shown below and getting jobId from response returned
jobId = "6214ad2171125f2bf2b3f7b4"

'''
Device details to run simulator
Instructions:
Open .env file and replace DEVICE_KEY and DEVICE_SECRET accordingly

Python_Firmware_Test1:
DEVICE_KEY=wnUdCMJf5a
DEVICE_SECRET=DDFas5dIB28RVVNgRPql

Python_Firmware_Test2:
DEVICE_KEY=INQCUhOavq
DEVICE_SECRET=R5BqjMocOk5AI46OPr90

Python_Firmware_Test3:
DEVICE_KEY=YrY9DbaHiU
DEVICE_SECRET=mSCucfKRIPoOYzWy1Yxh
'''
def ConnectionFirmwareOTAUpgradeManagementGeneral(accessKey, secretKey, orgId, url):
    '''Search for Firmware File to get FirmwareId'''
    # SearchFirmwareId.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "productKey = '" + ProductKey + "'")
    '''Create OTA Job and using Device Key to specify devices'''
    # jobId = CreateOTAJob_py.createOTAJob_upgrade(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.0","1.2"], deviceKeys = [DeviceKey3])
    # jobId = CreateOTAJob_py.createOTAJob_verify(accessKey, secretKey, orgId, url, firmwareId_v1_2_veri, version = ["1.0"], [DeviceKey, DeviceKey2, DeviceKey3])

    '''Alternative: Create OTA Job and using attributes to specify devices'''
    # jobId = CreateOTAJob_py.createOTAJob_upgrade_attributes(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.0","1.2"], attributes = {'Int_Attribute' : [100,1000]})
    # jobId = CreateOTAJob_py.createOTAJob_verify_attributes(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.2"], attributes = {'Int_Attribute' : [100]})

    '''Alternative: Create OTA Job and using tags to specify devices'''
    # jobId = CreateOTAJob_py.createOTAJob_upgrade_tags(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.0","1.2"], tags = {"firmwarekey": ["firmware","firmwarevalue"]})
    # jobId = CreateOTAJob_py.createOTAJob_verify_tags(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.2"], tags = {"firmwarekey": ["firmware","firmwarevalue"]})

    '''Alternative: Create OTA Job and using assetTrees to specify devices'''
    # jobId = CreateOTAJob_py.createOTAJob_upgrade_assetTrees(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.0","1.2"], treeId = "loqyJOpX")
    # jobId = CreateOTAJob_py.createOTAJob_upgrade_assetTrees(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.0","1.2"], treeId = "loqyJOpX", includedNotes = "")
    # jobId = CreateOTAJob_py.createOTAJob_verify_assetTrees(accessKey, secretKey, orgId, url, firmwareId = firmwareId_v1_1, version = ["1.0","1.2"], treeId = "loqyJOpX", includedNotes = "")

    '''Start OTA Job'''
    # StartOTAJob_py.startOTAJob(accessKey, secretKey, orgId, url, jobId)

    '''Get OTA Job'''
    # GetOTAJob_py.getOTAJob(accessKey, secretKey, orgId, url, jobId)

    '''Cancel OTA Task in a job'''
    # CancelOTATask_py.cancelOTATask(accessKey, secretKey, orgId, url, [DeviceKey2, DeviceKey3], jobId)

    '''Retry OTA Task in a job when the task failed or cancelled'''
    # RetryOTATask_py.retryOTATask(accessKey, secretKey, orgId,url, [DeviceKey3], jobId)

    '''Stop OTA Job'''
    # StopOTAJob_py.stopOTAJob(accessKey, secretKey, orgId, url, jobId)

    '''Delete OTA Job'''
    # DeleteOTAJob_py.deleteOTAJob(accessKey, secretKey, orgId, url, jobId)


    '''Search OTA Job with pagination'''
    # SearchOTAJob_py.searchOTAJob(accessKey, secretKey, orgId, url)

    '''Search OTA Job with expression using product key'''
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "productKey ='" + ProductKey + "'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "productKey in ('" + ProductKey + "')")

    '''Search OTA Job with expression using firmware ID'''
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareId ='" + firmwareId_v1_2_veri + "'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareId in ('" + firmwareId_v1_2_veri + "')")

    '''Search OTA Job with expression using firmware version'''
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareVersion = '1.2'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareVersion in ('1.1','1.2')")

    '''Search OTA Job with expression using type'''
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "type  = 'upgrade'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "type  = 'verify'")

    '''Search OTA Job with expression using status'''
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "status = 'started'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "status = 'stopped'")

    '''Search OTA Job with expression using firmware name'''
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName like 'Python_Firmware_V1.2_Veri'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.default like 'Python_Firmware_V1.2_Veri'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.default like 'Python_Firmware_V1.2_Veri'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.en_US like 'Python_Firmware_Name'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.zh_CN like 'Python_固件名称'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.zh_CN like '固件名称'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.ja_JP like 'Python_ファームウェア名'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.ja_JP like 'ウェア名'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.es_ES like 'Python_NombreDelFirmware'")
    # SearchOTAJob_py.searchOTAJob_Expression(accessKey, secretKey, orgId, url, "firmwareName.es_ES like 'NombreDelFirmware'")

    '''Search OTA Task with pagination'''
    # SearchOTATask_py.searchOTATask(accessKey, secretKey, orgId, url)

    '''Search OTA Task with expression using job ID'''
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "jobId ='" + jobId + "'")
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "jobId in ('" + jobId + "')")

    '''Search OTA Task with expression using device key'''
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "deviceKey ='" + DeviceKey + "'")
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "deviceKey in ('wnUdCMJf5a', 'INQCUhOavq', 'YrY9DbaHiU')")

    '''Search OTA Task with expression using fromversion'''
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "fromVersion = '1.0'")
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "fromVersion in ('1.0','1.2')")

    '''Search OTA Task with expression using toVersion'''
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "toVersion = '1.2'")
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "toVersion in ('1.0','1.2')")

    '''Search OTA Task with expression using status'''
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "status = 'succeeded'")
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "status in ('succeeded', 'failed')")

    '''Search OTA Task with expression using description'''
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "desc = 'Cancelled by user'")
    # SearchOTATask_py.searchOTATask_Expression(accessKey, secretKey, orgId, url, "desc in ('Cancelled by user', 'upgrading firmware finished')")

