import streamprocessing.getStageState as GetStageState_py
import streamprocessing.deleteStageState as DeleteStageState_py
import streamprocessing.listPipelines as ListPipelines_py
import streamprocessing.getPipelineDetails as GetPipelineDetails_py
import streamprocessing.getPipelineOffsetAndLag as GetPipelineOffsetAndLag
import streamprocessing.resetPipelineOffset as ResetPipelineOffset
import streamprocessing.operatepipeline.startPipeline as StartPipeline_py
import streamprocessing.operatepipeline.pausePipeline as PausePipeline_py
import streamprocessing.operatepipeline.stopPipeline as StopPipeline_py
import streamprocessing.operatepipeline.savePipeline as SavePipeline_py
import streamprocessing.operatepipeline.releasePipeline as ReleasePipeline_py

pipeline_Id= "1010eac9-7770-4769-8011-2b02d761d5e0"

def streamProcessingGeneral(accessKey, secretKey, orgId, url):
    # GetPipelineDetails_py.getPipelineDetails(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # ListPipelines_py.listPipeline(accessKey, secretKey, orgId, url)
    # ListPipelines_py.listPipeline_optionalParameters(accessKey, secretKey, orgId, url)

    # GetStageState_py.getStageState(accessKey, secretKey, orgId, url,
    #                                pipelineId= "ade78e6a-0df6-4312-9afd-574959278286",
    #                                stageInstanceName= "LatePointTagger_01",
    #                                assetIds= "ChahG3d9",
    #                                pointIds= "temp")

    # DeleteStageState_py.deleteStageState(accessKey, secretKey, orgId, url,
    #                                pipelineId="1010eac9-7770-4769-8011-2b02d761d5e0",
    #                                stageInstanceName=  "LatePointTagger_01",
    #                                assetIds="ChahG3d9",
    #                                pointIds="temp")

    # GetPipelineOffsetAndLag.getPipelineOffsetAndLag(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # ResetPipelineOffset.resetPipelineOffset(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)


    '''
    Operating Pipeline
    https://support.envisioniot.com/docs/stream-processing-api/en/2.3.0/operate_pipeline.html
    '''
    # StartPipeline_py.startPipeline(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # PausePipeline_py.pausePipeline(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # StopPipeline_py.stopPipeline(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # SavePipeline_py.savePipeline(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # ReleasePipeline_py.releasePipeline(accessKey, secretKey, orgId, url, pipelineId= pipeline_Id)

    # SavePipeline_py.createPipeline(accessKey, secretKey, orgId, url)









