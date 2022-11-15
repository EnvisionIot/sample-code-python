import aep.notificationmanagement.sendTemplateMail as sendTemplateMail_py
import aep.notificationmanagement.sendTemplateSMS as sendTemplateSMS_py
import aep.notificationmanagement.searchSendResult as searchSendResult_py


def notificationManagementGeneral(accessKey, secretKey, orgId, url):

    # sendTemplateMail_py.sendTemplateMail(accessKey, secretKey, orgId, url)

    # sendTemplateSMS_py.sendTemplateSMS(accessKey, secretKey, orgId, url)

    '''eventId will be returned when running sendTemplateMail/sendTemplateSMS'''
    searchSendResult_py.searchSendResult(accessKey, secretKey, orgId, url, eventId="evt16481907951941900")
    searchSendResult_py.searchSendResult(accessKey, secretKey, orgId, url, eventId="evt16481917406771004")



















