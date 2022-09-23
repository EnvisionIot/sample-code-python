# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Device Asset assetId can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
DeviceAsset_assetId = "G5M8Ojhd"
# Device Asset ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)
DeviceAsset_ProductKey = "4kZqiPoC"
# Device Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
DeviceAsset_DeviceKey = "RqMa4xiwqo"
# Logical Asset assetId can be found on EnOS portal (Go to Device Management/Logical Asset under Asset ID)
LogicalAsset_assetId = "AvxV8hkR"
# Tree Id can be found on the EnOS portal (Go to Asset Trees/<Asset_Tree_Name> under Tree ID)
Existing_TreeId = "LlrLCZqt"


def AssetTreeGeneral(accessKey, secretKey, orgId, url):
    '''Create, Get and Delete Asset Tree and also delete Logical Asset which was created along with the Asset Tree'''
    # TreeId = CreateAssetTree_py.CreateAssetTree(accessKey, secretKey, orgId, url, ModelId)
    # AssetId = GetAssetTree_py.GetAssetTree(accessKey, secretKey, orgId, url, TreeId)
    # DeleteAssetTree_py.DeleteAssetTree(accessKey, secretKey, orgId, url, TreeId)
    # DeleteLogicalAsset_py.DeleteLogicalAsset(accessKey, secretKey, orgId, url, AssetId)

    '''Create New Asset Tree and associate Asset Tree with a existing logical asset using its assetId,
    LogicalAsset_assetId as defined above and 
    Delete the Asset Tree
    '''
    # AssociatedLogicalAsset_TreeId = CreateAssetTreeAndAssociateAsset_py.CreateAssetTreeAndAssociateAsset_assetId(
    # accessKey, secretKey, orgId, url, LogicalAsset_assetId)
    # DeleteAssetTree_py.DeleteAssetTree(accessKey, secretKey, orgId, url, AssociatedLogicalAsset_TreeId)

    '''Create New Asset Tree and associate Asset Tree with a exising device asset using its product key and device key,
    DeviceAsset_ProductKey and DeviceAsset_DeviceKey as defined above respectively and 
    Delete the Asset Tree
    '''
    # AssociatedDeviceAsset_TreeId = CreateAssetTreeAndAssociateAsset_py.CreateAssetTreeAndAssociateAsset_Keys(
    # accessKey, secretKey, orgId, url, DeviceAsset_ProductKey, DeviceAsset_DeviceKey)
    # DeleteAssetTree_py.DeleteAssetTree(accessKey, secretKey, orgId, url, AssociatedDeviceAsset_TreeId)

    '''Update Existing Asset Tree using Existing_TreeId as declared above'''
    # UpdateAssetTree_py.UpdateAssetTree(accessKey, secretKey, orgId, url, Existing_TreeId)

    '''Get Asset Tree'''
    # GetAssetTree_py.GetAssetTree(accessKey, secretKey, orgId, url, Existing_TreeId)

    '''Search Asset Tree with projection and pagination'''
    # SearchAssetTree_py.SearchAssetTree(accessKey, secretKey, orgId, url)

    '''Search Asset Tree with expression using tree Id'''
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "treeId ='" + Existing_TreeId + "'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "treeId in ('" + Existing_TreeId + "')")

    '''Search Asset Tree with expression using name'''
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name like 'Default_Updated_Python_AssetTree'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.default like 'Default_Updated_Python_AssetTree'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.default like 'Python_AssetTree'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.en_US like 'Updated_Python_AssetTree'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.zh_CN like '更新Python资产树'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.zh_CN like '树'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.ja_JP like '更新されたPythonアセットツリー'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.ja_JP like 'トツリー'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.es_ES like 'ÁrbolDeActivosDePythonActualizado'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "name.es_ES like 'Python'")

    '''Search Asset Tree with expression using tags'''
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "tags.AssetTreeKey1 = 'AssetTreeValue1'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "tags.NewAssetTreeKey1 = 'NewAssetTreeValue1'")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "exists(tags.AssetKey1)")
    # SearchAssetTree_py.SearchAssetTree_Expression(accessKey, secretKey, orgId, url, "exists(tags.NewAssetTreeKey1)")

    '''Search Asset Tree with filter'''
    # SearchAssetTree_py.SearchAssetTree_Filter(accessKey, secretKey, orgId, url)


