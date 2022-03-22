import aep.applicationportal.authentication.login as login_py
import aep.applicationportal.authentication.logout as logout_py
import aep.applicationportal.authentication.getTokenInformation as getTokenInformation_py

import aep.applicationportal.usersandorganization.chooseOrganization as chooseOrganization_py

def applicationPortalGeneral(accessKey, secretKey, orgId, url):

    accessToken = login_py.login(accessKey, secretKey, url)
    chooseOrganization_py.chooseOrganization(accessKey, secretKey, orgId, url, accessToken)
    # logout_py.logout(accessKey, secretKey, url, accessToken)

    # getTokenInformation_py.getTokenInformation(accessKey, secretKey, url, accessToken)


