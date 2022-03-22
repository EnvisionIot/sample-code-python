import IoTHub.connection.GatewayAndSubDevices.addSubDevice as AddSubDevice_py
import IoTHub.connection.GatewayAndSubDevices.getGateway as GetGateway_py
import IoTHub.connection.GatewayAndSubDevices.removeSubDevice as RemoveSubDevice_py
import IoTHub.connection.GatewayAndSubDevices.searchSubDevice as SearchSubDevice_py

# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Gateway Asset Asset ID can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
Gateway_AssetId = "zhD6Kpfs"
# Gateway Asset Product Key can be found on EnOS portal (Go to Device Management/Products under Product Key)
Gateway_ProductKey = "8f7KmDEC"
# Gateway Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
Gateway_DeviceKey = "cJdubki1tb"

# SubDevice Asset ID can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
SubDevice1_AssetId = "OPVD7NPz"
SubDevice2_AssetId = "Nmw9npSq"

# SubDevice/Device Asset ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)
SubDevice_ProductKey = "4kZqiPoC"

# SubDeviceDevice Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
SubDevice1_DeviceKey = "ma60hFFTeL"
SubDevice2_DeviceKey = "GW46kFBhkA"

# These attributes can be found on the EnOS portal (Go to Device Management/Device/View(Device that you choose)/Attributes)
SubDevice_AttributeName = "Date_Attribute"
SubDevice_AttributeValue = "2022-01-01"


