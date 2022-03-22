import IoTHub.connection.Product.createProduct as CreateProduct_py
import IoTHub.connection.Product.deleteProduct as DeleteProduct_py
import IoTHub.connection.Device.createDevice as CreateDevice_py
import IoTHub.connection.Device.deleteDevice as DeleteDevice_py
import IoTHub.connection.Device.disableDevice as DisableDevice_py
import IoTHub.connection.Device.enableDevice as EnableDevice_py
import IoTHub.connection.Device.getDevice as GetDevice_py
import IoTHub.connection.Device.replaceDevice as ReplaceDevice_py
import IoTHub.connection.Device.searchDevice as SearchDevice_py
import IoTHub.connection.Device.updateDevice as UpdateDevice_py
import IoTHub.connection.Device.getDeviceStatistics as GetDeviceStatistics_py

# Model Id can be found on EnOS portal (Go to Models under Model ID)
Input_modelId = "python_4attri_model"


def ConnectionDeviceGeneral(accessKey, secretKey, orgId, url):
    # Device Asset assetId can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
    # Device Asset ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)
    # Device Asset Device Key can be found on EnOS portal (Go to Device Management/Device Asset under Device Key)

    '''Creating a product
    Creating and Deleting Device
    Deleting a product
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_MandatoryParams(accessKey, secretKey, orgId, url, ProductKey)
    # DeleteDevice_py.DeleteDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a product
    Creating, Disabling, Enabling, Updating, Getting, and Deleting a device using AssetId
    Deleting a product
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # DisableDevice_py.DisableDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # EnableDevice_py.EnableDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # UpdateDevice_py.UpdateDevice_assetId_PatchUpdate(accessKey, secretKey, orgId, url, AssetId)
    # GetDevice_py.GetDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteDevice_py.DeleteDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating, Disabling, Enabling, Updating, Getting and Deleting a device using ProductKey and DeviceKey
    Deleting a product
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # DisableDevice_py.DisableDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # EnableDevice_py.EnableDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # UpdateDevice_py.UpdateDevice_Keys_PatchUpdate(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # GetDevice_py.GetDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # DeleteDevice_py.DeleteDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating a device, GettingStatistics overall, GettingStatistics and Deleting Device using ProductKey
    Deleting a product
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # GetDeviceStatistics_py.GetDeviceStatistics(accessKey, secretKey, orgId, url)
    # GetDeviceStatistics_py.GetDeviceStatistics_ProductKey(accessKey, secretKey, orgId, url, ProductKey)
    # DeleteDevice_py.DeleteDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating a device, Replacing DeviceKey and Deleting Device using assetId
    Deleting a product
    Note: Replacing a Device would change its Device Key and Device Secret but Asset Id remains unchanged
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # ReplaceDevice_py.ReplaceDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteDevice_py.DeleteDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating a device, Replacing DeviceKey and Deleting Device using ProductKey and DeviceKey
    Deleting a product
    Note: Replacing a Device would change its Device Key and Device Secret but Asset Id remains unchanged
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # New_DeviceKey = ReplaceDevice_py.ReplaceDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # DeleteDevice_py.DeleteDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, New_DeviceKey)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating a device, Replacing DeviceKey manually and Deleting Device
    Deleting a product
    Note: Replacing a Device would change its Device Key and Device Secret but Asset Id remains unchanged
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # Newer_DeviceKey = ReplaceDevice_py.ReplaceDevice_ManualType(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, "Type_New_Device_Key")
    # DeleteDevice_py.DeleteDevice_Keys(accessKey, secretKey, orgId, url, ProductKey, Newer_DeviceKey)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating, Update and Deleting a device
    Deleting a product
    Note: IsPatchUpdate = False for Updating of Devices
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)
    # UpdateDevice_py.UpdateDevice_assetId_NoPatchUpdate(accessKey, secretKey, orgId, url, AssetId)
    # UpdateDevice_py.UpdateDevice_Keys_NoPatchUpdate(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)
    # DeleteDevice_py.DeleteDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)

    '''Creating a Product
    Creating, Searching and Deleting a device
    Deleting a product
    '''
    # ProductKey = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # AssetId, DeviceKey = CreateDevice_py.CreateDevice_OptionalParams(accessKey, secretKey, orgId, url, ProductKey)

    '''Search Product'''
    # SearchDevice_py.SearchDevice(accessKey, secretKey, orgId, url)

    '''Search Product Projection'''
    # SearchDevice_py.SearchDevice_Projection(accessKey, secretKey, orgId, url)

    '''Search Product Pagination'''
    # SearchDevice_py.SearchDevice_Pagination(accessKey, secretKey, orgId, url)

    '''Search Product Expression with modelId'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "modelId ='" + Input_modelId + "'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "modelId !='" + Input_modelId + "'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "modelId in ('" + Input_modelId + "')")

    '''Search Product Expression with productKey'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "productKey ='" + ProductKey + "'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "productKey in ('" + ProductKey + "')")

    '''Search Product Expression with deviceKey'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceKey ='" + DeviceKey + "'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceKey in ('" + DeviceKey + "')")

    '''Search Product Expression with assetId'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "assetId ='" + AssetId + "'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "assetId in ('" + AssetId + "')")

    '''Search Product Expression with deviceTags'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 = 'DeviceValue1'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 != 'DeviceValue1'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "exists(deviceTags.DeviceKey1)")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "not exists(deviceTags.DeviceKey1)")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 in ('DeviceValue1')")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 = 'DeviceValue1' and deviceTags.DeviceKey2 = 'DeviceValue2'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 = 'DeviceValue1' and deviceTags.DeviceKey2 = 'DeviceValue2' and deviceTags.DeviceKey3 = 'DeviceValue3'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 = 'DeviceValue1' and deviceTags.DeviceKey123 != 'DeviceValue123'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 = 'DeviceValue1' or deviceTags.DeviceKey1 = 'DeviceValue2'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "exists(deviceTags.DeviceKey1) and exists(deviceTags.DeviceKey3)")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "exists(deviceTags.DeviceKey1) or exists(deviceTags.DeviceKey3)")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceTags.DeviceKey1 in ('DeviceValue1') and deviceTags.DeviceKey3 in ('DeviceValue3')")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "modelId = 'python_4attri_model' and deviceTags.DeviceKey3 = 'DeviceValue3'")

    '''Search Product Expression with deviceAttributes'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceAttributes.Attribute_Name = 100")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "exists(deviceAttributes.Attribute_Name)")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "not exists(deviceAttributes.Attribute_Name)")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceAttributes.Attribute_Name in (100)")

    '''Search Product Expression with productType'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "productType = 'Device'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "productType = 'Gateway'")

    '''Search Product Expression with firmwareVersion'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "firmwareVersion = 'moxa_cross_v2.2.0'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "firmwareVersion in ('moxa_cross_v2.2.0')")

    '''Search Product Expression with deviceName'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName like 'Device_MyDeviceName'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.default like 'MyDeviceName'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.default like 'yDeviceNa'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.en_US like 'Device_MyDeviceName'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.zh_CN like 'Device_我的设备名称'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.zh_CN like '设备名称'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.ja_JP like 'Device_私のデバイス名'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.ja_JP like '私のデバイス'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.es_ES like 'Device_NombreDeMiDispositivo'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "deviceName.es_ES like 'NombreDeMi'")

    '''Search Product Expression with status'''
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "status = 'online'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "status in ('online')")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "status = 'offline'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "status = 'inactive'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "status = 'disable'")
    # SearchDevice_py.SearchDevice_expression(accessKey, secretKey, orgId, url, "status = 'mirror'")

    # DeleteDevice_py.DeleteDevice_assetId(accessKey, secretKey, orgId, url, AssetId)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey)


