import aep.applicationportal.authentication.login as login_py
import aep.applicationportal.usersandorganization.chooseOrganization as chooseOrganization_py
import aep.businessprocessmanagement.Process.getProcessInstance as getProcessInstance_py
import aep.businessprocessmanagement.Process.getProcessViewColumns as getProcessViewColumns_py
import aep.businessprocessmanagement.Process.queryProcessInstance as queryProcessInstance_py


def businessProcessManagementGeneral(accessKey, secretKey, orgId, url):
    accessToken = login_py.login(accessKey, secretKey, url)
    # accessToken = login_py.login_admin(accessKey, secretKey, url)
    refreshToken = chooseOrganization_py.chooseOrganization(accessKey, secretKey, orgId, url, accessToken)

    # getProcessInstance_py.getProcessInstance(accessKey, secretKey, url, accessToken)

    # getProcessViewColumns_py.getProcessViewColumns(accessKey, secretKey, url, accessToken, displayViewKey="PYTHON_VIEWKEY")

    queryProcessInstance_py.queryProcessInstance(accessKey, secretKey, url, accessToken)











