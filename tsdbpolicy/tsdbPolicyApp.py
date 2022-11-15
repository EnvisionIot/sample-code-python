import tsdbPolicy.v2_0.getMeasurementPointTSDBMetadata as GetMeasurementPointTSDBMetadata_py
import tsdbPolicy.v2_0.getStoragePolicy_V2_0 as GetStoragePolicy_V2_0_py
import tsdbPolicy.v2_0.saveStoragePolicy_V2_0 as SaveStoragePolicy_V2_0_py
import tsdbPolicy.v2_1.getStoragePolicy_V2_1 as GetStoragePolicy_V2_1_py
import tsdbPolicy.v2_1.saveStoragePolicy_V2_1 as SaveStoragePolicy_V2_1_py
import tsdbPolicy.v2_1.getUnformattedPolicy as GetUnformattedPolicy_py
import tsdbPolicy.v2_1.updateUnformattedPolicy as UpdateUnformattedPolicy_py


def tsdbPolicyGeneral(accessKey, secretKey, orgId, url):
    '''
    V2.0
    https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.0/overview.html
    '''
    # GetMeasurementPointTSDBMetadata_py.getMeasurementPointTSDBMetadata(accessKey, secretKey, orgId, url, modelIds= ["Python_Demo_Model", "demo_lift_model"])
    # GetMeasurementPointTSDBMetadata_py.getMeasurementPointTSDBMetadata_measurepoints(accessKey, secretKey, orgId, url, modelIds= ["demo_lift_model"], measurepoints= ["temp", "humidity"])

    # GetStoragePolicy_V2_0_py.getStoragePolicy_V2_0(accessKey, secretKey, orgId, url, policyId= "823aad0f-efe1-4ee6-ae88-79232c2a9b5c")

    # SaveStoragePolicy_V2_0_py.saveStoragePolicy_V2_0(accessKey, secretKey, orgId, url, policyId= "823aad0f-efe1-4ee6-ae88-79232c2a9b5c", modelId="Python_Demo_Model", points= ["Int_Output"])

    '''
    V2.1
    https://support.envisioniot.com/docs/tsdb-policy-api/en/2.3.0/v2.1/overview.html
    '''
    # GetStoragePolicy_V2_1_py.getStoragePolicy_V2_1(accessKey, secretKey, orgId, url, policyId= "823aad0f-efe1-4ee6-ae88-79232c2a9b5c")

    # SaveStoragePolicy_V2_1_py.saveStoragePolicy_V2_1(accessKey, secretKey, orgId, url, policyId= "823aad0f-efe1-4ee6-ae88-79232c2a9b5c", modelId="Python_Demo_Model", points= ["Int_Output"])

    # GetUnformattedPolicy_py.getUnformattedPolicy(accessKey, secretKey, orgId, url)

    # UpdateUnformattedPolicy_py.updateUnformattedPolicy(accessKey, secretKey, orgId, url)




