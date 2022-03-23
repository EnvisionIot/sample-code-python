# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from dotenv import load_dotenv

import IoTHub.model.modelApp
import IoTHub.connection.Product.connectionProductApp
import IoTHub.connection.Device.connectionDeviceApp
import IoTHub.connection.DeviceData.connectionDeviceDataApp
import IoTHub.connection.Certificate.connectionCertificateApp
import IoTHub.connection.GatewayAndSubDevices.connectionGatewayAndSubDevicesApp
import IoTHub.connection.HTTPMessageIntegration.connectionHTTPMessageIntegrationApp
import IoTHub.connection.FirmwareManagement.connectionFirmwareManagementApp
import IoTHub.connection.FirmwareOTAUpgradeManagement.connectionFirmwareOTAUpgradeManagementApp
import IoTHub.asset.assetApp
import IoTHub.assetTree.assetTree.assetTreeApp
import IoTHub.assetTree.assetTreeNode.assetTreeNodeApp
import IoTHub.alert.alertApp
import edp.streamprocessing.streamProcessingApp
import edp.tsdbPolicy.tsdbPolicyApp
import edp.tsdbData.tsdbDataApp
import edp.dataFederation.dataFederationApp
import edp.batchProcessing.batchProcessingApp
import aep.applicationportal.applicationPortalApp
import aep.businessprocessmanagement.businessProcessManagementApp



load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    accessKey = os.getenv('accessKey')
    secretKey = os.getenv('secretKey')
    orgId = os.getenv('orgId')
    url = os.getenv('url')

    # Model Service
    # https://support.envisioniot.com/docs/model-api/en/2.3.0/overview.html
    # IoTHub.model.modelApp.modelGeneral(accessKey, secretKey, orgId, url)

    # Connection Service
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/overview.html

    # Connection Service - Product
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_product.html
    # IoTHub.connection.Product.connectionProductApp.ConnectionProductGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - Device
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_device.html
    # IoTHub.connection.Device.connectionDeviceApp.ConnectionDeviceGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - Device Data
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_device_data.html
    # IoTHub.connection.DeviceData.connectionDeviceDataApp.ConnectionDeviceDataGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - Certificate
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_certificate.html
    # IoTHub.connection.Certificate.connectionCertificateApp.ConnectionCertificateGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - Gateway and Sub-Device
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_gateway_subdevice.html
    # IoTHub.connection.GatewayAndSubDevices.connectionGatewayAndSubDevicesApp.ConnectionGatewayAndSubDevicesGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - HTTP Message Integration
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_integration.html
    # IoTHub.connection.HTTPMessageIntegration.connectionHTTPMessageIntegrationApp.ConnectionHTTPMessageIntegrationGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - Firmware Management
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_firmware.html
    # IoTHub.connection.FirmwareManagement.connectionFirmwareManagementApp.ConnectionFirmwareManagementGeneral(accessKey, secretKey, orgId, url)

    # Connection Service - Firmware OTA Upgrade Management
    # https://support.envisioniot.com/docs/connection-api/en/2.3.0/index_ota.html
    # IoTHub.connection.FirmwareOTAUpgradeManagement.connectionFirmwareOTAUpgradeManagementApp.ConnectionFirmwareOTAUpgradeManagementGeneral(accessKey, secretKey, orgId, url)

    # Asset Service
    # https://support.envisioniot.com/docs/asset-api/en/2.3.0/overview.html
    # IoTHub.asset.assetApp.AssetGeneral(accessKey, secretKey, orgId, url)

    # Asset Tree Service - Asset Tree
    # https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/index_asset_tree.html
    # IoTHub.assetTree.assetTree.assetTreeApp.AssetTreeGeneral(accessKey, secretKey, orgId, url)

    # Asset Tree Service - Asset Tree Node
    # https://support.envisioniot.com/docs/asset-tree-api/en/2.3.0/index_asset_node.html
    # IoTHub.assetTree.assetTreeNode.assetTreeNodeApp.AssetTreeNodeGeneral(accessKey, secretKey, orgId, url)

    # Alert Service (Severity/Type/Content/Rule/Record)
    # https://support.envisioniot.com/docs/alert-api/en/2.3.0/overview.html
    # IoTHub.alert.alertApp.alertGeneral(accessKey, secretKey, orgId, url)

    # Stream Processing Service
    # https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/overview.html
    # edp.streamprocessing.streamProcessingApp.streamProcessingGeneral(accessKey, secretKey, orgId, url)

    # TSDB Policy Service
    # https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/overview.html
    # edp.tsdbPolicy.tsdbPolicyApp.tsdbPolicyGeneral(accessKey, secretKey, orgId, url)

    # TSDB Data Service
    # https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/overview.html
    # edp.tsdbData.tsdbDataApp.tsdbDataGeneral(accessKey, secretKey, orgId, url)

    # Data Federation Service
    # https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/overview.html
    # edp.dataFederation.dataFederationApp.dataFederationGeneral(accessKey, secretKey, orgId, url)

    # Batch Processing Service
    # https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/overview.html#
    # edp.batchProcessing.batchProcessingApp.batchProcessingGeneral(accessKey, secretKey, orgId, url)

    # Application Portal Service
    # https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/overview.html
    # aep.applicationportal.applicationPortalApp.applicationPortalGeneral(accessKey, secretKey, orgId, url)

    # Business Process Management Service
    # https://support.envisioniot.com/docs/bpm-api/en/2.3.0/overview.html
    aep.businessprocessmanagement.businessProcessManagementApp.businessProcessManagementGeneral(accessKey, secretKey, orgId, url)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/