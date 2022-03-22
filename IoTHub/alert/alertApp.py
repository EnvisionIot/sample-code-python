import IoTHub.alert.severity.createAlertSeverity as CreateAlertSeverity_py
import IoTHub.alert.severity.deleteAlertSeverity as DeleteAlertSeverity_py
import IoTHub.alert.severity.searchAlertSeverity as SearchAlertSeverity_py
import IoTHub.alert.severity.updateAlertSeverity as UpdateAlertSeverity_py
import IoTHub.alert.type.createAlertType as CreateAlertType_py
import IoTHub.alert.type.deleteAlertType as DeleteAlertType_py
import IoTHub.alert.type.searchAlertType as SearchAlertType_py
import IoTHub.alert.type.updateAlertType as UpdateAlertType_py
import IoTHub.alert.content.createAlertContent as CreateAlertContent_py
import IoTHub.alert.content.deleteAlertContent as DeleteAlertContent_py
import IoTHub.alert.content.getAlertContent as GetAlertContent_py
import IoTHub.alert.content.searchAlertContent as SearchAlertContent_py
import IoTHub.alert.content.updateAlertContent as UpdateAlertContent_py
import IoTHub.alert.rule.createAlertRule as CreateAlertRule_py
import IoTHub.alert.rule.deleteAlertRule as DeleteAlertRule_py
import IoTHub.alert.rule.searchAlertRule as SearchAlertRule_py
import IoTHub.alert.rule.updateAlertRule as UpdateAlertRule_py
import IoTHub.alert.record.old.activeAlertRecord.aggregateActiveAlerts as AggregateActiveAlerts_py
import IoTHub.alert.record.old.activeAlertRecord.closeActiveAlert as CloseActiveAlert_py
import IoTHub.alert.record.old.activeAlertRecord.createActiveAlert as CreateActiveAlert_py
import IoTHub.alert.record.old.activeAlertRecord.createActiveAlertBatch as CreateActiveAlertBatch_py
import IoTHub.alert.record.old.activeAlertRecord.deleteActiveAlert as DeleteActiveAlert_py
import IoTHub.alert.record.old.activeAlertRecord.searchActiveAlerts as SearchActiveAlerts_py
import IoTHub.alert.record.old.historyAlertRecord.createHistoryAlert as CreateHistoryAlert_py
import IoTHub.alert.record.old.historyAlertRecord.createHistoryAlertBatch as CreateHistoryAlertBatch_py
import IoTHub.alert.record.old.historyAlertRecord.searchHistoryAlerts as SearchHistoryAlerts_py
import IoTHub.alert.record.old.historyAlertRecord.scrollHistoryAlerts as ScrollHistoryAlerts_py
import IoTHub.alert.record.old.alertTags.updateActiveAlertTags as UpdateActiveAlertTags_py
import IoTHub.alert.record.old.alertTags.batchUpdateActiveAlertTags as BatchUpdateActiveAlertTags_py
import IoTHub.alert.record.old.alertTags.updateHistoryAlertTags as UpdateHistoryAlertTags_py
import IoTHub.alert.record.new.historyAndActiveAlertRecords.createAlert as CreateAlert_py
import IoTHub.alert.record.new.historyAndActiveAlertRecords.batchCreateAlerts as BatchCreateAlerts_py
import IoTHub.alert.record.new.historyAndActiveAlertRecords.searchAlerts as SearchAlerts_py
import IoTHub.alert.record.new.historyAndActiveAlertRecords.closeAlert as CloseAlert_py
import IoTHub.alert.record.new.historyAndActiveAlertRecords.scrollAlerts as ScrollAlerts_py
import IoTHub.alert.record.new.alertTags.updateAlertTags as UpdateAlertTags_py
import IoTHub.alert.record.new.alertTags.batchUpdateAlertTags as BatchUpdateAlertTags_py

