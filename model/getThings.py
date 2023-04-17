import poseidon.poseidon
from requests.models import PreparedRequest

def getThings(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "get", "orgId": orgId, 'modelId': 'demo_lift_model', 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)