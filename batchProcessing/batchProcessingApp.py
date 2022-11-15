import batchProcessing.v2_1.cancelFlowInstance_V2_1 as CancelFlowInstance_V2_1_py
import batchProcessing.v2_0.cancelFlowInstance_V2_0 as CancelFlowInstance_V2_0_py
import batchProcessing.v2_1.createDirectory_V2_1 as CreateDirectory_V2_1_py
import batchProcessing.v2_0.createDirectory_V2_0 as CreateDirectory_V2_0_py
import batchProcessing.v2_1.deleteFlow_V2_1 as DeleteFlow_V2_1_py
import batchProcessing.v2_0.deleteFlow_V2_0 as DeleteFlow_V2_0_py
import batchProcessing.v2_1.disableFlow_V2_1 as DisableFlow_V2_1_py
import batchProcessing.v2_0.disableFlow_V2_0 as DisableFlow_V2_0_py
import batchProcessing.v2_1.enableFlow_V2_1 as EnableFlow_V2_1_py
import batchProcessing.v2_0.enableFlow_V2_0 as EnableFlow_V2_0_py
import batchProcessing.v2_1.exportFlow_V2_1 as ExportFlow_V2_1_py
import batchProcessing.v2_0.exportFlow_V2_0 as ExportFlow_V2_0_py
import batchProcessing.v2_1.getCurrentTime_V2_1 as GetCurrentTime_V2_1_py
import batchProcessing.v2_0.getCurrentTime_V2_0 as GetCurrentTime_V2_0_py
import batchProcessing.v2_1.getFlow_V2_1 as GetFlow_V2_1_py
import batchProcessing.v2_0.getFlow_V2_0 as GetFlow_V2_0_py
import batchProcessing.v2_1.getFlowInstance_V2_1 as GetFlowInstance_V2_1_py
import batchProcessing.v2_0.getFlowInstance_V2_0 as GetFlowInstance_V2_0_py
import batchProcessing.v2_1.getMyFlow_V2_1 as GetMyFlow_V2_1_py
import batchProcessing.v2_0.getMyFlow_V2_0 as GetMyFlow_V2_0_py
import batchProcessing.v2_1.getTaskInstance_V2_1 as GetTaskInstance_V2_1_py
import batchProcessing.v2_1.getTaskInstanceLog_V2_1 as GetTaskInstanceLog_V2_1_py
import batchProcessing.v2_0.getTaskInstanceLog_V2_0 as GetTaskInstanceLog_V2_0_py
import batchProcessing.v2_1.getTimezone_V2_1 as GetTimezone_V2_1_py
import batchProcessing.v2_0.getTimezone_V2_0 as GetTimezone_V2_0_py
import batchProcessing.v2_1.importFlow_V2_1 as ImportFlow_V2_1_py
import batchProcessing.v2_0.importFlow_V2_0 as ImportFlow_V2_0_py
import batchProcessing.v2_1.listFlowInstances_V2_1 as ListFlowInstances_V2_1_py
import batchProcessing.v2_0.listFlowInstances_V2_0 as ListFlowInstances_V2_0_py
import batchProcessing.v2_1.listWorkflowDirectories_V2_1 as ListWorkFlowDirectories_V2_1_py
import batchProcessing.v2_0.listWorkflowDirectories_V2_0 as ListWorkFlowDirectories_V2_0_py
import batchProcessing.v2_1.loadFlowForEdit_V2_1 as LoadFlowForEdit_V2_1_py
import batchProcessing.v2_0.loadFlowForEdit_V2_0 as LoadFlowForEdit_V2_0_py
import batchProcessing.v2_1.saveFlow_V2_1 as SaveFlow_V2_1_py
import batchProcessing.v2_0.saveFlow_V2_0 as SaveFlow_V2_0_py
import batchProcessing.v2_1.searchFlow_V2_1 as SearchFlow_V2_1_py
import batchProcessing.v2_0.searchFlow_V2_0 as SearchFlow_V2_0_py
import batchProcessing.v2_1.triggerFlow_V2_1 as TriggerFlow_V2_1_py
import batchProcessing.v2_0.triggerFlow_V2_0 as TriggerFlow_V2_0_py
import batchProcessing.v2_1.triggerFlowFromTask_V2_1 as TriggerFlowFromTask_V2_1_py
import batchProcessing.v2_1.updateAndTriggerFlow_V2_1 as UpdateAndTriggerFlow_V2_1_py
import batchProcessing.v2_0.updateAndTriggerFlow_V2_0 as UpdateAndTriggerFlow_V2_0_py
import time

