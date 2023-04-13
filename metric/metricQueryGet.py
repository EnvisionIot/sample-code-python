from poseidon import poseidon

access_key = 'accessKey'
secret_key = 'secretKey'
apigw = ''
org_id = ''


def _metric_query_get(metrics, mdm_ids, start_time, end_time, extra_fields, format):
    url = 'https://' + apigw + '/metric-center/v2.2/customer-metric/data?orgId=' + org_id + \
          '&metrics=' + metrics + \
          '&mdmIds=' + mdm_ids + \
          '&start_time=' + start_time + \
          '&end_time=' + end_time + \
          '&extra_fields=' + extra_fields + \
          '&format=' + format

    header = {"Content-Type": "application/x-www-form-urlencoded"}

    req = poseidon.urlopen(access_key, secret_key, url, header, 'GET')
    print(req)
