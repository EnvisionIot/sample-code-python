import dataFederation.listChannels as ListChannels_py
import dataFederation.readData as ReadData_py
import dataFederation.listJobs as ListJobs_py
import dataFederation.getJobDetails as GetJobDetails_py
import dataFederation.writeMessage as WriteMessage_py
import dataFederation.writeChunkFile as WriteChunkFile_py
import dataFederation.operateChannel as OperateChannel_py
import dataFederation.createDownloadRequest as CreateDownloadRequest_py
import dataFederation.getDownloadStatus as GetDownloadStatus_py
import dataFederation.cancelDownload as CancelDownload_py
import base64


def dataFederationGeneral(accessKey, secretKey, orgId, url):
    '''List Channels'''
    # ListChannels_py.listChannels(accessKey, secretKey, orgId, url)
    # ListChannels_py.listChannels(accessKey, secretKey, orgId, url, channelType="READ")
    # ListChannels_py.listChannels(accessKey, secretKey, orgId, url, channelType="WRITE")
    # ListChannels_py.listChannels(accessKey, secretKey, orgId, url, channelType="DOWNLOAD")

    '''Read Data'''
    # ReadData_py.readData(accessKey, secretKey, orgId, url,
    #                      channelId="ch-28b1b7",
    #                      sqlQuery="show schemas",
    #                      source="demo",
    #                      queue=None,
    #                      itemFormat=None)
    # ReadData_py.readData(accessKey, secretKey, orgId, url,
    #                      channelId="ch-28b1b7",
    #                      sqlQuery="SELECT orgid, value FROM db_demomanager.smart_battery_data where measurepoints = 'temp_before'",
    #                      source="demo",
    #                      queue=None,
    #                      itemFormat=None)
    #
    # ReadData_py.readData_source(accessKey, secretKey, orgId, url,
    #                             channelId="ch-28b1b7",
    #                             sqlQuery="SELECT orgid, value FROM db_demomanager.smart_battery_data where measurepoints = 'temp_before'",
    #                             source="demo")
    #
    # ReadData_py.readData_queue(accessKey, secretKey, orgId, url,
    #                            channelId="ch-28b1b7",
    #                            sqlQuery="SELECT orgid, value FROM db_demomanager.smart_battery_data where measurepoints = 'temp_before'",
    #                            queue="Hot")
    #
    # ReadData_py.readData_itemFormat(accessKey, secretKey, orgId, url,
    #                                 channelId="ch-28b1b7",
    #                                 sqlQuery="SELECT orgid, value FROM db_demomanager.smart_battery_data where measurepoints = 'temp_before'",
    #                                 itemFormat=1)

    '''List Jobs'''
    # ListJobs_py.listJobs(accessKey, secretKey, orgId, url, channelId="ch-28b1b7")
    # ListJobs_py.listJobs(accessKey, secretKey, orgId, url, channelId="ch-e98adc")
    # ListJobs_py.listJobs(accessKey, secretKey, orgId, url, channelId="ch-6b98e9")

    '''Get Job Details'''
    # GetJobDetails_py.getJobDetails(accessKey, secretKey, orgId, url, channelId="ch-28b1b7", jobId="1de0ddb2-fb3a-24a2-7779-f3236f5d67a1")

    '''Operate Channel'''
    # OperateChannel_py.operateChannels(accessKey, secretKey, orgId, url, channelId="ch-28b1b7", action="start")
    # OperateChannel_py.operateChannels(accessKey, secretKey, orgId, url, channelId="ch-28b1b7", action="stop")

    # OperateChannel_py.operateChannels_resource(accessKey, secretKey, orgId, url,
    #                                            channelId="ch-28b1b7",
    #                                            action="start",
    #                                            resourceId="federation_6ahw26",
    #                                            resourceConfig="2",
    #                                            ifMultiResourceAnalysis=False)

    '''Write Message'''
    # data = str({'table': 'employees',
    #             'lines': [{'emp_no': '90909',
    #                        'birth_date': '2000-01-01 00:00:00',
    #                        'first_name': 'Mitsuko',
    #                        'last_name': 'Yuzuki',
    #                        'gender': 'F',
    #                        'hire_date': '2022-01-01 00:00:00'}]
    #             })
    # WriteMessage_py.writeMessage(accessKey, secretKey, orgId, url,
    #                              channelId="ch-16637e",
    #                              dataSourceName="employees",
    #                              data=data,
    #                              sync=True)

    '''Write Chunk File'''
    # contents = 'Test Message'
    # size = len(contents.encode('utf-8'))
    # chunkFileData = (base64.b64encode(bytes(contents, 'utf-8'))).decode()
    #
    # WriteChunkFile_py.writeChunkFile(accessKey, secretKey, orgId, url,
    #                                  channelId="ch-16637e",
    #                                  dataSourceName="HDFS(EnOS)",
    #                                  fileName="File_Test",
    #                                  totalSize=size,
    #                                  chunkOffset=0,
    #                                  chunkSize=size,
    #                                  chunkData=chunkFileData)

    '''Create Download Request'''
    # taskId = CreateDownloadRequest_py.createDownloadRequest(accessKey, secretKey, orgId, url,
    #                                                channelId="ch-e98adc",
    #                                                taskName="CreateDownloadReqest_GetEmployee",
    #                                                sourceName="hive_enos",
    #                                                querySql="SELECT * FROM db_demomanager.employee",
    #                                                filePackageName="FilePackageName_Employee")

    # CreateDownloadRequest_py.createDownloadRequest(accessKey, secretKey, orgId, url,
    #                                                channelId="ch-e98adc",
    #                                                taskName="CreateDownloadReqest_GetEmployee_FileConfig",
    #                                                sourceName="hive_enos",
    #                                                querySql="SELECT * FROM db_demomanager.employee",
    #                                                filePackageName="FilePackageName_Employee_FileConfig",
    #                                                files={"split": True,
    #                                                       "encoding": "utf-8",
    #                                                       "delimiter": ",",
    #                                                       "fileHeader": ["c1", "c2", "c3"],
    #                                                       "fileRename": {"1": "group1",
    #                                                                      "2": "group2",
    #                                                                      "3": "group3"}
    #                                                       })
    #
    # CreateDownloadRequest_py.createDownloadRequest(accessKey, secretKey, orgId, url,
    #                                                channelId="ch-e98adc",
    #                                                taskName="CreateDownloadReqest_GetEmployee_callback",
    #                                                sourceName="hive_enos",
    #                                                querySql="SELECT * FROM db_demomanager.employee",
    #                                                filePackageName="FilePackageName_Employee_callbackURL",
    #                                                callbackURL="http://localhost:8080")
    #
    # CreateDownloadRequest_py.createDownloadRequest(accessKey, secretKey, orgId, url,
    #                                                channelId="ch-e98adc",
    #                                                taskName="CreateDownloadReqest_GetEmployee_SelfParams",
    #                                                sourceName="hive_enos",
    #                                                querySql="SELECT * FROM db_demomanager.employee",
    #                                                filePackageName="FilePackage_Employee_SelfParams",
    #                                                selfDefineQueuePara="set mapreduce.map.memory.mb=1024;set mapreduce.reduce.memory.mb=2048")


    '''Get Download Status'''
    # GetDownloadStatus_py.getDownloadStatus(accessKey, secretKey, orgId, url,
    #                                        channelId="ch-e98adc",
    #                                        taskId="2603e4901038472a8dcd7faf4d1ec336")
    # GetDownloadStatus_py.getDownloadStatus(accessKey, secretKey, orgId, url,
    #                                        channelId="ch-e98adc",
    #                                        taskId=taskId)

    '''Cancel Download'''
    # CancelDownload_py.cancelDownload(accessKey, secretKey, orgId, url,
    #                                        channelId="ch-e98adc",
    #                                        taskId="2546e27eabc6449b91f1fc3989eba9a0")









