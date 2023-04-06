import connection.Certificate.listCertificate as ListCertificate_py

# Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"
# Device Asset assetId can be found on EnOS portal (Go to Device Management/Device Asset under Asset ID)
AssetId = "assetId1"
# Device Asset ProductKey can be found on EnOS portal (Go to Device Management/Products under Product Key)
ProductKey = "pk1"
# Device Asset Device Key can be found on the EnOS portal (Go to Device Management/Device Asset under Device Key)
DeviceKey = "dk1"


file1 = open('resources/IoTHub/ConnectServiceModel/Certificate/csr (revoked).txt', 'r')
file2 = open('resources/IoTHub/ConnectServiceModel/Certificate/csr.txt', 'r')
file3 = open('resources/IoTHub/ConnectServiceModel/Certificate/csrtest.txt', 'r')
fileGW = open('resources/IoTHub/ConnectServiceModel/Certificate/csrGW.txt', 'r')
CSR_revoked = file1.read()
CSR = file2.read()
CSR2 = file3.read()
CSR_GW = fileGW.read()
file1.close()
file2.close()
file3.close()
fileGW.close()

def ConnectionCertificateGeneral(accessKey, secretKey, orgId, url):

    # ApplyCertificate_py.ApplyCertificate_assetId(accessKey, secretKey, orgId, url, AssetId, CSR2)
    # ApplyCertificate_py.ApplyCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, CSR)

    # RenewCertificate_py.RenewCertificate_assetId(accessKey, secretKey, orgId, url, AssetId, CSR)
    # RenewCertificate_py.RenewCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey, CSR)

    # RevokeCertificate_py.RevokeCertificate_assetId(accessKey, secretKey, orgId, url, AssetId)
    # RevokeCertificate_py.RevokeCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)

    ListCertificate_py.ListCertificate_assetId(accessKey, secretKey, orgId, url, AssetId)
    # ListCertificate_py.ListCertificate_Keys(accessKey, secretKey, orgId, url, ProductKey, DeviceKey)






