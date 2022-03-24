"""
 * Copyright (C), 2015-2021, Envision
 * FileName: queryProcessInstanceByView
 * Author:  Dylan Yeo
 * Date:    22/03/22
 * Description: Query the list of process instance by process view
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/query_process_instance_by_view.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest
import time

current_time = round(time.time()*1000)

def queryProcessInstanceByView(accessKey, secretKey, url, accessToken, displayViewKey, id):
    accessURL = url + "/enos-bpm-service/v2.0/work/display-view/" + displayViewKey + "/process-instances/query"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"columns": [{"id": id,
                         "filter": "inProgress"
                         }],
            "pagination":  {"current": 0,
                            "pageSize": 5,
                            "sorts": [{"field": "started",
                                       "order": "DESC"}]
                                      }
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
