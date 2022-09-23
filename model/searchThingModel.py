import poseidon.poseidon
from requests.models import PreparedRequest


def searchmodel_withexpression(accessKey, secretKey, orgId, url, expression):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": expression,
        "projection": [
            "modelId",
            "name",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_projection(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "event_tags.type = 'temp' ",
        "projection": [
            "modelId",
            "name",
            "events",
            "modelIdPath",
            "orgId",
            "desc",
            "tags",
            "attributes",
            "measurepoints",
            "services",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_pagination(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "event_tags.type = 'temp' ",
        "projection": [
            "modelId",
            "name",
            "event",
        ],
        "pagination": {
            "pageNo": 1,
            "pageSize": 20,
            # Sorter not supported
            # "sorters": [{
            # "field": "modelId",
            # "order": "ASC"
            # }]
        }
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_name(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "modelId in ( 'python_4attri_model' )",
       "projection": [
            "modelId",
            "name",
            "events",
            "modelIdPath",
            "orgId",
            "desc",
            "tags",
            "attributes",
            "measurepoints",
            "services",
            #"category",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_publicmodels(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "modelId in ( 'EnOS_Solar_Site' , 'ESSHVAC' )",
        "projection": [
            "modelId",
            "name",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_features_pagination(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "modelId in ( 'EnOS_Solar_Site' )",
        "projection": [
            "modelId",
            "name",
            "attributes",
            "measurepoints",
            "services",
            "events"
        ],
        "pagination": {
            "pageNo": 1,
            "pageSize": 10,
        }
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_tag_pagination(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "tags.amc_solar_o15952073792221_product = 'tA4ZSAFR' ",
        "projection": [
            "modelId",
            "name",
            "attributes",
            "measurepoints",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_attributeTags(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "attribute_tags.location = 'singapore' ",
        "projection": [
            "modelId",
            "name",
            "attributes",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_serviceTags(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "service_tags.function = 'toogle' ",
        "projection": [
            "modelId",
            "name",
            "services",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_eventTags(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "event_tags.type = 'temp' ",
        "projection": [
            "modelId",
            "name",
            "events",
            "modelIdPath",
            "orgId",
            "desc",
            "tags",
            "attributes",
            "measurepoints",
            "services",
        ]
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def searchmodel_noprojection(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "search", "orgId": orgId, 'scope': 1}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {
        "expression": "event_tags.type = 'temp' ",
    }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

