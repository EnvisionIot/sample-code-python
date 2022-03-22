import IoTHub.asset.createLogicalAsset as CreateLogicalAsset_py
import IoTHub.asset.deleteLogicalAsset as DeleteLogicalAsset_py
import IoTHub.asset.updateLogicalAsset as UpdateLogicalAsset_py
import IoTHub.asset.getAsset as GetAsset_py
import IoTHub.asset.updateAsset as UpdateAsset_py

#Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
#Device Asset assetId can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
DeviceAsset_assetId = "G5M8Ojhd"
#Logical Asset assetId can be found on EnOS portal (Go to Device Management/Logical Asset under Asset ID)
LogicalAsset_assetId = "AvxV8hkR"

def AssetGeneral(accessKey, secretKey, orgId, url):

    '''Creates, Update, Get and Delete Logical Asset'''
    # NewLogical_assetId = CreateLogicalAsset_py.CreateLogicalAsset(accessKey, secretKey, orgId, url, ModelId)
    # UpdateLogicalAsset_py.UpdateLogicalAsset(accessKey, secretKey, orgId, url, NewLogical_assetId)
    # GetAsset_py.GetAsset(accessKey, secretKey, orgId, url, NewLogical_assetId)
    # DeleteLogicalAsset_py.DeleteLogicalAsset(accessKey, secretKey, orgId, url, NewLogical_assetId)

    '''Update Existing Logical Asset using LogicalAsset_assetId as declared above'''
    # UpdateLogicalAsset_py.UpdateLogicalAsset(accessKey, secretKey, orgId, url, LogicalAsset_assetId)

    '''Update Existing Device Asset using DeviceAsset_assetId as declared above'''
    # UpdateAsset_py.UpdateAsset(accessKey, secretKey, orgId, url, DeviceAsset_assetId)

    '''Get Existing Logical Asset using LogicalAsset_assetId as declared above'''
    # GetAsset_py.GetAsset(accessKey, secretKey, orgId, url, LogicalAsset_assetId)

    '''Get Existing Device Asset using DeviceAsset_assetId as declared above'''
    # GetAsset_py.GetAsset(accessKey, secretKey, orgId, url, DeviceAsset_assetId)





