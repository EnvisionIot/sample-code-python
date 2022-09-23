import time
from datetime import datetime

start_time = "2022-03-01 00:00:00"
end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
currentTime = str(round(time.time() * 1000.0))


def tsdbDataGeneral(accessKey, secretKey, orgId, url):
    '''Upload Measurement Points for testing'''
    # Token = GetToken_py.GetToken(accessKey, secretKey, url)
    #
    # number = random.randrange(1, 99999)
    # UploadMeasurementPoints_py.UploadMeasurementPoints(orgId, Token, "G5M8Ojhd", "AI_Int_Power", str(number), currentTime)
    #
    # number = round(random.uniform(1.0, 99999.99), 2)
    # UploadMeasurementPoints_py.UploadMeasurementPoints(orgId, Token, "G5M8Ojhd", "AI_Double_Power", str(number), currentTime)
    #
    # number = round(random.uniform(1.0, 99999.99),2)
    # UploadMeasurementPoints_py.UploadMeasurementPoints(orgId, Token, "G5M8Ojhd", "PI_Double_Power", str(number), currentTime)
    #
    # number = random.randrange(1, 99999)
    # UploadMeasurementPoints_py.UploadMeasurementPoints(orgId, Token, "G5M8Ojhd", "DI_Int_Power", str(number), currentTime)
    #
    # number = round(random.uniform(1.0, 99999.99),2)
    # UploadMeasurementPoints_py.UploadMeasurementPoints(orgId, Token, "G5M8Ojhd", "Generic_Double_Power", str(number), currentTime)
    #
    # number = random.randrange(1, 99999)
    # UploadMeasurementPoints_py.UploadMeasurementPoints(orgId, Token, "G5M8Ojhd", "Generic_Int_Power", str(number), currentTime)
    '''
    V2.0
    https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/overview.html
    '''

    '''Filter Asset Latest Data'''
    '''Operator: eq (Equals to)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="G5M8Ojhd,Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="eq",
    #                                                          valueFilter=999)
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="eq",
    #                                                          valueFilter=999)
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Double_Power",
    #                                                          operator="eq",
    #                                                          valueFilter="999.99")

    '''Operator: nq (Not equals to)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="nq",
    #                                                          valueFilter=1)

    '''Operator: gt (Greater than)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="gt",
    #                                                          valueFilter=100)

    '''Operator: lt (Less than)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="lt",
    #                                                          valueFilter=1000)

    '''Operator: ge (Greater than or equals to)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="ge",
    #                                                          valueFilter=999)

    '''Operator: le (Less than or equals to)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="le",
    #                                                          valueFilter=999)

    '''Operator: Between (Interval of 2 values)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="between",
    #                                                          valueFilter="1,1000")

    '''Operator: In (One of the multiple values stated)'''
    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          measurepoint="Generic_Int_Power",
    #                                                          operator="in",
    #                                                          valueFilter="1,500,999")

    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0_timeWindow(accessKey, secretKey, orgId, url,
    #                                                                     timeWindow=120)

    # FilterAssetLatestData_V2_0_py.filterAssetLatestData_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset AI Data With Aggregation Logic'''
    # GetAssetAIDataWithAggregationLogic_V2_0_py.getAssetAIDataWithAggregationLogic_V2_0(accessKey, secretKey, orgId, url,
    #                                                                                    assetIds="G5M8Ojhd",
    #                                                                                    measurepointsWithLogic="count(AI_Double_Power)",
    #                                                                                    startTime=start_time,
    #                                                                                    endTime=end_time,
    #                                                                                    modelId="Python_Demo_Model")
    #
    # multiplePointIds_AI_WithLogic = "count(Int_Output),avg(AI_Int_Power),sum(AI_Double_Power),max(AI_Int_Power),min(AI_Int_Power)"
    # GetAssetAIDataWithAggregationLogic_V2_0_py.getAssetAIDataWithAggregationLogic_V2_0(accessKey, secretKey, orgId, url,
    #                                                                                    assetIds="G5M8Ojhd",
    #                                                                                    measurepointsWithLogic=multiplePointIds_AI_WithLogic,
    #                                                                                    startTime=start_time,
    #                                                                                    endTime=end_time)
    #
    # multipleAssetIds_AI_WithLogic="G5M8Ojhd,Re2qPON3"
    # GetAssetAIDataWithAggregationLogic_V2_0_py.getAssetAIDataWithAggregationLogic_V2_0(accessKey, secretKey, orgId, url,
    #                                                                                    assetIds=multipleAssetIds_AI_WithLogic,
    #                                                                                    measurepointsWithLogic="count(AI_Double_Power)",
    #                                                                                    startTime=start_time,
    #                                                                                    endTime=end_time)
    #
    # GetAssetAIDataWithAggregationLogic_V2_0_py.getAssetAIDataWithAggregationLogic_V2_0_interval(accessKey, secretKey, orgId, url,
    #                                                                                             measurepointsWithLogic="avg(Int_Output),count(AI_Int_Power)",
    #                                                                                             interval=10)
    # GetAssetAIDataWithAggregationLogic_V2_0_py.getAssetAIDataWithAggregationLogic_V2_0_interval(accessKey, secretKey,
    #                                                                                             orgId, url,
    #                                                                                             measurepointsWithLogic="Int_Output,AI_Int_Power",
    #                                                                                             interval=0)
    #
    # GetAssetAIDataWithAggregationLogic_V2_0_py.getAssetAIDataWithAggregationLogic_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset AI Raw Data'''
    # GetAssetAIRawData_V2_0_py.getAssetAIRawData_V2_0(accessKey, secretKey, orgId, url,
    #                                                  assetIds="G5M8Ojhd",
    #                                                  measurepoints="AI_Int_Power",
    #                                                  startTime=start_time,
    #                                                  endTime=end_time,
    #                                                  modelId="Python_Demo_Model")
    #
    # multiplePointIds_AI = "Int_Output,AI_Int_Power,AI_Double_Power"
    # GetAssetAIRawData_V2_0_py.getAssetAIRawData_V2_0(accessKey, secretKey, orgId, url,
    #                                                  assetIds="G5M8Ojhd",
    #                                                  measurepoints=multiplePointIds_AI,
    #                                                  startTime=start_time,
    #                                                  endTime=end_time)
    #
    # multipleAssetIds_AI = "G5M8Ojhd,Re2qPON3"
    # GetAssetAIRawData_V2_0_py.getAssetAIRawData_V2_0(accessKey, secretKey, orgId, url,
    #                                                  assetIds=multipleAssetIds_AI,
    #                                                  measurepoints="AI_Int_Power",
    #                                                  startTime=start_time,
    #                                                  endTime=end_time)
    #
    # GetAssetAIRawData_V2_0_py.getAssetAIRawData_V2_0_withQuality(accessKey, secretKey, orgId, url,
    #                                                              withQuality=True)
    #
    # GetAssetAIRawData_V2_0_py.getAssetAIRawData_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset Current Day Electric Power'''
    # GetAssetCurrentDayElectricPower_V2_0_py.getAssetCurrentDayElectricPower_V2_0(accessKey, secretKey, orgId, url,
    #                                                                              assetIds="G5M8Ojhd",
    #                                                                              measurepoints="PI_Double_Power",
    #                                                                              modelId="Python_Demo_Model")
    #
    # multiplePointIds_PI = "PI_Double_Power,outputPower,power2"
    # GetAssetCurrentDayElectricPower_V2_0_py.getAssetCurrentDayElectricPower_V2_0(accessKey, secretKey, orgId, url,
    #                                                                              assetIds="G5M8Ojhd",
    #                                                                              measurepoints=multiplePointIds_PI)
    #
    # multipleAssetIds_PI = "G5M8Ojhd,Re2qPON3"
    # GetAssetCurrentDayElectricPower_V2_0_py.getAssetCurrentDayElectricPower_V2_0(accessKey, secretKey, orgId, url,
    #                                                                              assetIds=multipleAssetIds_PI,
    #                                                                              measurepoints="PI_Double_Power")
    #
    # GetAssetCurrentDayElectricPower_V2_0_py.getAssetCurrentDayElectricPower_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset DI Data'''
    # GetAssetDIData_V2_0_py.getAssetDIData_V2_0(accessKey, secretKey, orgId, url,
    #                                            assetIds="G5M8Ojhd",
    #                                            measurepoints="DI_Int_Power",
    #                                            startTime=start_time,
    #                                            endTime=end_time,
    #                                            modelId="Python_Demo_Model")
    # 
    # multiplePointIds_DI = "DI_Int_Power,DIPower2"
    # GetAssetDIData_V2_0_py.getAssetDIData_V2_0(accessKey, secretKey, orgId, url,
    #                                            assetIds="G5M8Ojhd",
    #                                            measurepoints=multiplePointIds_DI,
    #                                            startTime=start_time,
    #                                            endTime=end_time,
    #                                            modelId="Python_Demo_Model")
    # 
    # multipleAssetIds_DI = "G5M8Ojhd,Re2qPON3"
    # GetAssetDIData_V2_0_py.getAssetDIData_V2_0(accessKey, secretKey, orgId, url,
    #                                            assetIds=multipleAssetIds_DI,
    #                                            measurepoints="DI_Int_Power",
    #                                            startTime=start_time,
    #                                            endTime=end_time,
    #                                            modelId="Python_Demo_Model")
    # 
    # GetAssetDIData_V2_0_py.getAssetDIData_V2_0_autoInterpolate(accessKey, secretKey, orgId, url,
    #                                                            autoInterpolate=True)
    # 
    # GetAssetDIData_V2_0_py.getAssetDIData_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset DI Data Duration'''
    # GetAssetDIDataDuration_V2_0_py.getAssetDIDataDuration_V2_0(accessKey, secretKey, orgId, url,
    #                                                            assetIds="G5M8Ojhd",
    #                                                            measurepoints="DI_Int_Power",
    #                                                            startTime=start_time,
    #                                                            endTime=end_time,
    #                                                            modelId="Python_Demo_Model")
    #
    # multiplePointIds_DI_Duration = "DI_Int_Power,DIPower2"
    # GetAssetDIDataDuration_V2_0_py.getAssetDIDataDuration_V2_0(accessKey, secretKey, orgId, url,
    #                                                            assetIds="G5M8Ojhd",
    #                                                            measurepoints=multiplePointIds_DI_Duration,
    #                                                            startTime=start_time,
    #                                                            endTime=end_time,
    #                                                            modelId="Python_Demo_Model")
    #
    # multipleAssetIds_DI_Duration = "G5M8Ojhd,Re2qPON3"
    # GetAssetDIDataDuration_V2_0_py.getAssetDIDataDuration_V2_0(accessKey, secretKey, orgId, url,
    #                                                            assetIds=multipleAssetIds_DI_Duration,
    #                                                            measurepoints="DI_Int_Power",
    #                                                            startTime=start_time,
    #                                                            endTime=end_time,
    #                                                            modelId="Python_Demo_Model")
    #
    # GetAssetDIDataDuration_V2_0_py.getAssetDIDataDuration_V2_0_status(accessKey, secretKey, orgId, url,
    #                                                                   status="9341")
    #
    # GetAssetDIDataDuration_V2_0_py.getAssetDIDataDuration_V2_0_Unknown(accessKey, secretKey, orgId, url,
    #                                                                   unknown= False)

    '''Get Asset Electric Power Data'''
    # GetAssetElectricPowerData_V2_0_py.getAssetElectricPowerData_V2_0(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  measurepointsWithLogic="sum(PI_Double_Power)",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multiplePointIdsWithLogic_PI = "sum(PI_Double_Power),count(outputPower),avg(power2)"
    # GetAssetElectricPowerData_V2_0_py.getAssetElectricPowerData_V2_0(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  measurepointsWithLogic=multiplePointIdsWithLogic_PI,
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multipleAssetIdsWithLogic_PI = "G5M8Ojhd,Re2qPON3"
    # GetAssetElectricPowerData_V2_0_py.getAssetElectricPowerData_V2_0(accessKey, secretKey, orgId, url,
    #                                                                  assetIds=multipleAssetIdsWithLogic_PI,
    #                                                                  measurepointsWithLogic="sum(PI_Double_Power)",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # GetAssetElectricPowerData_V2_0_py.getAssetElectricPowerData_V2_0_interval(accessKey, secretKey, orgId, url,
    #                                                                           measurepointsWithLogic="sum(PI_Double_Power),count(outputPower),avg(power2)",
    #                                                                           interval=10)
    # GetAssetElectricPowerData_V2_0_py.getAssetElectricPowerData_V2_0_interval(accessKey, secretKey, orgId, url,
    #                                                                           measurepointsWithLogic="PI_Double_Power,outputPower,power2",
    #                                                                           interval=0)
    #
    # GetAssetElectricPowerData_V2_0_py.getAssetElectricPowerData_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset Generic Data'''
    # GetAssetGenericData_V2_0_py.getAssetGenericData_V2_0(accessKey, secretKey, orgId, url,
    #                                                      assetIds="G5M8Ojhd",
    #                                                      measurepoints="Generic_Int_Power",
    #                                                      startTime=start_time,
    #                                                      endTime=end_time,
    #                                                      modelId="Python_Demo_Model")
    #
    # multiplePointIds_Generic = "Generic_Int_Power,Generic_Double_Power"
    # GetAssetGenericData_V2_0_py.getAssetGenericData_V2_0(accessKey, secretKey, orgId, url,
    #                                                      assetIds="G5M8Ojhd",
    #                                                      measurepoints=multiplePointIds_Generic,
    #                                                      startTime=start_time,
    #                                                      endTime=end_time,
    #                                                      modelId="Python_Demo_Model")
    #
    # multipleAssetIds_Generic = "G5M8Ojhd,Re2qPON3"
    # GetAssetGenericData_V2_0_py.getAssetGenericData_V2_0(accessKey, secretKey, orgId, url,
    #                                                      assetIds=multipleAssetIds_Generic,
    #                                                      measurepoints="Generic_Int_Power",
    #                                                      startTime=start_time,
    #                                                      endTime=end_time,
    #                                                      modelId="Python_Demo_Model")
    #
    # GetAssetGenericData_V2_0_py.getAssetGenericData_V2_0_withQuality(accessKey, secretKey, orgId, url,
    #                                                                  withQuality=True)
    #
    # GetAssetGenericData_V2_0_py.getAssetGenericData_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset Latest Data'''
    # GetAssetLatestData_V2_0_py.getAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                    assetIds="G5M8Ojhd",
    #                                                    measurepoints="Generic_Int_Power",
    #                                                    timeWindow=None,
    #                                                    modelId="Python_Demo_Model")
    #
    # multiplePointIds_Latest = "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power"
    # GetAssetLatestData_V2_0_py.getAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                    assetIds="G5M8Ojhd",
    #                                                    measurepoints=multiplePointIds_Latest,
    #                                                    timeWindow=None,
    #                                                    modelId="Python_Demo_Model")
    #
    # multipleAssetIds_Latest = "G5M8Ojhd,Re2qPON3"
    # GetAssetLatestData_V2_0_py.getAssetLatestData_V2_0(accessKey, secretKey, orgId, url,
    #                                                    assetIds=multipleAssetIds_Latest,
    #                                                    measurepoints="Generic_Int_Power",
    #                                                    timeWindow=None,
    #                                                    modelId="Python_Demo_Model")
    #
    # GetAssetLatestData_V2_0_py.getAssetLatestData_V2_0_withLocalTime(accessKey, secretKey, orgId, url,
    #                                                                  LocalTime=True)
    #
    # GetAssetLatestData_V2_0_py.getAssetLatestData_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''Get Asset Raw Data by Time Range'''
    # GetAssetRawDataByTimeRange_V2_0_py.getAssetRawDataByTimeRange_V2_0(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  measurepoints="Generic_Int_Power",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multiplePointIds_time = "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power"
    # GetAssetRawDataByTimeRange_V2_0_py.getAssetRawDataByTimeRange_V2_0(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  measurepoints=multiplePointIds_time,
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multipleAssetIds_time = "G5M8Ojhd,Re2qPON3"
    # GetAssetRawDataByTimeRange_V2_0_py.getAssetRawDataByTimeRange_V2_0(accessKey, secretKey, orgId, url,
    #                                                                  assetIds=multipleAssetIds_time,
    #                                                                  measurepoints="Generic_Int_Power",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # GetAssetRawDataByTimeRange_V2_0_py.getAssetRawDataByTimeRange_V2_0_order(accessKey, secretKey, orgId, url,
    #                                                                          orderBy="timestamp desc")
    #
    # GetAssetRawDataByTimeRange_V2_0_py.getAssetRawDataByTimeRange_V2_0_withQuality(accessKey, secretKey, orgId, url,
    #                                                                                withQuality=True)
    #
    # GetAssetRawDataByTimeRange_V2_0_py.getAssetRawDataByTimeRange_V2_0_accessKey(accessKey, secretKey, orgId, url)

    '''
    V2.1
    https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/overview.html
    '''

    '''Filter Asset Latest Data'''
    '''Operator: eq (Equals to)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="G5M8Ojhd,Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="eq",
    #                                                          valueFilter=999)
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="eq",
    #                                                          valueFilter=999)
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="G5M8Ojhd",
    #                                                          pointId="Generic_Double_Power",
    #                                                          operator="eq",
    #                                                          valueFilter="999.99")

    '''Operator: nq (Not equals to)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="nq",
    #                                                          valueFilter=1)

    '''Operator: gt (Greater than)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="gt",
    #                                                          valueFilter=100)

    '''Operator: lt (Less than)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="lt",
    #                                                          valueFilter=1000)

    '''Operator: ge (Greater than or equals to)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="ge",
    #                                                          valueFilter=999)

    '''Operator: le (Less than or equals to)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="le",
    #                                                          valueFilter=999)

    '''Operator: Between (Interval of 2 values)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="between",
    #                                                          valueFilter="1,1000")

    '''Operator: In (One of the multiple values stated)'''
    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                          modelId="Python_Demo_Model",
    #                                                          assetIds="Re2qPON3",
    #                                                          pointId="Generic_Int_Power",
    #                                                          operator="in",
    #                                                          valueFilter="1,500,999")

    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1_timeWindow(accessKey, secretKey, orgId, url,
    #                                                                     timeWindow=120)

    # FilterAssetLatestData_V2_1_py.filterAssetLatestData_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                     itemFormat=2)

    '''Get Asset AI Data With Aggregation Logic'''
    # GetAssetAIDataWithAggregationLogic_V2_1_py.getAssetAIDataWithAggregationLogic_V2_1(accessKey, secretKey, orgId, url,
    #                                                                                    assetIds="G5M8Ojhd",
    #                                                                                    pointsIdsWithLogic="count(AI_Double_Power)",
    #                                                                                    startTime=start_time,
    #                                                                                    endTime=end_time,
    #                                                                                    modelId="Python_Demo_Model")
    #
    # multiplePointIds_AI_WithLogic = "count(Int_Output),avg(AI_Int_Power),sum(AI_Double_Power),max(AI_Int_Power),min(AI_Int_Power)"
    # GetAssetAIDataWithAggregationLogic_V2_1_py.getAssetAIDataWithAggregationLogic_V2_1(accessKey, secretKey, orgId, url,
    #                                                                                    assetIds="G5M8Ojhd",
    #                                                                                    pointsIdsWithLogic=multiplePointIds_AI_WithLogic,
    #                                                                                    startTime=start_time,
    #                                                                                    endTime=end_time)
    #
    # multipleAssetIds_AI_WithLogic="G5M8Ojhd,Re2qPON3"
    # GetAssetAIDataWithAggregationLogic_V2_1_py.getAssetAIDataWithAggregationLogic_V2_1(accessKey, secretKey, orgId, url,
    #                                                                                    assetIds=multipleAssetIds_AI_WithLogic,
    #                                                                                    pointsIdsWithLogic="count(AI_Double_Power)",
    #                                                                                    startTime=start_time,
    #                                                                                    endTime=end_time)
    #
    # GetAssetAIDataWithAggregationLogic_V2_1_py.getAssetAIDataWithAggregationLogic_V2_1_interval(accessKey, secretKey, orgId, url,
    #                                                                                             pointIdsWithLogic="count(Int_Output),avg(AI_Int_Power)",
    #                                                                                             interval=10)
    # GetAssetAIDataWithAggregationLogic_V2_1_py.getAssetAIDataWithAggregationLogic_V2_1_interval(accessKey, secretKey,
    #                                                                                             orgId, url,
    #                                                                                             pointIdsWithLogic="Int_Output,AI_Int_Power",
    #                                                                                             interval=0)
    #
    # GetAssetAIDataWithAggregationLogic_V2_1_py.getAssetAIDataWithAggregationLogic_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                                               itemFormat=2)

    '''Get Asset AI Raw Data'''
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1(accessKey, secretKey, orgId, url,
    #                                                  assetIds="G5M8Ojhd",
    #                                                  pointIds="AI_Int_Power",
    #                                                  startTime=start_time,
    #                                                  endTime=end_time,
    #                                                  modelId="Python_Demo_Model")
    #
    # multiplePointIds_AI = "Int_Output,AI_Int_Power,AI_Double_Power"
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1(accessKey, secretKey, orgId, url,
    #                                                  assetIds="G5M8Ojhd",
    #                                                  pointIds=multiplePointIds_AI,
    #                                                  startTime=start_time,
    #                                                  endTime=end_time)
    #
    # multipleAssetIds_AI = "G5M8Ojhd,Re2qPON3"
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1(accessKey, secretKey, orgId, url,
    #                                                  assetIds=multipleAssetIds_AI,
    #                                                  pointIds="AI_Int_Power",
    #                                                  startTime=start_time,
    #                                                  endTime=end_time)
    #
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                             itemFormat=2)
    #
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1_withQuality(accessKey, secretKey, orgId, url,
    #                                                              withQuality=True)
    #
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1_boundaryType(accessKey, secretKey, orgId, url,
    #                                                               boundaryType="outside")
    # GetAssetAIRawData_V2_1_py.getAssetAIRawData_V2_1_boundaryType(accessKey, secretKey, orgId, url,
    #                                                               boundaryType="sample",
    #                                                               interval="120",
    #                                                               interpolation="linear")

    '''Get Asset Current Day Electric Power'''
    # GetAssetCurrentDayElectricPower_V2_1_py.getAssetCurrentDayElectricPower_V2_1(accessKey, secretKey, orgId, url,
    #                                                                              assetIds="G5M8Ojhd",
    #                                                                              pointIds="PI_Double_Power",
    #                                                                              modelId="Python_Demo_Model")
    #
    # multiplePointIds_PI = "PI_Double_Power,outputPower,power2"
    # GetAssetCurrentDayElectricPower_V2_1_py.getAssetCurrentDayElectricPower_V2_1(accessKey, secretKey, orgId, url,
    #                                                                              assetIds="G5M8Ojhd",
    #                                                                              pointIds=multiplePointIds_PI)
    #
    # multipleAssetIds_PI = "G5M8Ojhd,Re2qPON3"
    # GetAssetCurrentDayElectricPower_V2_1_py.getAssetCurrentDayElectricPower_V2_1(accessKey, secretKey, orgId, url,
    #                                                                              assetIds=multipleAssetIds_PI,
    #                                                                              pointIds="PI_Double_Power")
    #
    # GetAssetCurrentDayElectricPower_V2_1_py.getAssetCurrentDayElectricPower_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                                         itemFormat=2)

    '''Get Asset DI Data'''
    # GetAssetDIData_V2_1_py.getAssetDIData_V2_1(accessKey, secretKey, orgId, url,
    #                                            assetIds="G5M8Ojhd",
    #                                            pointIds="DI_Int_Power",
    #                                            startTime=start_time,
    #                                            endTime=end_time,
    #                                            modelId="Python_Demo_Model")
    #
    # multiplePointIds_DI = "DI_Int_Power,DIPower2"
    # GetAssetDIData_V2_1_py.getAssetDIData_V2_1(accessKey, secretKey, orgId, url,
    #                                            assetIds="G5M8Ojhd",
    #                                            pointIds=multiplePointIds_DI,
    #                                            startTime=start_time,
    #                                            endTime=end_time,
    #                                            modelId="Python_Demo_Model")
    #
    # multipleAssetIds_DI = "G5M8Ojhd,Re2qPON3"
    # GetAssetDIData_V2_1_py.getAssetDIData_V2_1(accessKey, secretKey, orgId, url,
    #                                            assetIds=multipleAssetIds_DI,
    #                                            pointIds="DI_Int_Power",
    #                                            startTime=start_time,
    #                                            endTime=end_time,
    #                                            modelId="Python_Demo_Model")
    #
    # GetAssetDIData_V2_1_py.getAssetDIData_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                       itemFormat=2)
    #
    # GetAssetDIData_V2_1_py.getAssetDIData_V2_1_autoInterpolate(accessKey, secretKey, orgId, url,
    #                                                            autoInterpolate=True)

    '''Get Asset DI Data Duration'''
    # GetAssetDIDataDuration_V2_1_py.getAssetDIDataDuration_V2_1(accessKey, secretKey, orgId, url,
    #                                                            assetIds="G5M8Ojhd",
    #                                                            pointIds="DI_Int_Power",
    #                                                            startTime=start_time,
    #                                                            endTime=end_time,
    #                                                            modelId="Python_Demo_Model")
    #
    # multiplePointIds_DI_Duration = "DI_Int_Power,DIPower2"
    # GetAssetDIDataDuration_V2_1_py.getAssetDIDataDuration_V2_1(accessKey, secretKey, orgId, url,
    #                                                            assetIds="G5M8Ojhd",
    #                                                            pointIds=multiplePointIds_DI_Duration,
    #                                                            startTime=start_time,
    #                                                            endTime=end_time,
    #                                                            modelId="Python_Demo_Model")
    #
    # multipleAssetIds_DI_Duration = "G5M8Ojhd,Re2qPON3"
    # GetAssetDIDataDuration_V2_1_py.getAssetDIDataDuration_V2_1(accessKey, secretKey, orgId, url,
    #                                                            assetIds=multipleAssetIds_DI_Duration,
    #                                                            pointIds="DI_Int_Power",
    #                                                            startTime=start_time,
    #                                                            endTime=end_time,
    #                                                            modelId="Python_Demo_Model")
    #
    # GetAssetDIDataDuration_V2_1_py.getAssetDIDataDuration_V2_1_Status(accessKey, secretKey, orgId, url,
    #                                                                   status="9341")
    #
    # GetAssetDIDataDuration_V2_1_py.getAssetDIDataDuration_V2_1_Unknown(accessKey, secretKey, orgId, url,
    #                                                                   unknown= False)

    '''Get Asset Electric Power Data'''
    # GetAssetElectricPowerData_V2_1_py.getAssetElectricPowerData_V2_1(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  pointIdsWithLogic="sum(PI_Double_Power)",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multiplePointIdsWithLogic_PI = "sum(PI_Double_Power),count(outputPower),avg(power2)"
    # GetAssetElectricPowerData_V2_1_py.getAssetElectricPowerData_V2_1(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  pointIdsWithLogic=multiplePointIdsWithLogic_PI,
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multipleAssetIdsWithLogic_PI = "G5M8Ojhd,Re2qPON3"
    # GetAssetElectricPowerData_V2_1_py.getAssetElectricPowerData_V2_1(accessKey, secretKey, orgId, url,
    #                                                                  assetIds=multipleAssetIdsWithLogic_PI,
    #                                                                  pointIdsWithLogic="sum(PI_Double_Power)",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # GetAssetElectricPowerData_V2_1_py.getAssetElectricPowerData_V2_1_interval(accessKey, secretKey, orgId, url,
    #                                                                           pointIdsWithLogic="sum(PI_Double_Power),count(outputPower),avg(power2)",
    #                                                                           interval=10)
    # GetAssetElectricPowerData_V2_1_py.getAssetElectricPowerData_V2_1_interval(accessKey, secretKey, orgId, url,
    #                                                                           pointIdsWithLogic="PI_Double_Power,outputPower,power2",
    #                                                                           interval=0)
    #
    # GetAssetElectricPowerData_V2_1_py.getAssetElectricPowerData_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                             itemFormat=2)

    '''Get Asset Generic Data'''
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1(accessKey, secretKey, orgId, url,
    #                                                      assetIds="G5M8Ojhd",
    #                                                      pointIds="Generic_Int_Power",
    #                                                      startTime=start_time,
    #                                                      endTime=end_time,
    #                                                      modelId="Python_Demo_Model")
    # 
    # multiplePointIds_Generic = "Generic_Int_Power,Generic_Double_Power"
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1(accessKey, secretKey, orgId, url,
    #                                                      assetIds="G5M8Ojhd",
    #                                                      pointIds=multiplePointIds_Generic,
    #                                                      startTime=start_time,
    #                                                      endTime=end_time,
    #                                                      modelId="Python_Demo_Model")
    #
    # multipleAssetIds_Generic = "G5M8Ojhd,Re2qPON3"
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1(accessKey, secretKey, orgId, url,
    #                                                      assetIds=multipleAssetIds_Generic,
    #                                                      pointIds="Generic_Int_Power",
    #                                                      startTime=start_time,
    #                                                      endTime=end_time,
    #                                                      modelId="Python_Demo_Model")
    #
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                 itemFormat=2)
    #
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1_withQuality(accessKey, secretKey, orgId, url,
    #                                                                  withQuality=True)
    #
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1_boundaryType(accessKey, secretKey, orgId, url,
    #                                                                  boundaryType="outside")
    # GetAssetGenericData_V2_1_py.getAssetGenericData_V2_1_boundaryType(accessKey, secretKey, orgId, url,
    #                                                                   boundaryType="sample",
    #                                                                   interval="120",
    #                                                                   interpolation="linear")

    '''Get Asset Latest Data'''
    # GetAssetLatestData_V2_1_py.getAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                    assetIds="G5M8Ojhd",
    #                                                    pointIds="Generic_Int_Power",
    #                                                    timeWindow=None,
    #                                                    modelId="Python_Demo_Model")
    #
    # multiplePointIds_Latest = "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power"
    # GetAssetLatestData_V2_1_py.getAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                    assetIds="G5M8Ojhd",
    #                                                    pointIds=multiplePointIds_Latest,
    #                                                    timeWindow=None,
    #                                                    modelId="Python_Demo_Model")
    #
    # multipleAssetIds_Latest = "G5M8Ojhd,Re2qPON3"
    # GetAssetLatestData_V2_1_py.getAssetLatestData_V2_1(accessKey, secretKey, orgId, url,
    #                                                    assetIds=multipleAssetIds_Latest,
    #                                                    pointIds="Generic_Int_Power",
    #                                                    timeWindow=None,
    #                                                    modelId="Python_Demo_Model")
    #
    # GetAssetLatestData_V2_1_py.getAssetLatestData_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                          itemFormat=2)
    #
    # GetAssetLatestData_V2_1_py.getAssetLatestData_V2_1_withLocalTime(accessKey, secretKey, orgId, url,
    #                                                             LocalTime=True)

    '''Get Asset Raw Data by Time Range'''
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  pointIds="Generic_Int_Power",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multiplePointIds_time = "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power"
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1(accessKey, secretKey, orgId, url,
    #                                                                  assetIds="G5M8Ojhd",
    #                                                                  pointIds=multiplePointIds_time,
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # multipleAssetIds_time = "G5M8Ojhd,Re2qPON3"
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1(accessKey, secretKey, orgId, url,
    #                                                                  assetIds=multipleAssetIds_time,
    #                                                                  pointIds="Generic_Int_Power",
    #                                                                  startTime=start_time,
    #                                                                  endTime=end_time,
    #                                                                  modelId="Python_Demo_Model")
    #
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                               itemFormat=0)
    #
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_order(accessKey, secretKey, orgId, url,
    #                                                                          orderBy="timestamp desc")
    #
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_withQuality(accessKey, secretKey, orgId, url,
    #                                                                                withQuality=True)
    #
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_type(accessKey, secretKey, orgId, url,
    #                                                                         storage_type="ai")
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_type(accessKey, secretKey, orgId, url,
    #                                                                         storage_type="ai_normalized")
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_type(accessKey, secretKey, orgId, url,
    #                                                                         storage_type="di")
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_type(accessKey, secretKey, orgId, url,
    #                                                                         storage_type="pi")
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_type(accessKey, secretKey, orgId, url,
    #                                                                         storage_type="generic")
    #
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_boundaryType(accessKey, secretKey, orgId, url,
    #                                                                                 boundaryType="outside")
    # GetAssetRawDataByTimeRange_V2_1_py.getAssetRawDataByTimeRange_V2_1_boundaryType(accessKey, secretKey, orgId, url,
    #                                                                                 boundaryType="sample",
    #                                                                                 interval="120",
    #                                                                                 interpolation="linear")

    '''Get Asset Unformatted Data''' #Incomplete
    # GetAssetUnformattedData_V2_1_py.getAssetUnformattedData(accessKey, secretKey, orgId, url,
    #                                                              assetIds="",
    #                                                              pointIds="",
    #                                                              startTime=start_time,
    #                                                              endTime=end_time)
    #
    # GetAssetUnformattedData_py.getAssetUnformattedData_orderBy(accessKey, secretKey, orgId, url,
    #                                                                      orderBy="timestamp desc")
    #
    # GetAssetUnformattedData_py.getAssetUnformattedData_itemFormat(accessKey, secretKey, orgId, url,
    #                                                                         itemFormat=2)

    '''Delete Asset Latest Data'''
    # DeleteAssetLatestData_py.deleteAssetLatestData(accessKey, secretKey, orgId, url,
    #                                                assetIds="G5M8Ojhd",
    #                                                pointIds="AI_Int_Power")

    multiplePointIds_Delete="AI_Int_Power,AI_Double_Power"
    # DeleteAssetLatestData_py.deleteAssetLatestData(accessKey, secretKey, orgId, url,
    #                                                assetIds="G5M8Ojhd",
    #                                                pointIds=multiplePointIds_Delete)
    #
    multipleAssetIds_Delete = "G5M8Ojhd,Re2qPON3"
    # DeleteAssetLatestData_py.deleteAssetLatestData(accessKey, secretKey, orgId, url,
    #                                                assetIds=multipleAssetIds_Delete,
    #                                                pointIds="AI_Int_Power")

    # DeleteAssetLatestData_py.deleteAssetLatestData(accessKey, secretKey, orgId, url,
    #                                                assetIds=multipleAssetIds_Delete,
    #                                                pointIds=multiplePointIds_Delete)

    '''Get Last Changed Data'''
    # GetLastChangedData_py.getLastChangedData(accessKey, secretKey, orgId, url,
    #                                          assetIds="G5M8Ojhd",
    #                                          pointIds="AI_Double_Power")
    #
    # multipleAssetIds_LastChange = "G5M8Ojhd,Re2qPON3"
    # GetLastChangedData_py.getLastChangedData(accessKey, secretKey, orgId, url,
    #                                          assetIds=multipleAssetIds_LastChange,
    #                                          pointIds="AI_Double_Power")
    #
    # multiplePointIds_LastChange = "AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power"
    # GetLastChangedData_py.getLastChangedData(accessKey, secretKey, orgId, url,
    #                                          assetIds="G5M8Ojhd",
    #                                          pointIds=multiplePointIds_LastChange)
    #
    # GetLastChangedData_py.getLastChangedData_withLocalTime(accessKey, secretKey, orgId, url,
    #                                                        True)
    #
    # GetLastChangedData_py.getLastChangedData_itemFormat(accessKey, secretKey, orgId, url,
    #                                                     itemFormat=2)

    '''Check Dead Data'''
    # CheckDeadData_py.checkDeadData(accessKey, secretKey, orgId, url,
    #                                assetId="G5M8Ojhd",
    #                                pointId="AI_Double_Power")

    '''Submit Data Deletion Job'''
    # jobId = SubmitDataDeletionJob_py.submitDataDeletionJob(accessKey, secretKey, orgId, url,
    #                                                        modelId="Python_Demo_Model",
    #                                                        pointId="AI_Int_Power",
    #                                                        assetIds="G5M8Ojhd",
    #                                                        startTime="1643760000000",
    #                                                        endTime="1646006400000")
    # jobId = SubmitDataDeletionJob_py.submitDataDeletionJob(accessKey, secretKey, orgId, url,
    #                                                        modelId="Python_Demo_Model",
    #                                                        pointId=None,
    #                                                        assetIds="G5M8Ojhd",
    #                                                        startTime="1643760000000",
    #                                                        endTime="1646006400000")

    # '''Get Data Deletion Details'''
    # GetDataDeletionDetails_py.getDataDeletionDetails(accessKey, secretKey, orgId, url,
    #                                                  queryId=jobId)
    # GetDataDeletionDetails_py.getDataDeletionDetails(accessKey, secretKey, orgId, url,
    #                                                  queryId="419807391670087680")

    '''Resubmit Data Deletion Job'''
    # ResubmitDataDeletionJob_py.resubmitDataDeletionJob(accessKey, secretKey, orgId, url,
    #                                                    jobId=jobId)
    # ResubmitDataDeletionJob_py.resubmitDataDeletionJob(accessKey, secretKey, orgId, url,
    #                                                    jobId="419807391670087680")


