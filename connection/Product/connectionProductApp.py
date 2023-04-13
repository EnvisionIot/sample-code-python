# Model Id can be found on EnOS portal under MOdelID (Go to Models)
Input_modelId = "python_4attri_model"


def ConnectionProductGeneral(accessKey, secretKey, orgId, url):
    # ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)

    '''Creating, Getting and Deleting of product'''
    # ProductKey_Basic = CreateProduct_py.CreateProduct_Basic(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_Basic)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_Basic)

    '''Creating, Getting and Deleting of product with biDirectionalAuth setting'''
    # ProductKey_biDirectionalAuth = CreateProduct_py.CreateProduct_biDirectionalAuth(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_biDirectionalAuth)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_biDirectionalAuth)

    '''Creating, Getting and Deleting of product with dateFormatCustom setting'''
    # ProductKey_dataFormatCustom = CreateProduct_py.CreateProduct_dataFormatCustom(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_dataFormatCustom)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_dataFormatCustom)

    '''Creating, Getting and Deleting of product with localeNames'''
    # ProductKey_localeName = CreateProduct_py.CreateProduct_localeName(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_localeName)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_localeName)

    '''Creating, Getting and Deleting of product with productType as Gateway'''
    # ProductKey_productType_Gateway = CreateProduct_py.CreateProduct_productType_Gateway(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_productType_Gateway)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_productType_Gateway)

    '''Creating, Getting and Deleting of product with dynamicActivateEnabled setting'''
    # ProductKey_dynamicActivateEnabled = CreateProduct_py.CreateProduct_dynamicActivateEnabled(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_dynamicActivateEnabled)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_dynamicActivateEnabled)

    '''Creating, Getting and Deleting of product with productTags setting'''
    # ProductKey_productTags = CreateProduct_py.CreateProduct_productTags(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_productTags)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_productTags)

    '''Creating, Getting and Deleting of product with defaultValidDay setting'''
    # ProductKey_defaultValidDay = CreateProduct_py.CreateProduct_defaultValidDay(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_defaultValidDay)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_defaultValidDay)

    '''Creating, Getting and Deleting of product with maxValidDay setting'''
    # ProductKey_maxValidDay = CreateProduct_py.CreateProduct_maxValidDay(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_maxValidDay)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_maxValidDay)

    '''Creating, Getting and Deleting of product with default and max valid Day setting'''
    # ProductKey_defaultandmaxValidDay = CreateProduct_py.CreateProduct_deafaultandmaxValidDay(accessKey, secretKey, orgId, url, Input_modelId)
    # GetProduct_py.GetProduct(accessKey, secretKey, orgId, url, ProductKey_defaultandmaxValidDay)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_defaultandmaxValidDay)

    '''Searching of product'''
    # SearchProduct_py.SearchProduct(accessKey, secretKey, orgId, url)
    # SearchProduct_py.SearchProduct_Pagination(accessKey, secretKey, orgId, url)

    '''Creating, Updating and Deleting of product (Update parameters individually)'''
    # ProductKey_UpdateTest = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # UpdateProduct_py.UpdateProduct_productDesc(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)
    # UpdateProduct_py.UpdateProduct_biDirectionalAuth(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)
    # UpdateProduct_py.UpdateProduct_dynamicActivateEnabled(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)
    # UpdateProduct_py.UpdateProduct_productName(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)
    # UpdateProduct_py.UpdateProduct_productTags(accessKey,secretKey, orgId, url, ProductKey_UpdateTest)
    # UpdateProduct_py.UpdateProduct_defaultValidDay(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)
    # UpdateProduct_py.UpdateProduct_maxValidDay(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_UpdateTest)

    '''Creating and Updating of product (Update parameters altogether)'''
    # ProductKey_UpdateTest2 = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)
    # UpdateProduct_py.UpdateProduct(accessKey, secretKey, orgId, url, ProductKey_UpdateTest2)
    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_UpdateTest2)

    '''Creating, Searching and Deleting of product'''
    # ProductKey_Test = CreateProduct_py.CreateProduct_ForTesting(accessKey, secretKey, orgId, url, Input_modelId)

    '''Search Product'''
    # SearchProduct_py.SearchProduct(accessKey, secretKey, orgId, url)
    #
    '''Search Product Projection'''
    # SearchProduct_py.SearchProduct_Pagination(accessKey, secretKey, orgId, url)

    '''Search Product Expression with modelId'''
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "modelId ='" + Input_modelId + "'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "modelId in ('" + Input_modelId + "')")

    '''Search Product Expression with productKey'''
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "productKey ='" + ProductKey_Test + "'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productKey in ('" + ProductKey_Test + "')")

    '''Search Product Expression with productTags'''
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productTags.SearchKey1 = 'SearchValue1'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "exists(productTags.SearchKey1)")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "not exists(productTags.SearchKey1)")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productTags.SearchKey1 = 'SearchValue1' and productTags.SearchKey2 = 'SearchValue2'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productTags.SearchKey1 = 'SearchValue1' and productTags.SearchKey2 = 'SearchValue2' and productTags.SearchKey3 = 'SearchValue3'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productTags.SearchKey1 = 'SearchValue1' or productTags.SearchKey1 = 'SearchValue2'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"exists(productTags.SearchKey1) and exists(productTags.SearchKey3)")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"exists(productTags.SearchKey1) or exists(productTags.SearchKey3)")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"modelId = 'python_4attri_model' and productTags.SearchKey3 = 'SearchValue3'")

    '''Search Product Expression with productName'''
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productName like '<Product_Name_ProductTest>'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productName.default like 'ProductTest'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "productName.default like 'roductTe'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "productName.en_US like 'ProductTest'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productName.zh_CN like 'ProductTest_简体中文'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "productName.zh_CN like '中文'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productName.ja_JP like 'ProductTest_日本語'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "productName.ja_JP like '日本'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url,"productName.es_ES like 'ProductTest_Español'")
    # SearchProduct_py.SearchProduct_expression(accessKey, secretKey, orgId, url, "productName.es_ES like 'Español'")

    # DeleteProduct_py.DeleteProduct(accessKey, secretKey, orgId, url, ProductKey_Test)
