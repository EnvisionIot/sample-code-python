import poseidon.poseidon
from requests.models import PreparedRequest


def updateThingModel(accessKey, secretKey, orgId, url):
    accessURL = url + '/model-service/v2.1/thing-models'
    params = {"action": "update", "orgId": orgId, "isPatchUpdate": "false"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    body = {
        "modelId": "yourModelId",
        "name": {
            "defaultValue": "Device Name",
            "i18nValue": {
                "zh_CN": "设备名称",
                "en_US": "Device Name"
            }
        },
        "desc": "jw-1112",
        "category": "system",
        "tags": {
            "group": "1"
        },
        "attributes": {
            "capacity": {
                "identifier": "capacity",
                "name": {
                    "defaultValue": "capacity",
                    "i18nValue": {
                        "en_US": "capacity",
                        "zh_CN": "容量"
                    }
                },
                "desc": "Capacity",
                "i18nDesc": {
                    "defaultValue": "Capacity description",
                    "i18nValue": {
                        "en_US": "Capacity description",
                        "zh_CN": "容量描述"
                    }
                },
                "tags": {
                    "cap": "1"
                },
                "stdElementId": "urn:user:modelelement:std:atom-property-int:1.0",
                "isStdElement": True,
                "dataType": "INT",
                "unit": {
                    "unitId": "G",
                    "multiplier": "ONE"
                },
                "isRequired": True,
                "defaultValue": 111
            }
        },
        "measurepoints": {
            "ActiveSC": {
                "identifier": "ActiveSC",
                "name": {
                    "defaultValue": "活动状态字",
                    "i18nValue": {
                        "en_US": "ActiveSC_Name"
                    }
                },
                "desc": "ActiveSC desc",
                "i18nDesc": {
                    "defaultValue": "ActiveSC desc",
                    "i18nValue": {
                        "en_US": "ActiveSC desc",
                        "zh_CN": "活动状态描述"
                    }
                },
                "tags": {},
                "isStdElement": False,
                "dataType": "INT",
                "hasQuality": False,
                "signalType": "DI"
            }
        },
        "services": {
            "speedup": {
                "identifier": "speedup",
                "name": {
                    "defaultValue": "speedup",
                    "i18nValue": {
                        "en_US": "speedup"
                    }
                },
                "desc": "Speedup",
                "i18nDesc": {
                    "defaultValue": "Speedup",
                    "i18nValue": {
                        "en_US": "Speedup",
                        "zh_CN": "加速"
                    }
                },
                "isStdElement": False,
                "outputData": [
                    {
                        "identifier": "delta",
                        "name": {
                            "defaultValue": "delta",
                            "i18nValue": {
                                "en_US": "delta"
                            }
                        },
                        "desc": "Delta",
                        "i18nDesc": {
                            "defaultValue": "Delta",
                            "i18nValue": {
                                "en_US": "Delta",
                                "zh_CN": "Delta 描述"
                            }
                        },
                        "tags": {},
                        "isStdElement": False,
                        "dataType": "INT",
                    }
                ],
                "inputData": [
                    {
                        "identifier": "delta",
                        "name": {
                            "defaultValue": "delta",
                            "i18nValue": {
                                "en_US": "delta"
                            }
                        },
                        "desc": "Delta",
                        "i18nDesc": {
                            "defaultValue": "Delta",
                            "i18nValue": {
                                "en_US": "Delta",
                                "zh_CN": "Delta 描述"
                            }
                        },
                        "tags": {},
                        "isStdElement": False,
                        "dataType": "INT",
                        "unit": {
                            "unitId": "rpm",
                            "multiplier": "ONE"
                        },
                    }
                ],
                "callType": "ASYNC"
            }
        },
        "events": {
            "alert": {
                "identifier": "alert",
                "name": {
                    "defaultValue": "alert",
                    "i18nValue": {
                        "en_US": "alert"
                    }
                },
                "desc": "Alert",
                "i18nDesc": {
                    "defaultValue": "Alert",
                    "i18nValue": {
                        "en_US": "Alert",
                        "zh_CN": "告警"
                    }
                },
                "isStdElement": False,
                "outputData": [
                    {
                        "identifier": "event1",
                        "name": {
                            "defaultValue": "event1",
                            "i18nValue": {
                                "en_US": "event1"
                            }
                        },
                        "desc": "Event 1",
                        "i18nDesc": {
                            "defaultValue": "Event 1",
                            "i18nValue": {
                                "en_US": "Event 1",
                                "zh_CN": "事件"
                            }
                        },
                        "tags": {},
                        "isStdElement": False,
                        "dataType": "INT",
                    }
                ],
                "eventType": "ERROR"
            }
        }
    }
    print(body)
    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)