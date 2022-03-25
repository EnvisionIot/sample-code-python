import aep.iam.login as login_py
import aep.iam.getSessionInformation as getSessionInformation_py
import aep.iam.getOrganization as getOrganization_py
import aep.iam.listUserOrganization as listUserOrganization_py


def notificationManagementGeneral(accessKey, secretKey, orgId, url):

    sessionId = login_py.login(accessKey, secretKey, url)




















