import aep.iam.login as login_py
import aep.iam.getSessionInformation as getSessionInformation_py
import aep.iam.getOrganization as getOrganization_py
import aep.iam.listUserOrganization as listUserOrganization_py


def iamGeneral(accessKey, secretKey, orgId, url):

    sessionId = login_py.login(accessKey, secretKey, url)

    getSessionInformation_py.getSessionInformation(accessKey, secretKey, url, sessionId)

    getOrganization_py.getOrganization(accessKey, secretKey, orgId, url, sessionId)

    listUserOrganization_py.listUserOrganization(accessKey, secretKey, url, sessionId)




















