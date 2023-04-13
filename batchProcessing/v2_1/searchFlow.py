"""
 * Copyright (C), 2015-2021, Envision
 * FileName: searchFlow_V2_1
 * Author:  Dylan Yeo
 * Date:    14/03/22
 * Description: Search the basic information of workflows that meet the search criteria (including workflows of other users in the organization (OU))
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/batch-processing-api/en/2.3.0/v2.1/search_flow.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getFlowExpression(accessKey, secretKey, orgId, url, userId, expression):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "search", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"expression": expression,
            "pagination": {"pageNo": 1,
                           "pageSize": 10,
                           "sorters": [{"field": "start_time",
                                        "order": "DESC"
                                        }]}
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchFlowPagination(accessKey, secretKey, orgId, url, userId, pagination):
    accessURL = url + "/batch-processing-service/v2.1/flows"
    params = {"action": "search", "orgId": orgId, "userId": userId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"pagination": pagination
            }

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)