#userId can be found by clicking the profile icon on the top right corner of the EnOS portal under "User Id"
userId = "u16418031372711526"
current_Time = round(time.time()*1000)

def batchProcessingGeneral(accessKey, secretKey, orgId, url):
    '''Cancel Flow Instance: Version 2.1'''
    # CancelFlowInstance_V2_1_py.cancelFlowInstance_V2_1(accessKey, secretKey, orgId, url,
    #                                                    userId=userId,
    #                                                    flowInstanceId="13766-20220311060000")

    '''Cancel Flow Instance: Version 2.0'''
    # CancelFlowInstance_V2_0_py.cancelFlowInstance_V2_0(accessKey, secretKey, orgId, url,
    #                                                    userId=userId,
    #                                                    flowInstanceId="13768-20220311060000")

    '''Create Directory: Version 2.1'''
    # CreateDirectory_V2_1_py.createDirectory_V2_1(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              parentId="71f03ea6ffd844dda5ef6380fc013592",
    #                                              dirName="Python_Directory_NameV2_1")

    '''Create Directory: Version 2.0'''
    # CreateDirectory_V2_0_py.createDirectory_V2_0(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              parentId="71f03ea6ffd844dda5ef6380fc013592",
    #                                              dirName="Python_Directory_NameV2_0")

    '''Delete Flow: Version 2.1'''
    # DeleteFlow_V2_1_py.deleteFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                    userId=userId,
    #                                    flowId="13770")

    '''Delete Flow: Version 2.0'''
    # DeleteFlow_V2_0_py.deleteFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                    userId=userId,
    #                                    flowId="13768")

    '''Disable Flow: Version 2.1'''
    # DisableFlow_V2_1_py.disableFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                      userId=userId,
    #                                      flowId="13774")

    '''Disable Flow: Version 2.0'''
    # DisableFlow_V2_0_py.disableFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                      userId=userId,
    #                                      flowId="13775")

    '''Enable Flow: Version 2.1'''
    # EnableFlow_V2_1_py.enableFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                    userId=userId,
    #                                    flowId="13774")

    '''Enable Flow: Version 2.0'''
    # EnableFlow_V2_0_py.enableFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                    userId=userId,
    #                                    flowId="13775")
    
    '''Export Flow: Version 2.1'''
    # ExportFlow_V2_1_py.exportFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                    userId=userId,
    #                                    flowId="13774")

    '''Export Flow: Version 2.0'''
    # ExportFlow_V2_0_py.exportFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                    userId=userId,
    #                                    flowId="13775")

    '''Get Current Time: Version 2.1'''
    # GetCurrentTime_V2_1_py.getCurrentTime_V2_1(accessKey, secretKey, url)

    '''Get Current Time: Version 2.0'''
    # GetCurrentTime_V2_0_py.getCurrentTime_V2_0(accessKey, secretKey, url)

    '''Get Flow: Version 2.1'''
    # GetFlow_V2_1_py.getFlow_V2_1(accessKey, secretKey, orgId, url,
    #                              userId=userId,
    #                              flowId="13774")

    '''Get Flow: Version 2.0'''
    # GetFlow_V2_0_py.getFlow_V2_0(accessKey, secretKey, orgId, url,
    #                              userId=userId,
    #                              flowId="13775")

    '''Get Flow Instance: Version 2.1'''
    # GetFlowInstance_V2_1_py.getFlowInstance_V2_1(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              flowInstId="13774-20220311040000")

    '''Get Flow Instance: Version 2.0'''
    # GetFlowInstance_V2_0_py.getFlowInstance_V2_0(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              flowInstId="13775-20220311060700")

    '''Get My Flow: Version 2.1'''
    # GetMyFlow_V2_1_py.getMyFlow_V2_1(accessKey, secretKey, orgId, url, userId=userId)
    #
    # GetMyFlow_V2_1_py.getMyFlow_V2_1_expression(accessKey, secretKey, orgId, url,
    #                                             userId=userId,
    #                                             expression="13774")
    # GetMyFlow_V2_1_py.getMyFlow_V2_1_expression(accessKey, secretKey, orgId, url,
    #                                             userId=userId,
    #                                             expression="Python_FlowName2_1")

    '''Get My Flow: Version 2.0'''
    # GetMyFlow_V2_0_py.getMyFlow_V2_0(accessKey, secretKey, orgId, url, userId=userId)
    #
    # GetMyFlow_V2_0_py.getMyFlow_V2_0_searchValue(accessKey, secretKey, orgId, url,
    #                                             userId=userId,
    #                                             searchValue="13775")
    # GetMyFlow_V2_0_py.getMyFlow_V2_0_searchValue(accessKey, secretKey, orgId, url,
    #                                             userId=userId,
    #                                             searchValue="Python_FlowName2_0")

    '''Get Task Instance: Version 2.1'''
    # GetTaskInstance_V2_1_py.getTaskInstance_V2_1(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              taskInstId="613010-2022031400")

    '''Get Task Instance Log: Version 2.1'''
    # GetTaskInstanceLog_V2_1_py.getTaskInstanceLog_V2_1(accessKey, secretKey, orgId, url,
    #                                                    userId=userId,
    #                                                    taskInstId="613010-2022031400",
    #                                                    maxLength=100)

    '''Get Task Instance Log: Version 2.0'''
    # GetTaskInstanceLog_V2_0_py.getTaskInstanceLog_V2_0(accessKey, secretKey, orgId, url,
    #                                                    userId=userId,
    #                                                    taskInstId="613011-2022031400",
    #                                                    maxLength=100)

    '''Get Time Zone: Version 2.1'''
    # GetTimezone_V2_1_py.getTimezone_V2_1(accessKey, secretKey, url)

    '''Get Time Zone: Version 2.0'''
    # GetTimezone_V2_0_py.getTimezone_V2_0(accessKey, secretKey, url)

    '''Import Flow: Version 2.1'''
    # ImportFlow_V2_1_py.importFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                 userId=userId,
    #                                 flowName="Python_FlowName2_1",
    #                                 description="Flow V2_1 Description",
    #                                 dirId="97ec492e108b44f484a7790ee23764aa")

    '''Import Flow: Version 2.0'''
    # ImportFlow_V2_0_py.importFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                 userId=userId,
    #                                 flowName="Python_FlowName2_0",
    #                                 description="Flow V2_0 Description",
    #                                 dirId="ea329ff896ad4cccbf64206836e2a6c0")

    '''List Flow Instances: Version 2.1'''
    # ListFlowInstances_V2_1_py.listFlowInstances_V2_1(accessKey, secretKey, orgId, url,
    #                                                  userId=userId,
    #                                                  schedule_type="1",
    #                                                  owner="dylan.yeo",
    #                                                  fromTriggerTime="1640995200000",
    #                                                  toTriggerTime=current_Time,
    #                                                  status="-1,0,1,2,3,4,5,6,7,8,9,10",
    #                                                  )
    #
    # ListFlowInstances_V2_1_py.listFlowInstances_V2_1_expression(accessKey, secretKey, orgId, url,
    #                                                             userId=userId,
    #                                                             expression="13774-2022031400")
    # ListFlowInstances_V2_1_py.listFlowInstances_V2_1_expression(accessKey, secretKey, orgId, url,
    #                                                             userId=userId,
    #                                                             expression="Python_FlowName2_1")
    #
    # ListFlowInstances_V2_1_py.listFlowInstances_V2_1_pagination(accessKey, secretKey, orgId, url,
    #                                                             userId=userId,
    #                                                             pagination={"pageNo": 1,
    #                                                                         "pageSize": 5,
    #                                                                         "sorters": [{
    #                                                                             "field": "start_time",
    #                                                                             "order": "DESC"
    #                                                                         }]})

    '''List Flow Instances: Version 2.0'''
    # ListFlowInstances_V2_0_py.listFlowInstances_V2_0(accessKey, secretKey, orgId, url,
    #                                                  userId=userId,
    #                                                  schedule_type="1",
    #                                                  owner="dylan.yeo",
    #                                                  fromTriggerTime="1640995200000",
    #                                                  toTriggerTime=current_Time,
    #                                                  status="-1,0,1,2,3,4,5,6,7,8,9,10",
    #                                                  )
    #
    # ListFlowInstances_V2_0_py.listFlowInstances_V2_0_expression(accessKey, secretKey, orgId, url,
    #                                                             userId=userId,
    #                                                             expression="13775-2022031400")
    # ListFlowInstances_V2_0_py.listFlowInstances_V2_0_expression(accessKey, secretKey, orgId, url,
    #                                                             userId=userId,
    #                                                             expression="Python_FlowName2_0")
    #
    # ListFlowInstances_V2_0_py.listFlowInstances_V2_0_pagination(accessKey, secretKey, orgId, url,
    #                                                             userId=userId,
    #                                                             pagination={"pageNo": 0,
    #                                                                         "pageSize": 5,
    #                                                                         "sorters": [{
    #                                                                             "field": "start_time",
    #                                                                             "order": "DESC"
    #                                                                         }]})

    '''List Workflow Directories: Version 2.1'''
    # ListWorkFlowDirectories_V2_1_py.listWorkFlowDirectories_V2_1(accessKey, secretKey, orgId, url, userId=userId)

    '''List Workflow Directories: Version 2.0'''
    # ListWorkFlowDirectories_V2_0_py.listWorkFlowDirectories_V2_0(accessKey, secretKey, orgId, url, userId=userId)

    '''Load Flow for edit: Version 2.1'''
    # LoadFlowForEdit_V2_1_py.loadFlowForEdit_V2_1(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              flowId="13774")

    '''Load Flow for edit: Version 2.0'''
    # LoadFlowForEdit_V2_0_py.loadFlowForEdit_V2_0(accessKey, secretKey, orgId, url,
    #                                              userId=userId,
    #                                              flowId="13775")

    '''Save Flow: Version 2.1'''
    # SaveFlow_V2_1_py.saveFlow_V2_1(accessKey, secretKey, orgId, url, userId=userId)

    '''Save Flow: Version 2.0'''
    # SaveFlow_V2_0_py.saveFlow_V2_0(accessKey, secretKey, orgId, url, userId=userId)

    '''Search Flow: Version 2.1'''
    # SearchFlow_V2_1_py.getFlow_V2_1_expression(accessKey, secretKey, orgId, url,
    #                                            userId=userId,
    #                                            expression="13774")
    # SearchFlow_V2_1_py.getFlow_V2_1_expression(accessKey, secretKey, orgId, url,
    #                                            userId=userId,
    #                                            expression="Python_FlowName2_1")
    #
    # SearchFlow_V2_1_py.searchFlow_V2_1_pagination(accessKey, secretKey, orgId, url,
    #                                               userId=userId,
    #                                               pagination={"pageNo": 1,
    #                                                           "pageSize": 20,
    #                                                           "sorters": [{"field": "start_time",
    #                                                                        "order": "DESC"
    #                                                                        }]})

    '''Search Flow: Version 2.0'''
    # SearchFlow_V2_0_py.getFlow_V2_0_expression(accessKey, secretKey, orgId, url,
    #                                            userId=userId,
    #                                            expression="13775")
    # SearchFlow_V2_0_py.getFlow_V2_0_expression(accessKey, secretKey, orgId, url,
    #                                            userId=userId,
    #                                            expression="Python_FlowName2_0")
    #
    # SearchFlow_V2_0_py.searchFlow_V2_0_pagination(accessKey, secretKey, orgId, url,
    #                                               userId=userId,
    #                                               pagination={"pageNo": 0,
    #                                                           "pageSize": 20,
    #                                                           "sorters": [{"field": "start_time",
    #                                                                        "order": "DESC"
    #                                                                        }]})

    '''Trigger Flow: Version 2.1'''
    # TriggerFlow_V2_1_py.triggerFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                      userId=userId,
    #                                      flowId="13774",
    #                                      triggerTime=current_Time)

    '''Trigger Flow: Version 2.0'''
    # TriggerFlow_V2_0_py.triggerFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                      userId=userId,
    #                                      flowId="13775",
    #                                      triggerTime=current_Time)

    '''Trigger Flow From Task: Version 2.1'''
    # TriggerFlowFromTask_V2_1_py.triggerFlowFromTask_V2_1(accessKey, secretKey, orgId, url,
    #                                                      userId=userId,
    #                                                      flowId="13774",
    #                                                      taskId="613010",
    #                                                      triggerTime=current_Time)

    '''Parameters for Update and Trigger Flow'''
    params = ["""java -cp ide.sdk-0.1.3.jar com.envision.dataplatform.C2R.C2RBeelineUtil -i
              ${inputPath}  -o ${outputPath} -ot ${outputTableName} -ca ${columnAll} -cm
              ${columnMust} -cs ${columnSelected} -g ${group_name} -h "${HIVE_JDBC}" -u
              ${unix_timestamp} -z ${time_zone}"""]

    '''Update and Trigger Flow: Version 2.1'''
    # UpdateAndTriggerFlow_V2_1_py.updateAndTriggerFlow_V2_1(accessKey, secretKey, orgId, url,
    #                                                        userId=userId,
    #                                                        flowId="13774",
    #                                                        triggerTime=current_Time,
    #                                                        parameters=params)

    '''Update and Trigger Flow: Version 2.0'''
    # UpdateAndTriggerFlow_V2_0_py.updateAndTriggerFlow_V2_0(accessKey, secretKey, orgId, url,
    #                                                        userId=userId,
    #                                                        flowId="13775",
    #                                                        triggerTime=current_Time,
    #                                                        parameters=params)
