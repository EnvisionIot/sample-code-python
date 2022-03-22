import IoTHub.model.getThings
import IoTHub.model.searchThingModel as SearchThingModel

def modelGeneral(accessKey, secretKey, orgId, url):

    #Get Thing Model

    IoTHub.model.getThings.getThings(accessKey, secretKey, orgId, url)

    #Search Thing Model

    SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "modelId in ( \"demo_lift_model\" )");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url,"modelId in ( \"EnOS_Solar_Site\", \"ESSHVAC\" )");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "modelId in ( \"EnOS_Solar_Site\" )");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url,"tags.amc_solar_o15952073792221_product = 'tA4ZSAFR' ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "attribute_tags.location = \"singapore\" ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "measurepoint_tags.location = \"floor\" ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "service_tags.function = \"toogle\" ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "event_tags.type = \"temp\" ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "service_tags.function = 'toogle' and event_tags.type = 'temp' ");

    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "event_tags.type like 'temp' ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "exists(event_tags.type) ");
    #SearchThingModel.searchmodel_withexpression(accessKey, secretKey, orgId, url, "not exists(event_tags.type) ");

    #SearchThingModel.searchmodel_projection(accessKey, secretKey, orgId, url);

    #SearchThingModel.searchmodel_noprojection(accessKey, secretKey, orgId, url)

    #SearchThingModel.searchmodel_name(accessKey, secretKey, orgId, url);
    #SearchThingModel.searchmodel_publicmodels(accessKey, secretKey, orgId, url);
    #SearchThingModel.searchmodel_features_pagination(accessKey, secretKey, orgId, url);
    #SearchThingModel.searchmodel_tag_pagination(accessKey, secretKey, orgId, url);
    #SearchThingModel.searchmodel_attributeTags(accessKey, secretKey, orgId, url);
    #SearchThingModel.searchmodel_serviceTags(accessKey, secretKey, orgId, url);
    #SearchThingModel.searchmodel_eventTags(accessKey, secretKey, orgId, url);
