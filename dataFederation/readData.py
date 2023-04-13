"""
 * Copyright (C), 2015-2021, Envision
 * FileName: readData
 * Author:  Dylan Yeo
 * Date:    08/03/22
 * Description: Read data by providing SQL query through the specified channel
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/data-federation-api/en/2.3.0/read_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def readData(accessKey, secretKey, orgId, url, channelId, sqlQuery, source, queue, itemFormat):
    accessURL = url + '/data-federation/v2.0/channels/read/' + channelId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"sqlQuery": sqlQuery,
            "source": source,
            "queue": queue,
            "itemFormat": itemFormat
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def readData_source(accessKey, secretKey, orgId, url, channelId, sqlQuery, source):
    accessURL = url + '/data-federation/v2.0/channels/read/' + channelId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Content-Type": "application/json"}

    body = {"sqlQuery": sqlQuery,
            "source": source
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, headers=header)
    print(response)


def readData_queue(accessKey, secretKey, orgId, url, channelId, sqlQuery, queue):
    accessURL = url + '/data-federation/v2.0/channels/read/' + channelId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Content-Type": "application/json"}

    body = {"sqlQuery": sqlQuery,
            "source": "demo",
            "queue": queue,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, headers=header)
    print(response)


def readData_itemFormat(accessKey, secretKey, orgId, url, channelId, sqlQuery, itemFormat):
    accessURL = url + '/data-federation/v2.0/channels/read/' + channelId
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Content-Type": "application/json"}

    body = {"sqlQuery": sqlQuery,
            "source": "demo",
            "itemFormat": itemFormat
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, headers=header)
    print(response)


