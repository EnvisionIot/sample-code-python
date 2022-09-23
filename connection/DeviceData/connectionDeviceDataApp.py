# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Device Asset Asset ID can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
AssetId = "G5M8Ojhd"
# Device Asset Product Key can be found on EnOS portal (Go to Device Management/Products under Product Key)
ProductKey = "4kZqiPoC"
# Device Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
DeviceKey = "RqMa4xiwqo"


def ConnectionDeviceDataGeneral(accessKey, secretKey, orgId, url):
    '''Creating MeasurementPoint value'''
    # CommandId_assetId = SetMeasurementPoint_py.SetMeasurementPoint_assetId(accessKey, secretKey, orgId, url, AssetId)
    # CommandId_Keys = SetMeasurementPoint_py.SetMeasurementPoint_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)

    '''Get command information (delay of 5 seconds as command may not be found directly after creating a command)'''
    # time.sleep(5)
    # GetCommand_py.GetCommand_assetId(accessKey, secretKey, orgId, url, AssetId, CommandId_assetId)
    # GetCommand_py.GetCommand_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, CommandId_Keys)

    '''Cancel Command'''
    # CancelCommand_py.CancelCommand_assetId(accessKey, secretKey, orgId, url, AssetId)
    # CancelCommand_py.CancelCommand_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # CancelCommand_py.CancelCommand_assetId_CommandId(accessKey, secretKey, orgId, url, AssetId, CommandId_assetId)
    # CancelCommand_py.CancelCommand_Keys_CommandId(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, CommandId_Keys)

    '''Get an Event'''
    # GetEvent_py.GetEvent(accessKey, secretKey, orgId, url)
    # GetEvent_py.GetEvent_ResolveName(accessKey, secretKey, orgId, url)

    '''Get the most updated MeasurementPoint Value'''
    # GetLatestMeasurementPoints_py.GetLatestMeasurementPoints_assetId(accessKey, secretKey, orgId, url, AssetId)
    # GetLatestMeasurementPoints_py.GetLatestMeasurementPoints_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)

    '''Invoke a service'''
    # InvokeService_py.InvokeService_assetId(accessKey, secretKey, orgId, url, AssetId)
    # InvokeService_py.InvokeService_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)


    '''Search for commands(Asset Id parameters) with projection and pagination'''
    # SearchCommand_py.SearchCommand_assetId(accessKey, secretKey, orgId, url, AssetId)
    
    '''Search for commands(assetId parameters) with expression using state
    States:
    1: Created
    2: Revoked
    3: Expired
    4: Sent
    5: Succeeded
    6: Failed
    7: Timed Out
    Refer to: https://support.envisioniot.com/docs/device-connection/en/2.3.0/howto/device/viewing_command_status.html
    '''
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "state = 5")

    '''Search for commands(Asset Id parameters) with expression using commandName'''
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.default like 'Service1'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.default like 'Serv'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.default like 'Int_MeasurementPoint'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.default like 'MeasurementPoi'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.en_US like 'Integer Measurement Point'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.en_US like 'Integ'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.zh_CN like '整数测量点'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.zh_CN like '测量点'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.ja_JP like '整数メジャーポイント'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.ja_JP like 'ーポ'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.es_ES like 'Punto de medida entero'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "commandName.es_ES like 'de medida'")

    '''Search for commands(Asset Id parameters) with expression using createTime'''
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "createTime < '2022-01-21 17:27:46'")
    # SearchCommand_py.SearchCommand_expression_assetId(accessKey, secretKey, orgId, url, AssetId, "createTime >= '2022-01-21 17:27:46'")


    '''Search for commands(productKey and deviceKey parameters) with projection and pagination'''
    # SearchCommand_py.SearchCommand_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)

    '''Search for commands(Product Key and Device Key parameters) with expression using state
    States: Refer to "Search for commands(assetId parameters) with expression using state" above
    Refer to: https://support.envisioniot.com/docs/device-connection/en/2.3.0/howto/device/viewing_command_status.html
    '''
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, "state = 5")

    '''Search for commands(Product Key and Device Key parameters) with expression using commandName'''
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.default like 'Service1'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.default like 'Serv'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.default like 'Int_MeasurementPoint'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.default like 'MeasurementPoi'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.en_US like 'Integer Measurement Point'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.en_US like 'Integ'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.zh_CN like '整数测量点'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.zh_CN like '测量点'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.ja_JP like '整数メジャーポイント'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.ja_JP like 'ーポ'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.es_ES like 'Punto de medida entero'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"commandName.es_ES like 'de medida'")

    '''Search for commands(Product Key and Device Key parameters) with expression using createTime'''
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"createTime < '2022-01-21 17:27:46'")
    # SearchCommand_py.SearchCommand_expression_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey,"createTime >= '2022-01-21 17:27:46'")


    '''Search for events with pagination and resolveName'''
    # SearchEvent_py.SearchEvent(accessKey, secretKey, orgId, url)

    '''Search for events with productKey'''
    # SearchEvent_py.SearchEvent_productKey(accessKey, secretKey, orgId, url, ProductKey)

    '''Search for events with deviceKey'''
    # SearchEvent_py.SearchEvent_deviceKey(accessKey, secretKey, orgId, url, DeviceKey)

    '''Search for events with assetId'''
    # SearchEvent_py.SearchEvent_assetId(accessKey, secretKey, orgId, url, AssetId)

    '''Search for events with tslEventKey'''
    # SearchEvent_py.SearchEvent_tslEventKey(accessKey, secretKey, orgId, url, "Event1")

    '''Search for events with tslEventType'''
    # SearchEvent_py.SearchEvent_tslEventType(accessKey, secretKey, orgId, url, "INFO")

    '''Search for events with startTime'''
    # SearchEvent_py.SearchEvent_startTime(accessKey, secretKey, orgId, url, "2022-01-25 10:32:32")

    '''Search for events with endTime'''
    # SearchEvent_py.SearchEvent_endTime(accessKey, secretKey, orgId, url, "2022-01-25 10:32:32")

    '''Search for events with expression'''
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "productKey = '4kZqiPoC'")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "productKey in ('4kZqiPoC')")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "deviceKey = 'RqMa4xiwqo'")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "deviceKey in ('RqMa4xiwqo')")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "assetId ='G5M8Ojhd'")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "assetId in ('G5M8Ojhd')")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "tslEventKey = 'Event1'")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "tslEventKey in ('Event1')")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "tslEventType = 'INFO'")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "tslEventType in ('INFO')")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "productKey = '4kZqiPoC' and deviceKey = 'RqMa4xiwqo'")
    # SearchEvent_py.SearchEvent_expression(accessKey, secretKey, orgId, url, "tslEventKey = 'Event1' or tslEventType = 'WARNING'")

    '''Generate Token for application use'''
    # Token = GetToken_py.GetToken(accessKey, secretKey, url)

    '''Download File from Device'''
    # DownloadFile_py.DownloadFile_assetId(orgId, Token, AssetId)
    # DownloadFile_py.DownloadFile_Keys(orgId, Token, ProductKey, DeviceKey)

    '''Delete File from Device'''
    # DeleteFile_py.DeleteFile_assetId(accessKey, secretKey, orgId, Token, AssetId)
    # DeleteFile_py.DeleteFile_Keys(accessKey, secretKey, orgId, Token, ProductKey, DeviceKey)
