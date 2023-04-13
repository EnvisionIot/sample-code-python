import aep.applicationportal.authentication.login as login_py
import aep.applicationportal.usersandorganization.chooseOrganization as chooseOrganization_py
import aep.businessprocessmanagement.process.getProcessInstance as getProcessInstance_py
import aep.businessprocessmanagement.process.getProcessViewColumns as getProcessViewColumns_py
import aep.businessprocessmanagement.process.queryProcessInstance as queryProcessInstance_py
import aep.businessprocessmanagement.process.queryProcessInstanceByView as queryProcessInstanceByView_py
import aep.businessprocessmanagement.process.startProcessInstance as startProcessInstance_py
import aep.businessprocessmanagement.process.terminateProcessInstance as terminateProcessInstance_py
import aep.businessprocessmanagement.task.getTask as getTask_py
import aep.businessprocessmanagement.task.queryTask as queryTask_py
import aep.businessprocessmanagement.task.claimTask as claimTask_py
import aep.businessprocessmanagement.task.completeTask as completeTask_py
import aep.businessprocessmanagement.task.claimAndCompleteTask as claimAndCompleteTask_py


def businessProcessManagementGeneral(accessKey, secretKey, orgId, url):
    accessToken = login_py.login(accessKey, secretKey, url)
    # accessToken = login_py.login_admin(accessKey, secretKey, url)
    # refreshToken = chooseOrganization_py.chooseOrganization(accessKey, secretKey, orgId, url, accessToken)

    '''
    1. Process
    https://support.envisioniot.com/docs/bpm-api/en/2.3.0/process/index_process.html
    '''
    # getProcessInstance_py.getProcessInstance(accessKey, secretKey, url, accessToken, processInstanceId="54366b8f-ab3d-11ec-8df5-120e04f331d8")

    # getProcessViewColumns_py.getProcessViewColumns(accessKey, secretKey, url, accessToken, displayViewKey="PYTHON_VIEWKEY")

    # queryProcessInstance_py.queryProcessInstance(accessKey, secretKey, url, accessToken)

    # queryProcessInstanceByView_py.queryProcessInstanceByView(accessKey, secretKey, url, accessToken, displayViewKey="API230JAVAPWF_KEY", id="adf38f2eea9a211ecad0f8e1ac2659f4c")

    # startProcessInstance_py.startProcessInstance(accessKey, secretKey, url, accessToken)

    # terminateProcessInstance_py.terminateProcessInstance(accessKey, secretKey, url, accessToken, processInstanceId="473e66a9-aa75-11ec-ad0f-8e1ac2659f4c")

    '''
    2. Task
    https://support.envisioniot.com/docs/bpm-api/en/2.3.0/task/index_task.html
    '''
    # getTask_py.getTask(accessKey, secretKey, url, accessToken, taskId="543ab164-ab3d-11ec-8df5-120e04f331d8")

    # queryTask_py.queryTask(accessKey ,secretKey, url, accessToken)

    # claimTask_py.claimTask(accessKey, secretKey, url, accessToken, taskId="543ab164-ab3d-11ec-8df5-120e04f331d8")

    # completeTask_py.completeTask(accessKey, secretKey, url, accessToken, taskId="0f0af846-ab3b-11ec-8df5-120e04f331d8")

    # claimAndCompleteTask_py.claimAndCompleteTask(accessKey, secretKey, url, accessToken, taskId="cc3a2f2f-ab3e-11ec-ad0f-8e1ac2659f4c")

















