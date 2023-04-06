# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Device Asset assetId can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
DeviceAsset_assetId = "assetId1"
# Device Asset ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)
DeviceAsset_ProductKey = "pk1"
# Device Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
DeviceAsset_DeviceKey = "dk1"
# Logical Asset assetId can be found on EnOS portal (Go to Device Management/Logical Asset under Asset ID)
# Root Node Asset Id
LogicalAsset_assetId = "assetId1"
# Tree Id can be found on the EnOS portal (Go to Asset Trees/<Asset_Tree_Name> under Tree ID)
Existing_TreeId = "treeId1"
# These Asset Ids can be found on the EnOS portal (Go to Asset Trees/<Asset_Tree_Name>/<Asset_Name> under Asset ID)
Node_AssetId = "assetId1"
SubNode_AssetId = "assetId2"


def AssetTreeNodeGeneral(accessKey, secretKey, orgId, url):

    # AssociateAsset_py.AssociateAsset_assetId(accessKey, secretKey, orgId, url, DeviceAsset_assetId, Existing_TreeId, LogicalAsset_assetId)
    # AssociateAsset_py.AssociateAsset_Keys(accessKey, secretKey, orgId, url, DeviceAsset_ProductKey, DeviceAsset_DeviceKey, Existing_TreeId, LogicalAsset_assetId)

    # Node_AssetId= CreateAndAssociateAsset_py.CreateAndAssociateAsset(accessKey, secretKey, orgId, url, ModelId, Existing_TreeId, LogicalAsset_assetId)

    # DeleteAssetNode_py.DeleteAssetNode_assetId(accessKey, secretKey, orgId, url, Node_AssetId, Existing_TreeId)
    # DeleteAssetNode_py.DeleteAssetNode_Keys(accessKey, secretKey, orgId, url, DeviceAsset_ProductKey, DeviceAsset_DeviceKey, Existing_TreeId)

    # GetAssetTrees_py.GetAssetTrees(accessKey, secretKey, orgId, url)

    '''Search Asset Node with projection and pagination'''
    # SearchAssetNode_py.SearchAssetNode(accessKey, secretKey, orgId, url)

    '''Search Asset Node with expression using tree Id'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "treeId ='" + Existing_TreeId + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "treeId in ('" + Existing_TreeId + "')")

    '''Search Asset Node with expression using asset Id'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "assetId ='" + LogicalAsset_assetId + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "assetId = 'G5M8Ojhd' or assetId ='AvxV8hkR'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "assetId in ('" + LogicalAsset_assetId + "')")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "assetIds in ('G5M8Ojhd','AvxV8hkR')")

    '''Search Asset Node with expression using model Id'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "modelId in ('" + ModelId + "')")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "modelId ='" + ModelId + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "modelIds in ('Python_Demo_Model', 'EnOS_CITY_BUILDING')")

    '''Search Asset Node with expression usiSng root model Id'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "rootModelId in ('" + ModelId + "')")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "rootModelId ='" + ModelId + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "rootModelIds in ('Python_Demo_Model', 'EnOS_CITY_BUILDING')")

    '''Search Asset Node with expression using name'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name like 'Default_Python_AssetNode'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.default like 'Default_Python_AssetNode'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.default like 'Node'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.en_US like 'Python_AssetNode'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.zh_CN like 'Python断言节点'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.zh_CN like '节点'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.ja_JP like 'Pythonアサートノード'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.ja_JP like 'ード'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.es_ES like 'NodoDeAfirmaciónDePython'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "name.es_ES like 'Nodo'")

    '''Search Asset Node with expression using attributes'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "attributes.Int_Attribute = 1")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "attributes.String_Attribute = 'AssetNode'")

    '''Search Asset Node with expression using tags'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "tags.AssetNodeKey1 = 'AssetNodeValue1'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "exists(tags.AssetNodeKey1)")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "tags.AssetNodeKey2 in ('AssetNodeValue1','AssetNodeValue2')")

    '''Search Asset Node with expression using createTime'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "createTime = 1640684761334")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "createTime <= 1639645258000")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "createTime >= 1639645258000")

    '''Search Asset Node with expression using product key and device key'''
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "productKey ='" + DeviceAsset_ProductKey + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "deviceKey ='" + DeviceAsset_DeviceKey + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "deviceKey = 'RqMa4xiwqo' and productKey = '4kZqiPoC'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "productKey like'" + DeviceAsset_ProductKey + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "deviceKey like'" + DeviceAsset_DeviceKey + "'")
    # SearchAssetNode_py.SearchAssetNode_Expression(accessKey, secretKey, orgId, url, "deviceKey like 'RqMa4xiwqo' and productKey like '4kZqiPoC'")

    '''Search Asset Node with filter using asset Ids'''
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"assetIds": ["AvxV8hkR","pqXwiK5U"]})

    '''Search Asset Node with filter using model Ids'''
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"modelIds": ["Python_Demo_Model","EnOS_CITY_BUILDING"]})

    '''Search Asset Node with filter using root model Ids'''
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"rootModelIds": ["Python_Demo_Model","EnOS_CITY_BUILDING"]})

    '''Search Asset Node with filter using attributes'''
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"attributes": {"Int_Attribute": 1,"String_Attribute": "AssetNode"}})

    '''Search Asset Node with filter using tags'''
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"tags":{"AssetNodeKey1": "AssetNodeValue1","AssetNodeKey2": "AssetNodeValue2"}})

    '''Search Asset Node with filter using nameLike'''
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "Default_Python_AssetNode"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "Default_Python_AssetNode", "locale": "default"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "Python_AssetNode", "locale": "en_US"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "Node", "locale": "en_US"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "Python断言节点", "locale": "zh_CN"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "断言节点", "locale": "zh_CN"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "Pythonアサートノード", "locale": "ja_JP"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "アサート", "locale": "ja_JP"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "NodoDeAfirmaciónDePython", "locale": "es_ES"}})
    # SearchAssetNode_py.SearchAssetNode_Filter(accessKey, secretKey, orgId, url, {"nameLike": {"value": "NodoDe", "locale": "es_ES"}})


    '''Search Related Asset Node with projection and pagination'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode(accessKey, secretKey, orgId, url, Existing_TreeId)

    '''Search Related Asset Node with filter using assetIds'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["AvxV8hkR","pqXwiK5U"]})

    '''Search Related Asset Node with filter using model Ids'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"modelIds": ["Python_Demo_Model"]})

    '''Search Related Asset Node with filter using root model Ids'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"rootModelIds": ["Python_Demo_Model"]})

    '''Search Related Asset Node with filter using attributes'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"attributes": {"Int_Attribute": 1,"String_Attribute": "AssetNode"}})

    '''Search Related Asset Node with filter using tags'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"tags":{"AssetNodeKey1": "AssetNodeValue1","AssetNodeKey2": "AssetNodeValue2"}})

    '''Search Related Asset Node with filter using nameLike'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "Default_Python_AssetNode"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "Default_Python_AssetNode", "locale": "default"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "Python_AssetNode", "locale": "en_US"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "Node", "locale": "en_US"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "Python断言节点", "locale": "zh_CN"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "断言节点", "locale": "zh_CN"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "Pythonアサートノード", "locale": "ja_JP"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "アサート", "locale": "ja_JP"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "NodoDeAfirmaciónDePython", "locale": "es_ES"}})
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"nameLike": {"value": "NodoDe", "locale": "es_ES"}})

    '''Search Related Asset Node with filter using isParentOfAssetId'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"isParentOfAssetId": "pqXwiK5U"})

    '''Search Related Asset Node with filter using isChildOfAssetId'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"isChildOfAssetId": "AvxV8hkR"})

    '''Search Related Asset Node with filter using isAncestorOfAssetId'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"isAncestorOfAssetId": "pqXwiK5U"})

    '''Search Related Asset Node with filter using isDescendantOfAssetId'''
    # SearchRelatedAssetNode_py.SearchRelatedAssetNode_Filter(accessKey, secretKey, orgId, url, Existing_TreeId, {"isDescendantOfAssetId": "AvxV8hkR"})

    '''Search Asset Path with projection and pagination'''
    # SearchAssetPath_py.SearchAssetPath(accessKey, secretKey, orgId, url, Existing_TreeId)
    
    '''Search Asset Path with from (Starting point of asset paths) using root model Ids'''
    # SearchAssetPath_py.SearchAssetPath_from(accessKey, secretKey, orgId, url, Existing_TreeId, {"rootModelIds": ["Python_Demo_Model"]})

    '''Search Asset Path with from (Starting point of asset paths) using model Ids'''
    # SearchAssetPath_py.SearchAssetPath_from(accessKey, secretKey, orgId, url, Existing_TreeId, {"modelIds": ["Python_Demo_Model"]})

    '''Search Asset Path with from (Starting point of asset paths) using asset Ids'''
    # SearchAssetPath_py.SearchAssetPath_from(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["AvxV8hkR"]})
    # SearchAssetPath_py.SearchAssetPath_from(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["pqXwiK5U"]})
    # SearchAssetPath_py.SearchAssetPath_from(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["AvxV8hkR","pqXwiK5U"]})

    '''Search Asset Path with to (Ending point of asset paths) using root model Ids'''
    # SearchAssetPath_py.SearchAssetPath_to(accessKey, secretKey, orgId, url, Existing_TreeId, {"rootModelIds": ["Python_Demo_Model"]})

    '''Search Asset Path with to (Ending point of asset paths) using model Ids'''
    # SearchAssetPath_py.SearchAssetPath_to(accessKey, secretKey, orgId, url, Existing_TreeId, {"modelIds": ["Python_Demo_Model"]})

    '''Search Asset Path with to (Ending point of asset paths) using asset Ids'''
    # SearchAssetPath_py.SearchAssetPath_to(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["LKnsI2hG"]})
    # SearchAssetPath_py.SearchAssetPath_to(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["pqXwiK5U"]})
    # SearchAssetPath_py.SearchAssetPath_to(accessKey, secretKey, orgId, url, Existing_TreeId, {"assetIds": ["pqXwiK5U","LKnsI2hG"]})

    '''Search Asset Path with pathProjection (Choose between showing all paths or start & end points of paths)'''
    # SearchAssetPath_py.SearchAssetPath_pathProjection(accessKey, secretKey, orgId, url, Existing_TreeId, "COMPLETE")
    # SearchAssetPath_py.SearchAssetPath_pathProjection(accessKey, secretKey, orgId, url, Existing_TreeId, "END_NODE_ONLY")









