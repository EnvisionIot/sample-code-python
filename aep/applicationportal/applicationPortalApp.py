import aep.applicationportal.authentication.login as login_py
import aep.applicationportal.authentication.logout as logout_py
import aep.applicationportal.authentication.getTokenInformation as getTokenInformation_py
import aep.applicationportal.authentication.refreshAccessToken as refreshAccessToken_py
import aep.applicationportal.authentication.revokeRefreshToken as revokeRefreshToken_py
import aep.applicationportal.usersandorganization.chooseOrganization as chooseOrganization_py
import aep.applicationportal.usersandorganization.createAndJoinUser as createAndJoinUser_py
import aep.applicationportal.usersandorganization.joinUsers as joinUsers_py
import aep.applicationportal.usersandorganization.getManageableUserList as getManageableUserList_py
import aep.applicationportal.usersandorganization.getOrganizationList as getOrganizationList_py
import aep.applicationportal.usersandorganization.getOrganizationLanguageList as getOrganizationLanguageList_py
import aep.applicationportal.usersandorganization.getOrganizationUserList as getOrganizationUserList_py
import aep.applicationportal.usersandorganization.getOrganizationRoles as getOrganizationRoles_py
import aep.applicationportal.usersandorganization.getAppUserList as getAppUserList_py
import aep.applicationportal.usersandorganization.getUserInformation as getUserInformation_py
import aep.applicationportal.usersandorganization.getUserDomain as getUserDomain_py
import aep.applicationportal.usersandorganization.getUserStructures as getUserStructures_py
import aep.applicationportal.usersandorganization.getUserRoles as getUserRoles_py
import aep.applicationportal.usersandorganization.getUserPermissions as getUserPermissions_py
import aep.applicationportal.usersandorganization.getUserBaseInfo as getUserBaseInfo_py
import aep.applicationportal.usersandorganization.getUsersAssetList as getUsersAssetList_py
import aep.applicationportal.usersandorganization.getUsersRoleList as getUsersRoleList_py
import aep.applicationportal.usersandorganization.getUsersStructureList as getUsersStructureList_py
import aep.applicationportal.usersandorganization.getUsersUserGroupList as getUsersUserGroupList_py
import aep.applicationportal.usersandorganization.assignOrganizationStructures as assignOrganizationStructures_py
import aep.applicationportal.usersandorganization.assignUserRoles as assignUserRoles_py
import aep.applicationportal.usersandorganization.assignUserGroups as assignUserGroups_py
import aep.applicationportal.usersandorganization.removeOrganizationStructures as removeOrganizationStructures_py
import aep.applicationportal.usersandorganization.removeUserRoles as removeUserRoles_py
import aep.applicationportal.usersandorganization.removeUserGroups as removeUserGroups_py
import aep.applicationportal.usersandorganization.removeUser as removerUser_py
import aep.applicationportal.asset.authorizeAsset as authorizeAsset_py
import aep.applicationportal.asset.checkAssetPermission as checkAssetPermission_py
import aep.applicationportal.asset.getAssetsByApplication as getAssetsByApplication_py
import aep.applicationportal.asset.getAssetsByOrganization as getAssetsByOrganization_py
import aep.applicationportal.asset.getAssetStructure as getAssetStructure_py
import aep.applicationportal.asset.getStructureAsset as getStructureAsset_py
import aep.applicationportal.asset.syncAsset as syncAsset_py
import aep.applicationportal.asset.getUsersWithAssetAccess as getUsersWithAssetAccess_py
import aep.applicationportal.application.createMessage as createMessage_py
import aep.applicationportal.application.getAppMenuAndPermission as getAppMenuAndPermission_py
import aep.applicationportal.application.getColorsOfTheMessageIcon as getColorsOfTheMessageIcon_py
import aep.applicationportal.application.getMessageRingtones as getMessageRingtones_py
import aep.applicationportal.application.getUserApplications as getUserApplications_py
import aep.applicationportal.application.updateMessages as updateMessages_py
import aep.applicationportal.application.getUnresolvedMessages as getUnresolvedMessages_py