def ConnectionGatewayAndSubDevicesGeneral(accessKey, secretKey, orgId, url):
    '''Add SubDevice to Gateway, Get Gateway and Remove SubDevice from Gateway using Gateway Asset ID'''
    # AddSubDevice_py.AddSubDevice_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId)
    # GetGateway_py.GetGateway_assetId(accessKey, secretKey, orgId, url)
    # RemoveSubDevice_py.RemoveSubDevice_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId)

    '''Add SubDevice to Gateway, Get Gateway and Remove SubDevice from Gateway using Gateway Product Key and Device Key'''
    # AddSubDevice_py.AddSubDevice_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey)
    # GetGateway_py.GetGateway_Keys(accessKey, secretKey, orgId, url)
    # RemoveSubDevice_py.RemoveSubDevice_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey)

    '''Add Python_SubDevice1 and Python_SubDevice2 for searching purposes below'''
    # AddSubDevice_py.AddSubDevice_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId)

    '''Search SubDevice(Asset Id parameter) with projection and pagination'''
    # SearchSubDevice_py.SearchSubDevice_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId)

    '''Search SubDevice(Product Key and Device Key parameters) with projection and pagination'''
    # SearchSubDevice_py.SearchSubDevice_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey)

    '''Search SubDevice(Asset Id parameter) with expression using Model Id'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "modelId = '" + ModelId + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "modelId in ('" + ModelId + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "modelId in (\"" + ModelId + "\")")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using Model Id'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "modelId = '" + ModelId + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "modelId in ('" + ModelId + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "modelId in (\"" + ModelId + "\")")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice Product Key'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "productKey = '" + SubDevice_ProductKey + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "productKey in ('" + SubDevice_ProductKey + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "productKey in (\"" + SubDevice_ProductKey + "\")")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice Product Key'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "productKey = '" + SubDevice_ProductKey + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "productKey in ('" + SubDevice_ProductKey + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "productKey in (\"" + SubDevice_ProductKey + "\")")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice Device Key'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceKey = '" + SubDevice1_DeviceKey + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceKey in ('" + SubDevice1_DeviceKey + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceKey in (\"" + SubDevice1_DeviceKey + "\")")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice Device Key'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceKey = '" + SubDevice2_DeviceKey + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceKey in ('" + SubDevice2_DeviceKey + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceKey in (\"" + SubDevice2_DeviceKey + "\")")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice Asset Id'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "assetId = '" + SubDevice1_AssetId + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "assetId in ('" + SubDevice1_AssetId + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "assetId in (\"" + SubDevice1_AssetId + "\")")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice Asset Id'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "assetId = '" + SubDevice2_AssetId + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "assetId in ('" + SubDevice2_AssetId + "')")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "assetId in (\"" + SubDevice2_AssetId + "\")")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice Device Attributes'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceAttributes." + SubDevice_AttributeName + "='" + SubDevice_AttributeValue + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "exists(deviceAttributes." + SubDevice_AttributeName + ")")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "not exists(deviceAttributes." + "Random_AttributeName" + ")")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceAttributes." + SubDevice_AttributeName + " in ('" + SubDevice_AttributeValue + "')")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice Device Attributes'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceAttributes." + SubDevice_AttributeName + "='" + SubDevice_AttributeValue + "'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "exists(deviceAttributes." + SubDevice_AttributeName + ")")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "not exists(deviceAttributes." + "Random_AttributeName" + ")")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceAttributes." + SubDevice_AttributeName + " in ('" + SubDevice_AttributeValue + "')")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice Device Tags'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceTags.SubDevice1Key1 = 'SubDevice1Value1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "exists(deviceTags.SubDevice1Key1)")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "not exists(deviceTags.SubDevice1Key1)")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceTags.SubDevice1Key1 in ('SubDevice1Value1')")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceTags.SubDevice1Key1 = 'SubDevice1Value1' and deviceTags.SubDevice1Key2 = 'SubDevice1Value2'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceTags.SubDevice1Key1 = 'SubDevice1Value1' and deviceTags.SubDevice1Key2 = 'SubDevice1Value2' and deviceTags.SubDevice1Key3 = 'SubDevice1Value3'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceTags.SubDevice1Key1 = 'SubDevice1Value1' or deviceTags.SubDevice2Key1 = 'SubDevice2Value1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "exists(deviceTags.SubDevice1Key1) and exists(deviceTags.SubDevice1Key3)")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "exists(deviceTags.SubDevice1Key1) or exists(deviceTags.SubDevice1Key3)")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceTags.SubDevice1Key1 in ('SubDevice1Value1') and deviceTags.SubDevice1Key3 in ('SubDevice1Value3')")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "modelId = 'Python_Demo_Model' and deviceTags.SubDevice1Key3 = 'SubDevice1Value3'")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice Device Tags'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceTags.SubDevice2Key1 = 'SubDevice2Value1'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "exists(deviceTags.SubDevice2Key1)")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "not exists(deviceTags.SubDevice2Key1)")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceTags.SubDevice2Key1 in ('SubDevice2Value1')")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceTags.SubDevice2Key1 = 'SubDevice2Value1' and deviceTags.SubDevice2Key2 = 'SubDevice2Value2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceTags.SubDevice2Key1 = 'SubDevice2Value1' and deviceTags.SubDevice2Key2 = 'SubDevice2Value2' and deviceTags.SubDevice2Key3 = 'SubDevice2Value3'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceTags.SubDevice2Key1 = 'SubDevice2Value1' or deviceTags.SubDevice1Key1 = 'SubDevice1Value1'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "exists(deviceTags.SubDevice2Key1) and exists(deviceTags.SubDevice2Key3)")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "exists(deviceTags.SubDevice2Key1) or exists(deviceTags.SubDevice2Key3)")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceTags.SubDevice2Key1 in ('SubDevice2Value1') and deviceTags.SubDevice2Key3 in ('SubDevice2Value3')")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "modelId = 'Python_Demo_Model' and deviceTags.SubDevice2Key3 = 'SubDevice2Value3'")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice Device Name'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName like 'Python_SubDevice1_Default'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.default like 'Python_SubDevice1_Default'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.default like 'SubDevice1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.en_US like 'Python_SubDevice1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.zh_CN like 'Python子设备1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.zh_CN like '子设备1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.ja_JP like 'Pythonサブデバイス1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.ja_JP like 'サブデバイス1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.es_ES like 'SubDispositivoPython1'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "deviceName.es_ES like 'Python1'")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice Device Name'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName like 'Python_SubDevice2_Default'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.default like 'Python_SubDevice2_Default'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.default like 'SubDevice2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.en_US like 'Python_SubDevice2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.zh_CN like 'Python子设备2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.zh_CN like '子设备2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.ja_JP like 'Pythonサブデバイス2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.ja_JP like 'サブデバイス2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.es_ES like 'SubDispositivoPython2'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "deviceName.es_ES like 'Python2'")

    '''Search SubDevice(Asset Id parameter) with expression using SubDevice status'''
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "status = 'inactive'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "status = 'online'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "status = 'offline'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "status = 'disable'")
    # SearchSubDevice_py.SearchSubDevice_expression_assetId(accessKey, secretKey, orgId, url, Gateway_AssetId, "status = 'mirror'")

    '''Search SubDevice(Product Key and Device Key parameters) with expression using SubDevice status'''
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "status = 'inactive'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "status = 'online'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "status = 'offline'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "status = 'disable'")
    # SearchSubDevice_py.SearchSubDevice_expression_Keys(accessKey, secretKey, orgId, url, Gateway_ProductKey, Gateway_DeviceKey, "status = 'mirror'")
