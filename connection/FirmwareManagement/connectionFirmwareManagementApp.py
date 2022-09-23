import connection.FirmwareManagement.createFirmwareFile as CreateFirmwareFile_py

import connection.HTTPMessageIntegration.getToken as GetToken_py

ModelId = "Python_Demo_Model"
ProductKey = "4kZqiPoC"
DeviceKey = "RqMa4xiwqo"
AssetId = "G5M8Ojhd"


def ConnectionFirmwareManagementGeneral(accessKey, secretKey, orgId, url):
    getToken = GetToken_py.GetToken(accessKey, secretKey, url)
    # RefreshToken_py.refreshToken(accessKey,secretKey, url, getToken)
    CreateFirmwareFile_py.createFirmwareFile(secretKey, orgId, url, ProductKey, getToken)

    # DeleteFirmware_py.deleteFirmwareFile(accessKey, secretKey, orgId, url)

    # GetFirmwareFile_py.getFirmwareFile(accessKey, secretKey, orgId, url, "62046c6182355078ea03cd7a")

    # ListDeviceCurrentFirmware_py.listDeviceCurrentFirmware(accessKey, secretKey, orgId, url, "A1wKaFX6")

    '''Search Firmware File with pagination'''
    # SearchFirmwareFile_py.searchFirmwareFile(accessKey, secretKey, orgId, url)

    '''Search Firmware File with expression using product key'''
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "productKey = '" + ProductKey + "'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "productKey in ('A1wKaFX6')")

    '''Search Firmware File with expression using isVerified'''
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "isVerified = True")

    '''Search Firmware File with expression using name'''
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name like 'new firm'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.default like 'new firm'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.default like 'firm'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.en_US like 'Contents'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.zh_CN like '内容'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.zh_CN like '内'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.ja_JP like 'コンテンツ'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.ja_JP like 'ンツ'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.es_ES like 'Contenido'")
    # SearchFirmwareFile_py.searchFirmwareFile_Expression(accessKey, secretKey, orgId, url, "name.es_ES like 'Conten'")

    '''Search Device Upgrade with pagination'''
    # SearchDeviceUpgrade_py.searchDeviceUpgrade(accessKey, secretKey, orgId, url)

    '''Search Device Upgrade with expression using product key'''
    # SearchDeviceUpgrade_py.searchDeviceUpgrade_Expression(accessKey, secretKey, orgId, url, "productKey = '" + ProductKey + "'")
    # SearchDeviceUpgrade_py.searchDeviceUpgrade_Expression(accessKey, secretKey, orgId, url, "productKey in ('A1wKaFX6')")

    '''Search Device Upgrade with expression using firmware version'''
    # SearchDeviceUpgrade_py.searchDeviceUpgrade_Expression(accessKey, secretKey, orgId, url, "firmwareVersion = '1.0.1'")
    # SearchDeviceUpgrade_py.searchDeviceUpgrade_Expression(accessKey, secretKey, orgId, url, "firmwareVersion in ('moxa_cross_v2.2.0')")

    '''Search Device Upgrade with expression using isUpgrading'''
    # SearchDeviceUpgrade_py.searchDeviceUpgrade_Expression(accessKey, secretKey, orgId, url, "isUpgrading = False")
