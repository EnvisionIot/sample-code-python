from poseidon import poseidon

access_key = 'accessKey'
secret_key = 'secretKey'
apigw = 'api gate way'
org_id = 'your org id'
metrics = 'your metric id'
mdm_ids = 'your asset'
start_time = 'start time'
end_time = 'end time'
extra_fields = 'dimension fields'
format = 0

def _metric_query_get():
    url = 'https://' + apigw + '/metric-mgmt/v1.0/metrics/data/normal?orgId=' + org_id + \
          '&metrics=' + metrics + \
          '&mdmIds=' + mdm_ids + \
          '&startTime=' + start_time + \
          '&endTime=' + end_time + \
          '&extraField=' + extra_fields + \
          '&format=' + str(format)

    header = {"Content-Type": "application/json"}

    req = poseidon.urlopen(key=access_key, secret=secret_key, url=url.replace(" ", "%20"), headers=header, method='GET')
    print(req)