import time

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
    5. Alert Record - Old Version
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_alert_record_old.html
    '''

    '''
    5.1 Active Alert Record
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_active_alert.html
    '''
    # alertId_measurepointId = CreateActiveAlert_py.createActiveAlert_measurepointId(accessKey, secretKey, orgId, url)
    # alertId_deviceStatus = CreateActiveAlert_py.createActiveAlert_deviceStatus(accessKey, secretKey, orgId, url)

    # alertId_measurepointIdBatch = CreateActiveAlertBatch_py.createActiveAlertBatch_measurepointId(accessKey, secretKey, orgId, url)
    # alertId_deviceStatusBatch = CreateActiveAlertBatch_py.createActiveAlertBatch_deviceStatus(accessKey, secretKey, orgId, url)
    # alertId_mixBatch = CreateActiveAlertBatch_py.createActiveAlertBatch_mix(accessKey,secretKey, orgId, url)

    # DeleteActiveAlert_py.deleteActiveAlert(accessKey, secretKey, orgId, url, "202202170473a2db0b15bd8ea731577f5b3a9098")
    # DeleteActiveAlert_py.deleteActiveAlert(accessKey, secretKey, orgId, url, alertId_measurepointId)
    # DeleteActiveAlert_py.deleteActiveAlert(accessKey, secretKey, orgId, url, alertId_deviceStatus)

    # for id in alertId_measurepointIdBatch:
    #     DeleteActiveAlert_py.deleteActiveAlert(accessKey, secretKey, orgId, url, id)

    # for id in alertId_deviceStatusBatch:
    #     DeleteActiveAlert_py.deleteActiveAlert(accessKey, secretKey, orgId, url, id)

    # for id in alertId_mixBatch:
    #     DeleteActiveAlert_py.deleteActiveAlert(accessKey, secretKey, orgId, url, id)

    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "contentId")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "assetId")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "modelId")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "measurepointId")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "severityId")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "typeId")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_groupByField(accessKey, secretKey, orgId, url, "subTypeId")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, "2020-12-31 12:00:00", "2021-12-31 12:00:00")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, "2020-12-31 12:00:00")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, endTime = "2022-12-31 12:00:00")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus = 'offline'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus != 'offline'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "modelId = 'Python_Demo_Model'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "modelId in ('Python_Demo_Model','demo_lift_model')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "modelId != 'Python_Demo_Model'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetId = 'AvxV8hkR'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetId in ('AvxV8hkR','0EbRVlqx')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetId != 'AvxV8hkR'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId = 'Int_MeasurementPoint'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId in ('Int_MeasurementPoint','temp')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId != 'Int_MeasurementPoint'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "severityId = 'AA_severityId'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "severityId in ('AA_severityId','Warning')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "severityId != 'AA_severityId'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "typeId = 'AA_typeId'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "typeId in ('AA_typeId','type')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "typeId != 'AA_typeId'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId = 'AA_subTypeId'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId in ('AA_subTypeId','subtype')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId != 'AA_subTypeId'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "contentId = 'AA_contentId'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "contentId in ('AA_contentId','contentId 1')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "contentId != 'AA_contentId'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventType = 3")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventType in (3, 1)")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventType != 3")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId = '20220216bda8a9d8e1594910e3296da7e3e8281f'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId in ('20220216bda8a9d8e1594910e3296da7e3e8281f','20220118243abcea80961167d6b876a87a116977')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId != '20220216bda8a9d8e1594910e3296da7e3e8281f'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId = '100765'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId in ('100765','100754')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId != '100765'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetPath like 'assetIdx'")

    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "tag.ActiveAlertKey1 = 'ActiveAlertValue1'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "tag.ActiveAlertKey1 in ('ActiveAlertValue1','tag')")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "tag.ActiveAlertKey1 != 'ActiveAlertValue10'")
    # AggregateActiveAlerts_py.aggregateActiveAlerts_Expression(accessKey, secretKey, orgId, url, "exists(tag.ActiveAlertKey1)")

    '''Search Active Alerts with pagination'''
    # SearchActiveAlerts_py.searchActiveAlerts(accessKey, secretKey, orgId, url)

    '''Search Active Alerts with model ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_modelId(accessKey, secretKey, orgId, url)

    '''Search Active Alerts with asset ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_assetId(accessKey, secretKey, orgId, url)

    '''Search Active Alerts with measurepoint ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_measurepointId(accessKey, secretKey, orgId, url)

    '''Search Active Alerts with startOccurTime and endOccurTime'''
    # SearchActiveAlerts_py.searchActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, "2020-12-31 12:00:00", "2021-12-31 12:00:00")
    # SearchActiveAlerts_py.searchActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, "2020-12-31 12:00:00")
    # SearchActiveAlerts_py.searchActiveAlerts_TimeRange(accessKey, secretKey, orgId, url, endTime = "2022-12-31 12:00:00")

    '''Search Active Alerts with expression using deviceStatus'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus = 'offline'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline', 'online')")

    '''Search Active Alerts with expression using model ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "modelId = 'Python_Demo_Model'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "modelId in ('Python_Demo_Model','demo_lift_model')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "modelId != 'Python_Demo_Model'")

    '''Search Active Alerts with expression using asset ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetId = 'AvxV8hkR'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetId in ('AvxV8hkR','0EbRVlqx')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetId != 'AvxV8hkR'")

    '''Search Active Alerts with expression using measurepoint ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId = 'Int_MeasurementPoint'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId in ('Int_MeasurementPoint','temp')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId != 'Int_MeasurementPoint'")

    '''Search Active Alerts with expression using severity ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "severityId = 'AA_severityId'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "severityId in ('AA_severityId','Warning')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "severityId != 'AA_severityId'")

    '''Search Active Alerts with expression using type ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "typeId = 'AA_typeId'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "typeId in ('AA_typeId','type')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "typeId != 'AA_typeId'")

    '''Search Active Alerts with expression using subtype ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId = 'AA_subTypeId'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId in ('AA_subTypeId','subtype')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId != 'AA_subTypeId'")

    '''Search Active Alerts with expression using content ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "contentId = 'AA_contentId'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "contentId in ('AA_contentId','contentId 1')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "contentId != 'AA_contentId'")

    '''Search Active Alerts with expression using event type'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventType = 3")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventType in (3, 1)")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventType != 3")

    '''Search Active Alerts with expression using event ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId = '20220216bda8a9d8e1594910e3296da7e3e8281f'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId in ('20220216bda8a9d8e1594910e3296da7e3e8281f','20220118243abcea80961167d6b876a87a116977')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId != '20220216bda8a9d8e1594910e3296da7e3e8281f'")

    '''Search Active Alerts with expression using tree ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "treeId = 'LlrLCZqt'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "treeId in ('LlrLCZqt','U22GDyrC')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "treeId != 'LlrLCZqt'")

    '''Search Active Alerts with expression using hitRule ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId = '100765'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId in ('100765','100754')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId != '100765'")

    '''Search Active Alerts with expression using asset path'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "assetPath like 'assetIdx'")

    '''Search Active Alerts with expression using tag'''
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "tag.ActiveAlertKey1 = 'ActiveAlertValue1'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "tag.ActiveAlertKey1 in ('ActiveAlertValue1','tag')")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "tag.ActiveAlertKey1 != 'ActiveAlertValue10'")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "exists(tag.ActiveAlertKey1)")

    '''Search Active Alerts with scope using tree ID and asset ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt")
    # SearchActiveAlerts_py.searchActiveAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt", "AvxV8hkR", True)
    # SearchActiveAlerts_py.searchActiveAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt", includeDerivative=True)

    '''Search Active Alerts with Root Alert using event ID'''
    # SearchActiveAlerts_py.searchActiveAlerts_RootAlert(accessKey, secretKey, orgId, url, "20220216bda8a9d8e1594910e3296da7e3e8281f")
    # SearchActiveAlerts_py.searchActiveAlerts_RootAlert(accessKey, secretKey, orgId, url, "20220216bda8a9d8e1594910e3296da7e3e8281f", "LlrLCZqt")

    # close_eventId = CreateActiveAlert_py.createActiveAlert_measurepointId(accessKey, secretKey, orgId, url)
    # CloseActiveAlert_py.closeActiveAlert(accessKey, secretKey, orgId, url, close_eventId)

    '''
    5.2 History Alert Record
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_history_alert.html
    '''

    # CreateHistoryAlert_py.createHistoryAlert_measurepointId(accessKey, secretKey, orgId, url)
    # CreateHistoryAlert_py.createHistoryAlert_deviceStatus(accessKey, secretKey, orgId, url)

    # CreateHistoryAlertBatch_py.createHistoryAlertBatch_measurepointId(accessKey, secretKey, orgId, url)

    # CreateHistoryAlertBatch_py.createHistoryAlertBatch_deviceStatus(accessKey, secretKey, orgId, url)

    # CreateHistoryAlertBatch_py.createHistoryAlertBatch_mix(accessKey, secretKey, orgId, url)

    '''Search History Alerts with pagination'''
    # SearchHistoryAlerts_py.searchHistoryAlerts(accessKey, secretKey, orgId, url)

    '''Search History Alerts with model ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_modelId(accessKey, secretKey, orgId, url)

    '''Search History Alerts with asset ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_assetId(accessKey, secretKey, orgId, url)

    '''Search History Alerts with measurepoint ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_measurepointId(accessKey, secretKey, orgId, url)

    '''Search History Alerts with recoverStartTime and recoverEndTime'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_recoverTime(accessKey, secretKey, orgId, url)

    '''Search History Alerts with Expression using deviceStatus'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus = 'offline'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline', 'online')")

    '''Search History Alerts with Expression using model ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "modelId = 'Python_Demo_Model'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "modelId in ('Python_Demo_Model','demo_lift_model')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "modelId != 'Python_Demo_Model'")

    '''Search History Alerts with Expression using asset ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetId = 'AvxV8hkR'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetId in ('AvxV8hkR','32CDx7FU')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetId != 'AvxV8hkR'")

    '''Search History Alerts with Expression using measurepoint ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId = 'Int_MeasurementPoint'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId in ('Int_MeasurementPoint','temp')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId != 'Int_MeasurementPoint'")

    '''Search History Alerts with Expression using severity ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "severityId = 'HA_severityId'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "severityId in ('HA_severityId','AA_severityId')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "severityId != 'HA_severityId'")

    '''Search History Alerts with Expression using type ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "typeId = 'HA_typeId'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "typeId in ('HA_typeId','AA_typeId')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "typeId != 'HA_typeId'")

    '''Search History Alerts with Expression using subtype ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId = 'HA_subTypeId'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId in ('HA_subTypeId','AA_subTypeId')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId != 'HA_subTypeId'")

    '''Search History Alerts with Expression using content ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "contentId = 'HA_contentId'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "contentId in ('HA_contentId','AA_contentId')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "contentId != 'HA_contentId'")

    '''Search History Alerts with Expression using event type'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventType = 3")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventType in (3, 1)")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventType != 3")

    '''Search History Alerts with Expression using event ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId = '20220217251d703a8813bea81be069bb720871fe'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId in ('20220217251d703a8813bea81be069bb720871fe','202202174f4d5ca18aedf6c03275b5fb5531978b')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId != '20220217251d703a8813bea81be069bb720871fe'")

    '''Search History Alerts with Expression using tree ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "treeId = 'LlrLCZqt'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "treeId in ('LlrLCZqt','U22GDyrC')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "treeId != 'LlrLCZqt'")

    '''Search History Alerts with Expression using hitrule ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId = '100765'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId in ('100765','100754')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId != '100765'")

    '''Search History Alerts with Expression using asset path'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetPath like 'assetIdx'")

    '''Search History Alerts with Expression using tag'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "tag.HistoryAlertKey1 = 'HistoryAlertValue1'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "tag.HistoryAlertKey1 in ('HistoryAlertValue1','tag')")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "tag.HistoryAlertKey1 != 'HistoryAlertValue10'")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "exists(tag.HistoryAlertKey1)")

    '''Search History Alerts with Scope using treeID and asset ID'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt", "AvxV8hkR", True)
    # SearchHistoryAlerts_py.searchHistoryAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt", includeDerivative=True)

    '''Search History Alerts with RootAlert'''
    # SearchHistoryAlerts_py.searchHistoryAlerts_RootAlert(accessKey, secretKey, orgId, url, "20220217251d703a8813bea81be069bb720871fe")
    # SearchHistoryAlerts_py.searchHistoryAlerts_RootAlert(accessKey, secretKey, orgId, url, "20220217251d703a8813bea81be069bb720871fe", "LlrLCZqt")

    '''Incomplete'''
    '''Scroll History Alerts'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts(accessKey, secretKey, orgId, url)

    '''Scroll History Alerts with model ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_modelId(accessKey, secretKey, orgId, url)

    '''Scroll History Alerts with asset ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_assetId(accessKey, secretKey, orgId, url)

    '''Scroll History Alerts with measurepoint ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_measurepointsId(accessKey, secretKey, orgId, url)

    '''Scroll History Alerts with recoverStartTime and recoverEndTime'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_recoverTime(accessKey, secretKey, orgId, url)

    '''Scroll History Alerts with Expression using deviceStatus'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus = 'offline'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "deviceStatus in ('offline', 'online')")

    '''Scroll History Alerts with Expression using model ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "modelId = 'Python_Demo_Model'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "modelId in ('Python_Demo_Model','demo_lift_model')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "modelId != 'Python_Demo_Model'")

    '''Scroll History Alerts with Expression using asset ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetId = 'AvxV8hkR'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetId in ('AvxV8hkR','32CDx7FU')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetId != 'AvxV8hkR'")

    '''Scroll History Alerts with Expression using measurepoint ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId = 'Int_MeasurementPoint'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId in ('Int_MeasurementPoint','temp')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "measurepointId != 'Int_MeasurementPoint'")

    '''Scroll History Alerts with Expression using severity ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "severityId = 'HA_severityId'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "severityId in ('HA_severityId','AA_severityId')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "severityId != 'HA_severityId'")

    '''Scroll History Alerts with Expression using type ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "typeId = 'HA_typeId'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "typeId in ('HA_typeId','AA_typeId')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "typeId != 'HA_typeId'")

    '''Scroll History Alerts with Expression using subtype ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId = 'HA_subTypeId'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId in ('HA_subTypeId','AA_subTypeId')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "subTypeId != 'HA_subTypeId'")

    '''Scroll History Alerts with Expression using content ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "contentId = 'HA_contentId'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "contentId in ('HA_contentId','AA_contentId')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "contentId != 'HA_contentId'")

    '''Scroll History Alerts with Expression using event type'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventType = 3")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventType in (3, 1)")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventType != 3")

    '''Scroll History Alerts with Expression using event ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId = '20220217251d703a8813bea81be069bb720871fe'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId in ('20220217251d703a8813bea81be069bb720871fe','202202174f4d5ca18aedf6c03275b5fb5531978b')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId != '20220217251d703a8813bea81be069bb720871fe'")

    '''Scroll History Alerts with Expression using tree ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "treeId = 'LlrLCZqt'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "treeId in ('LlrLCZqt','U22GDyrC')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "treeId != 'LlrLCZqt'")

    '''Scroll History Alerts with Expression using hitrule ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId = '100765'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId in ('100765','100754')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "hitRuleId != '100765'")

    '''Scroll History Alerts with Expression using asset path'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "assetPath like 'assetIdx'")

    '''Scroll History Alerts with Expression using tag'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "tag.HistoryAlertKey1 = 'HistoryAlertValue1'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "tag.HistoryAlertKey1 in ('HistoryAlertValue1','tag')")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "tag.HistoryAlertKey1 != 'HistoryAlertValue10'")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "exists(tag.HistoryAlertKey1)")

    '''Scroll History Alerts with Scope using treeID and asset ID'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt", "AvxV8hkR", True)
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_Scope(accessKey, secretKey, orgId, url, "LlrLCZqt", includeDerivative=True)

    '''Scroll History Alerts with RootAlert'''
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_RootAlert(accessKey, secretKey, orgId, url, "20220217251d703a8813bea81be069bb720871fe")
    # ScrollHistoryAlerts_py.scrollHistoryAlerts_RootAlert(accessKey, secretKey, orgId, url, "20220217251d703a8813bea81be069bb720871fe", "LlrLCZqt")


    '''
    5.3 Alert Tags
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/index_alert_tag.html
    '''
    # UpdateActiveAlertTags_py.updateActiveAlertTags(accessKey, secretKey, orgId, url, "2022021779042097cd896fa6b16b56f8f96df9a4")
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey,secretKey, orgId, url, "eventId = '2022021779042097cd896fa6b16b56f8f96df9a4'")

    # UpdateHistoryAlertTags_py.updateHistoryAlertTags(accessKey, secretKey, orgId, url, "2022021702889da0ba242c4555de1cf79235e615")
    # SearchHistoryAlerts_py.searchHistoryAlerts_Expression(accessKey, secretKey, orgId, url, "eventId = '2022021702889da0ba242c4555de1cf79235e615'")

    # eventId_list = ["2022021779042097cd896fa6b16b56f8f96df9a4", "20220217b3dc06039e038602cef608b5ff2c7a72", "20220217ad40a5469adee2ba27cc01b9fb76e2aa"]
    # BatchUpdateActiveAlertTags_py.batchUpdateActiveAlertTags(accessKey, secretKey, orgId, url, eventId_list)
    # SearchActiveAlerts_py.searchActiveAlerts_Expression(accessKey, secretKey, orgId, url, "eventId in " + str(tuple(eventId_list)))

    '''
    6. Alert Record - New Version
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/index_alert_record_new.html
    '''

    '''
    6.1 History & Active Alert Records
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
    6.2 Alert Tags
    https://support.envisioniot.com/docs/alert-api/en/2.3.0/new_version/index_alert_tag.html
    '''
    # UpdateAlertTags_py.updateAlertTags(accessKey, secretKey, orgId, url, "20220218da6bbf975612b3714ab75970306e60b8")
    # SearchAlerts_py.searchAlerts_Expression(accessKey,secretKey, orgId, url, "alertId = '20220218da6bbf975612b3714ab75970306e60b8'")

    # alertId_list = ["20220218a4c5b2ba6d1be54336ba602dd46c805f", "202202188208c33af535209da6f97b0aef839428", "20220218c6636aac668c34de07e9a4f494a3f06f"]
    # BatchUpdateAlertTags_py.batchUpdateAlertTags(accessKey, secretKey, orgId, url, alertId_list)
    # SearchAlerts_py.searchAlerts_Expression(accessKey, secretKey, orgId, url, "alertId in " + str(tuple(alertId_list)))





