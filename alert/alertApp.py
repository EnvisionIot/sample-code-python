#Model Id can be found on EnOS portal (Go to Models under Model ID)
ModelId = "Python_Demo_Model"

Severity_ID = "Python_Severity_ID"
Type_ID = "Python_Type_ID"
Type_ID_Child = "Python_Type_ID_Child"
Content_ID = "Python_Content_ID"
Rule_ID = "Python_Rule_ID"

def alertGeneral(accessKey, secretKey, orgId, url):

    '''
    1. Alert Severity
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_severity.html
    '''
    # CreateAlertSeverity_py.createAlertSeverity(accessKey, secretKey, orgId, url)

    # DeleteAlertSeverity_py.deleteAlertSeverity(accessKey, secretKey, orgId, url)

    '''Search Alert Severity with pagination'''
    # SearchAlertSeverity_py.searchAlertSeverity(accessKey, secretKey, orgId, url)

    '''Search Alert Severity with expression using severityId'''
    # SearchAlertSeverity_py.searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, "severityId ='" + Severity_ID + "'")
    # SearchAlertSeverity_py.searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, "severityId in ('" + Severity_ID + "')")

    '''Search Alert Severity with expression using tags'''
    # SearchAlertSeverity_py.searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, "tags.SeverityKey1 = 'SeverityValue1'")
    # SearchAlertSeverity_py.searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, "severityId = 'Severity_ID' and tags.SeverityKey1 = 'SeverityValue1'")
    # SearchAlertSeverity_py.searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, "severityId = 'Severity_ID' or tags.SeverityKey1 = 'SeverityValue1'")
    # SearchAlertSeverity_py.searchAlertSeverity_Expression(accessKey, secretKey, orgId, url, "tags.SeverityKey1 = 'SeverityValue1' or tags.NewSeverityKey1 = 'NewSeverityValue1'")

    # UpdateAlertSeverity_py.updateAlertSeverity(accessKey, secretKey, orgId, url)

    '''
    2. Alert Type
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_type.html
    '''
    # CreateAlertType_py.createAlertType(accessKey, secretKey, orgId, url)
    # CreateAlertType_py.createAlertType_addParent(accessKey, secretKey, orgId, url)

    # DeleteAlertType_py.deleteAlertType(accessKey, secretKey, orgId, url)

    '''Search Alert Type with pagination'''
    # SearchAlertType_py.searchAlertType(accessKey, secretKey, orgId, url)

    '''Search Alert Type with expression using typeId'''
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "typeId ='" + Type_ID + "'")
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "typeId in ('" + Type_ID + "')")
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "typeId = 'Python_Type_ID' or typeId = 'Python_Type_ID_Child'")

    '''Search Alert Type with expression using parent typeId'''
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "parentTypeId ='" + Type_ID + "'")
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "parentTypeId in ('" + Type_ID + "')")

    '''Search Alert Type with expression using tags'''
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "tags.TypeKey1 = 'TypeValue1'")
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "typeId = 'Type_ID' and tags.TypeKey1 = 'TypeValue1'")
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "typeId = 'Python_Type_ID' or tags.TypeKey1 = 'TypeValue1'")
    # SearchAlertType_py.searchAlertType_Expression(accessKey, secretKey, orgId, url, "tags.TypeKey1 = 'TypeValue1' or tags.NewTypeKey1 = 'NewTypeValue1'")

    # UpdateAlertType_py.updateAlertType(accessKey, secretKey, orgId, url)
    # UpdateAlertType_py.updateAlertType_withParent(accessKey,secretKey, orgId, url)

    '''
    3. Alert Content
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_content.html
    '''
    # CreateAlertContent_py.createAlertContent(accessKey, secretKey, orgId, url)

    # GetAlertContent_py.getAlertContent(accessKey, secretKey, orgId, url)

    # DeleteAlertContent_py.deleteAlertContent(accessKey, secretKey, orgId, url)

    '''Search Alert Content with pagination'''
    # SearchAlertContent_py.searchAlertContent(accessKey, secretKey, orgId, url)

    '''Search Alert Content with model ID'''
    # SearchAlertContent_py.searchAlertContent_modelId(accessKey, secretKey, orgId, url)

    '''Search Alert Content with alert Type ID'''
    # SearchAlertContent_py.searchAlertContent_alertTypeId(accessKey, secretKey, orgId, url)

    '''Search Alert Content with sub Alert Type ID'''
    # SearchAlertContent_py.searchAlertContent_subAlertTypeId(accessKey, secretKey, orgId, url)

    '''Search Alert Content with expression using content ID'''
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentId ='" + Content_ID + "'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentId in ('" + Content_ID + "')")

    '''Search Alert Content with expression using model ID'''
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "modelId ='" + ModelId + "'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "modelId in ('" + ModelId + "')")

    '''Search Alert Content with expression using alert Type ID'''
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "alertTypeId ='" + Type_ID + "'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "alertTypeId in ('" + Type_ID + "')")

    '''Search Alert Content with expression using sub Alert Type ID'''
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "subAlertTypeId ='" + Type_ID + "'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "subAlertTypeId in ('" + Type_ID + "')")

    '''Search Alert Content with expression using contentDesc'''
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc like 'Default_Contents'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.default like 'Default_Contents'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.default like 'Default'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.en_US like 'Contents'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.zh_CN like '内容'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.zh_CN like '内'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.ja_JP like 'コンテンツ'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.ja_JP like 'ンツ'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.es_ES like 'Contenido'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentDesc.es_ES like 'Conten'")

    '''Search Alert Content with expression using tags'''
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "tags.ContentKey1 = 'ContentValue1'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "tags.NewContentKey1 = 'NewContentValue1'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "tags.ContentKey1 = 'ContentValue1' or  tags.NewContentKey1 = 'NewContentValue1'")
    # SearchAlertContent_py.searchAlertContent_Expression(accessKey, secretKey, orgId, url, "contentId = 'Python_Content_ID' and tags.ContentKey1 = 'ContentValue1'")

    # UpdateAlertContent_py.updateAlertContent(accessKey, secretKey, orgId, url)

    '''
    4. Alert Rule
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_rule.html
    '''
    # CreateAlertRule_py.createAlertRule(accessKey, secretKey, orgId, url)

    # CreateAlertRule_py.createAlertRule_measurepointIdCondition(accessKey, secretKey, orgId, url, "Python_Rule_ID1", "Int_MeasurementPoint", "${Int_MeasurementPoint} < 100")
    # CreateAlertRule_py.createAlertRule_measurepointIdCondition(accessKey, secretKey, orgId, url, "Python_Rule_ID2", "Int_MeasurementPoint", "(${Int_MeasurementPoint} < 100) and (${Int_MeasurementPoint} > 50)")
    # CreateAlertRule_py.createAlertRule_measurepointIdCondition(accessKey, secretKey, orgId, url, "Python_Rule_ID3", "Int_MeasurementPoint", "(${Int_MeasurementPoint} < 100) and (${Int_MeasurementPoint} > 50) and (${Int_MeasurementPoint} = 25)")
    # CreateAlertRule_py.createAlertRule_measurepointIdCondition(accessKey, secretKey, orgId, url, "Python_Rule_ID4", "Int_MeasurementPoint", "(${Int_MeasurementPoint} < 100) and ((${Int_MeasurementPoint} > 50) and (${Int_MeasurementPoint} = 25))")
    # CreateAlertRule_py.createAlertRule_deviceStatusCondition(accessKey, secretKey, orgId, url, "Python_Rule_ID5", "${Int_MeasurementPoint} < 100")
    # CreateAlertRule_py.createAlertRule_scope(accessKey, secretKey, orgId, url, "Python_Rule_ID6", "LlrLCZqt", "AvxV8hkR")

    # SearchAlertRule_py.searchAlertRule(accessKey, secretKey, orgId, url)
    # SearchAlertRule_py.searchAlertRule_modelId(accessKey, secretKey, orgId, url)
    # SearchAlertRule_py.searchAlertRule_measurepointId(accessKey, secretKey, orgId, url)

    '''Search Alert Rule with expression using rule ID'''
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "ruleId ='" + Rule_ID + "'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "ruleId in ('" + Rule_ID + "')")

    '''Search Alert Rule with expression using model ID'''
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "modelId ='" + ModelId + "'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "modelId in ('" + ModelId + "')")

    '''Search Alert Rule with expression using measure point ID'''
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "measurepointId  = 'Int_MeasurementPoint'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "measurepointId  in ('Int_MeasurementPoint')")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "measurepointId  is null")

    '''Search Alert Rule with expression using device status'''
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "deviceStatus ='offline'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline')")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "deviceStatus is null")

    '''Search Alert Rule with expression using tags'''
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "tags.RuleKey1 = 'RuleValue1'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "tags.NewRuleKey1 = 'NewRuleValue1'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "tags.RuleKey1 = 'RuleValue1' or  tags.NewRuleKey1 = 'NewRuleValue1'")
    # SearchAlertRule_py.searchAlertRule_Expression(accessKey, secretKey, orgId, url, "ruleId = 'Python_Rule_ID' and tags.RuleKey1 = 'RuleValue1'")

    # UpdateAlertRule_py.updateAlertRule_measurepointId(accessKey, secretKey, orgId, url)
    # UpdateAlertRule_py.updateAlertRule_deviceStatus(accessKey, secretKey, orgId, url)

    # DeleteAlertRule_py.deleteAlertRule(accessKey, secretKey, orgId, url)
    # for i in range(6):
    #     print("Python_Rule_ID" + str(i+1))
    #     DeleteAlertRule_py.deleteAlertRule_ruleId(accessKey, secretKey, orgId, url, "Python_Rule_ID" + str(i+1))

    '''

    5. Alert Record - New Version
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/index_alert_record_new.html
    '''

    '''
    5.1 History & Active Alert Records
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_alert_tag.html
    '''
    # CreateAlert_py.createAlert_ActiveAlert(accessKey, secretKey, orgId, url)
    # CreateAlert_py.createAlert_HistoryAlert(accessKey, secretKey, orgId, url)

    # BatchCreateAlerts_py.batchCreateAlert_ActiveAlert(accessKey, secretKey, orgId, url)
    # BatchCreateAlerts_py.batchCreateAlert_HistoryAlert(accessKey, secretKey, orgId, url)
    # BatchCreateAlerts_py.batchCreateAlert_mix(accessKey, secretKey, orgId, url)

    '''Search Alerts with pagination'''
    # SearchAlerts_py.searchAlerts(accessKey, secretKey, orgId, url)

    '''Search Alerts with instance ID'''
    # SearchAlerts_py.searchAlerts_instanceId(accessKey, secretKey, orgId, url)

    '''Search Alerts with metric ID'''
    # SearchAlerts_py.searchAlerts_metricId(accessKey, secretKey, orgId, url)

    '''Search Alerts with startRecoverTime and endRecoverTime'''
    # SearchAlerts_py.searchAlerts_recoverTime(accessKey, secretKey, orgId, url)

    '''Search Alerts with active status(Active or History Alerts)'''
    # Active Alert
    # SearchAlerts_py.searchAlerts_active(accessKey, secretKey, orgId, url, "true")
    # History Alert
    # SearchAlerts_py.searchAlerts_active(accessKey, secretKey, orgId, url, "false")
    # Both Active and History Alert
    # SearchAlerts_py.searchAlerts_active(accessKey, secretKey, orgId, url, "null")

    '''Search Alerts with expression using instance ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "instanceId = 'AvxV8hkR'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "instanceId in ( 'AvxV8hkR', 'ActiveAlert_instanceId')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "instanceId != 'AvxV8hkR'")

    '''Search Alerts with expression using metric ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricId = 'Int_MeasurementPoint'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricId in ( 'Int_MeasurementPoint', 'ActiveAlert_metricId')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricId != 'Int_MeasurementPoint'")

    '''Search Alerts with expression using severity ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "severityId = 'AA_newver_severityId'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "severityId in ( 'AA_newver_severityId', 'HA_newver_severityId')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "severityId != 'AA_newver_severityId'")

    '''Search Alerts with expression using type ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "typeId = 'AA_newver_typeId'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "typeId in ( 'AA_newver_typeId', 'HA_newver_typeId 1')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "typeId != 'AA_newver_typeId 1'")

    '''Search Alerts with expression using parent type ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "parentTypeId = 'parentTypeId'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "parentTypeId in ( 'parentTypeId', 'parentTypeId1')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "parentTypeId != 'parentTypeId'")

    '''Search Alerts with expression using content ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "contentId = 'AA_newver_contentId'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "contentId in ( 'AA_newver_contentId', 'yourContentId 1')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "contentId != 'AA_newver_contentId'")

    '''Search Alerts with expression using rule ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleId = 'AA_newver_ruleId'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleId in ( 'AA_newver_ruleId', 'HA_newver_ruleId')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleId != 'AA_newver_ruleId'")

    '''Search Alerts with expression using event type'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "eventType = 2")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "eventType in ( 2, 3)")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "eventType != 2")

    '''Search Alerts with expression using alert ID'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "alertId = '20220218c6636aac668c34de07e9a4f494a3f06f'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "alertId in ( '20220218c6636aac668c34de07e9a4f494a3f06f', '202202183b7c8f7dd021ebd35f873dd196994460')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "alertId != '20220218c6636aac668c34de07e9a4f494a3f06f'")

    '''Search Alerts with expression using metric tags'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 = 'ActiveAlertMetricTagValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 in ( 'ActiveAlertMetricTagValue1', 'ActiveAlertMetricTagValue2')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 != 'Alert ActiveAlertMetricTagValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 like 'ActiveAlertMetricTagValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "exists(metricTags.ActiveAlertMetricTagKey1)")

    '''Search Alerts with expression using rule tags'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 = 'ActiveAlertRuletagValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 in ( 'ActiveAlertRuletagValue1', 'ActiveAlertRuletagValue2')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 != 'ActiveAlertRuletagValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 like 'ActiveAlertRuletagValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "exists(ruleTags.ActiveAlertRuletagKey1)")

    '''Search Alerts with expression using tags'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 = 'ActiveAlert_newverValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 in ( 'ActiveAlert_newverValue1', 'ActiveAlert_newverValue2')")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 != 'ActiveAlert_newverValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 like 'ActiveAlert_newverValue1'")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "exists(tags.ActiveAlert_newverKey1)")

    '''Search Alerts with expression using inhibited'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "inhibited = true")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "inhibited = false")
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "inhibited != true")

    '''Search Alerts with expression using maskedBy'''
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "maskedBy = 'test' ")

    # CloseAlert_py.closeActiveAlert(accessKey, secretKey, orgId, url, "202202182d6ec4d749637cbbc5b73ff54d77ee1b")

    '''Incomplete'''
    '''Scroll Alerts'''
    # ScrollAlerts_py.scrollAlerts(accessKey, secretKey, orgId, url)

    '''Scroll Alerts with instance ID'''
    # ScrollAlerts_py.scrollAlerts_instanceId(accessKey, secretKey, orgId, url)

    '''Scroll Alerts with metric ID'''
    # ScrollAlerts_py.scrollAlerts_metricId(accessKey, secretKey, orgId, url)

    '''Scroll Alerts with startRecoverTime and endRecoverTime'''
    # ScrollAlerts_py.scrollAlerts_recoverTime(accessKey, secretKey, orgId, url)

    '''Scroll Alerts with active status(Active or History Alerts)'''
    # Active Alert
    # ScrollAlerts_py.scrollAlerts_active(accessKey, secretKey, orgId, url, "true")
    # History Alert
    # ScrollAlerts_py.scrollAlerts_active(accessKey, secretKey, orgId, url, "false")
    # Both Active and History Alert
    # ScrollAlerts_py.scrollAlerts_active(accessKey, secretKey, orgId, url, "null")

    '''Scroll Alerts with expression using instance ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "instanceId = 'AvxV8hkR'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "instanceId in ( 'AvxV8hkR', 'ActiveAlert_instanceId')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "instanceId != 'AvxV8hkR'")

    '''Scroll Alerts with expression using metric ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricId = 'Int_MeasurementPoint'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricId in ( 'Int_MeasurementPoint', 'ActiveAlert_metricId')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricId != 'Int_MeasurementPoint'")

    '''Scroll Alerts with expression using severity ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "severityId = 'AA_newver_severityId'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "severityId in ( 'AA_newver_severityId', 'HA_newver_severityId')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "severityId != 'AA_newver_severityId'")

    '''Scroll Alerts with expression using type ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "typeId = 'AA_newver_typeId'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "typeId in ( 'AA_newver_typeId', 'HA_newver_typeId 1')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "typeId != 'AA_newver_typeId 1'")

    '''Scroll Alerts with expression using parent type ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "parentTypeId = 'parentTypeId'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "parentTypeId in ( 'parentTypeId', 'parentTypeId1')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "parentTypeId != 'parentTypeId'")

    '''Scroll Alerts with expression using content ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "contentId = 'AA_newver_contentId'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "contentId in ( 'AA_newver_contentId', 'yourContentId 1')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "contentId != 'AA_newver_contentId'")

    '''Scroll Alerts with expression using rule ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleId = 'AA_newver_ruleId'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleId in ( 'AA_newver_ruleId', 'HA_newver_ruleId')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleId != 'AA_newver_ruleId'")

    '''Scroll Alerts with expression using event type'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "eventType = 2")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "eventType in ( 2, 3)")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "eventType != 2")

    '''Scroll Alerts with expression using alert ID'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "alertId = '20220218c6636aac668c34de07e9a4f494a3f06f'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "alertId in ( '20220218c6636aac668c34de07e9a4f494a3f06f', '202202183b7c8f7dd021ebd35f873dd196994460')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "alertId != '20220218c6636aac668c34de07e9a4f494a3f06f'")

    '''Scroll Alerts with expression using metric tags'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 = 'ActiveAlertMetricTagValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 in ( 'ActiveAlertMetricTagValue1', 'ActiveAlertMetricTagValue2')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 != 'Alert ActiveAlertMetricTagValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "metricTags.ActiveAlertMetricTagKey1 like 'ActiveAlertMetricTagValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "exists(metricTags.ActiveAlertMetricTagKey1)")

    '''Scroll Alerts with expression using rule tags'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 = 'ActiveAlertRuletagValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 in ( 'ActiveAlertRuletagValue1', 'ActiveAlertRuletagValue2')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 != 'ActiveAlertRuletagValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "ruleTags.ActiveAlertRuletagKey1 like 'ActiveAlertRuletagValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "exists(ruleTags.ActiveAlertRuletagKey1)")

    '''Scroll Alerts with expression using tags'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 = 'ActiveAlert_newverValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 in ( 'ActiveAlert_newverValue1', 'ActiveAlert_newverValue2')")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 != 'ActiveAlert_newverValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "tags.ActiveAlert_newverKey1 like 'ActiveAlert_newverValue1'")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "exists(tags.ActiveAlert_newverKey1)")

    '''Scroll Alerts with expression using inhibited'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "inhibited = true")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "inhibited = false")
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "inhibited != true")

    '''Scroll Alerts with expression using maskedBy'''
    # ScrollAlerts_py.scrollAlerts_Expression(accessKey, secretKey, orgId, url, "maskedBy = 'test' ")

    '''
    5.2 Alert Tags
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/index_alert_tag.html
    '''
    # UpdateAlertTags_py.updateAlertTags(accessKey, secretKey, orgId, url, "20220218da6bbf975612b3714ab75970306e60b8")
    # SearchAlerts_py.searchAlerts_Expression(accessKey,secretKey, orgId, url, "alertId = '20220218da6bbf975612b3714ab75970306e60b8'")

    # alertId_list = ["20220218a4c5b2ba6d1be54336ba602dd46c805f", "202202188208c33af535209da6f97b0aef839428", "20220218c6636aac668c34de07e9a4f494a3f06f"]
    # BatchUpdateAlertTags_py.batchUpdateAlertTags(accessKey, secretKey, orgId, url, alertId_list)
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "alertId in " + str(tuple(alertId_list)))