def applicationPortalGeneral(accessKey, secretKey, orgId, url):

    '''
    1. Authentication
    https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/authentication/index_authentication.html
    '''
    # accessToken = login_py.login(accessKey, secretKey, url)

    # refreshToken = chooseOrganization_py.chooseOrganization(accessKey, secretKey, orgId, url, accessToken)

    # getTokenInformation_py.getTokenInformation(accessKey, secretKey, url, accessToken)

    # newAccessToken = refreshAccessToken_py.refreshAccessToken(accessKey, secretKey, url, refreshToken)

    # revokeRefreshToken_py.revokeRefreshToken(accessKey, secretKey, url, accessToken, refreshToken)

    # logout_py.logout(accessKey, secretKey, url, newAccessToken)

    '''
    2. Users and Organisation
    https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/index_user_ou.html
    '''
    # createAndJoinUser_py.createAndJoinUser(accessKey, secretKey, orgId, url)

    # joinUsers_py.joinUsers(accessKey, secretKey, orgId, url)

    # getManageableUserList_py.getManageableUserList(accessKey, secretKey, url, accessToken)

    # getOrganizationList_py.getOrganizationList(accessKey, secretKey, url, accessToken)

    # getOrganizationLanguageList_py.getOrganizationLanguageList(accessKey, secretKey, orgId, url)

    # getOrganizationUserList_py.getOrganizationUserList(accessKey, secretKey, orgId, url)

    # getOrganizationRoles_py.getOrganizationRoles(accessKey, secretKey, orgId, url)

    # getAppUserList_py.getAppUserList(accessKey, secretKey, url, accessToken)

    # getUserInformation_py.getUserInformation(accessKey, secretKey, url, accessToken)

    # getUserDomain_py.getUserDomain(accessKey, secretKey, url)

    # getUserStructures_py.getUserStructures(accessKey, secretKey, url, accessToken)

    # getUserRoles_py.getUserRoles(accessKey, secretKey, orgId, url)

    # getUserPermissions_py.getUserPermissions(accessKey, secretKey, orgId, url)

    # getUserBaseInfo_py.getUserBaseInfo(accessKey, secretKey, orgId, url, email="ming.wang4@envision-digital.com")
    # getUserBaseInfo_py.getUserBaseInfo(accessKey, secretKey, orgId, url, domain="enosBFCustomer2")
    # getUserBaseInfo_py.getUserBaseInfo(accessKey, secretKey, orgId, url, phoneArea="86")
    # getUserBaseInfo_py.getUserBaseInfo(accessKey, secretKey, orgId, url, phone="1231234")
    # getUserBaseInfo_py.getUserBaseInfo(accessKey, secretKey, orgId, url, name="songxibin2013")

    # getUsersAssetList_py.getUsersAssetList(accessKey, secretKey, orgId, url)

    # getUsersRoleList_py.getUsersRoleList(accessKey, secretKey, orgId, url)

    # getUsersStructureList_py.getUsersStructureList(accessKey, secretKey, orgId, url)

    # getUsersUserGroupList_py.getUsersUserGroupList(accessKey, secretKey, orgId, url)

    # assignOrganizationStructures_py.assignOrganizationStructures(accessKey, secretKey, orgId, url)

    # assignUserRoles_py.assignUserRoles(accessKey, secretKey, orgId, url)

    # assignUserGroups_py.assignUserGroups(accessKey, secretKey, orgId, url)

    # removeOrganizationStructures_py.removeOrganizationStructures(accessKey, secretKey, orgId, url)

    # removeUserRoles_py.removeUserRoles(accessKey, secretKey, orgId, url)

    # removeUserGroups_py.removeUserGroups(accessKey, secretKey, orgId, url)

    # removerUser_py.removeUser(accessKey, secretKey, orgId, url)

    '''
    3. Asset (Requires assets to be synchronize)
    https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/index_asset.html
    '''
    # authorizeAsset_py.authorizeAsset(accessKey, secretKey, orgId, url)

    # checkAssetPermission_py.checkAssetPermission(accessKey, secretKey, url, accessToken)

    # getAssetsByApplication_py.getAssetsByApplication(accessKey, secretKey, url, accessToken)

    # getAssetsByOrganization_py.getAssetsByOrganization(accessKey, secretKey, orgId, url)

    # getAssetStructure_py.getAssetStructure(accessKey, secretKey, url, accessToken)

    # getStructureAsset_py.getStructureAsset(accessKey, secretKey, url, accessToken)

    # syncAsset_py.syncAsset(accessKey, secretKey, orgId, url)

    # getUsersWithAssetAccess_py.getUsersWithAssetAccess(accessKey, secretKey, orgId, url)

    '''
    4. Application
    https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/index_app.html
    '''
    # createMessage_py.createMessage(accessKey, secretKey, orgId, url)

    # getAppMenuAndPermission_py.getAppMenuAndPermission(accessKey, secretKey, url, accessToken)

    # getColorsOfTheMessageIcon_py.getColorsOfTheMessageIcon(accessKey, secretKey, url)

    # getMessageRingtones_py.getMessageRingtones(accessKey, secretKey, url)

    # getUserApplications_py.getUserApplications(accessKey, secretKey, url, accessToken)

    # updateMessages_py.updateMessages(accessKey, secretKey, url)

    # getUnresolvedMessages_py.getUnresolvedMessages(accessKey, secretKey, orgId, url)












