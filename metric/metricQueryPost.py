from poseidon import poseidon

access_key = 'accessKey'
secret_key = 'secretKey'
apigw = ''
org_id = ''


def _metric_query_post(metrics, mdm_ids, start_time, end_time, extra_fields, format):
    url = 'https://' + apigw + '/metric-center/v2.2/customer-metric/data?orgId=' + org_id

    header = {"Content-Type": "application/x-www-form-urlencoded"}

    body = {
        "orgId": org_id,
        "metrics": metrics,
        "mdmIds": mdm_ids,
        "startTime": start_time,
        "endTime": end_time,
        "extraFields": extra_fields,
        "format": format
    }

    req = poseidon.urlopen(access_key, secret_key, url, body, header, 'POST')
    print(req)
