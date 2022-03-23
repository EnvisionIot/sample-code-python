"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getColorsOfTheMessageIcon
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get the list of colors for configuring the message icon
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/get_colors_of_the_message_icon.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getColorsOfTheMessageIcon(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.2/message/enum/colors"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
