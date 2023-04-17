import connection.HTTPMessageIntegration.uploadMeasurementPoints as UploadMeasurementPoints_py
import connection.HTTPMessageIntegration.getToken as GetToken_py

# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Device Asset assetId can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
AssetId = "assetId1"
# Device Asset ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)
ProductKey = "pk1"
# Device Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
DeviceKey = "dk1"


def ConnectionHTTPMessageIntegrationGeneral(accessKey, secretKey, orgId, url):

    Token = GetToken_py.GetToken(accessKey,secretKey, url)

    # UploadAttributes_py.UploadAttributes_assetId(orgId, Token, AssetId)
    # UploadAttributes_py.UploadAttributes_Keys(orgId, Token, ProductKey, DeviceKey)
    # UploadAttributes_py.UploadAttributes_multifiles(orgId, Token, AssetId)


    # UploadEvents_py.UploadEvents_assetId(orgId, Token, AssetId)
    # UploadEvents_py.UploadEvents_Keys(orgId, Token, ProductKey, DeviceKey)

    UploadMeasurementPoints_py.UploadMeasurementPoints_assetId(orgId, Token, AssetId)
    # UploadMeasurementPoints_py.UploadMeasurementPoints_Keys(orgId, Token, ProductKey, DeviceKey)














