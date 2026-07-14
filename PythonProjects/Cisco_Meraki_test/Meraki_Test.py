import meraki

apiKey = "9ead4d8222cb98bb215fc75009209c5a4293ac0b"

meraki_dashboard = meraki.DashboardAPI(apiKey)
response = meraki_dashboard.organizations.getOrganization(organizationId='470199')
print(response)

# heartshare organization_id
organization_id = '470199'
organization_url = 'https://api.meraki.com/api/v1/organizations/470199'

# heartshare network_id
organization_network_id = 'L_3687885144863014962'



















# get 330 Jay St. network id

# network_id_330 = None

# all_networks = meraki_dashboard.organizations.getOrganizationNetworks(organization_id)

# for network in all_networks:
#     print(f"Network Name: {network['name']}, Network ID: {network['id']}")

# 330 Jay St. network id = L_3687885144863014964


# get current alert settings for 330 J
# network_id_330 = 'L_3687885144863014964'
# alert_settings_330 = meraki_dashboard.networks.getNetworkAlertsSettings(network_id_330)
# print(alert_settings_330)
#
#
# #adding a new admin to alerts
# # new_330J_alert_admin = 'kareem.alexis@heartshare.org'
# alert_settings_330 = {
#     'defaultDestinations': {
#         'emails' : ['bryan.marmolejos@heartshare.org', 'kareem.alexis@heartshare.org', 'kar.lau@heartshare.org', 'jimmy.ponce@heartshare.org', 'louis.appiah@heartshare.org', 'marie.douyon@heartshare.org', 'daizeren.ji@heartshare.org', 'paul.rivera@heartshare.org']
#     }, 'alerts': [
#
#         {'type': 'gatewayDown'}
#     ]
#
# }
# alert_settings_330['defaultDestinations']['emails'].append('bryan.marmolejos@heartshare.org')
# alert_settings_330['defaultDestinations']['emails'].append('kareem.alexis@heartshare.org')

# alert_admin_repsonse= meraki_dashboard.networks.updateNetworkAlertsSettings(network_id_330,
#                                                                              defaultDestinations=alert_settings_330['defaultDestinations'],
#                                                                              alerts=alert_settings_330['alerts'])
# print(f"New Admin Added to Default Alert: ", alert_admin_repsonse)




# 330 Jay St name
# network_330J = '330 Jay St.'
#
# all_networks_in_org = meraki_dashboard.organizations.getOrganizationNetworks(organization_id)
#
# network_id_330 = None
#
# for network in all_networks_in_org:
#     if network['name'] == network_330J:
#         network_id_330 = network['id']
#         break
#
#     if network_id_330:
#         print(f"Network ID for {network_330J} : {netwscork_id_330} " )
#     else:
#         print(f"Network {network_330J} ID not found")



# network_330_id_response = meraki_dashboard.networks.getNetwork()
# print(network_330_id_response)



# # test_1 organization_id
# test_organization_id ='3687885144863014949'
# test_organization_url = 'https://api.meraki.com/api/v1/organizations/3687885144863014949'
#
# # get test network id
# test_1_network_id = 'L_3687885144863015328'
# test_1_network_id_response = meraki_dashboard.organizations.getOrganizationNetworks(test_organization_id, test_1_network_id)
# print(test_1_network_id_response)
#
# # call for list of admins for heartshare organization
# admin_response = meraki_dashboard.organizations.getOrganizationAdmins(organization_id)
#
# # display admins
# print(admin_response)
#
# # get organization alerts
# # health_status_response = meraki_dashboard.organizations.getOrganizationAssuranceAlerts(test_organization_id, total_pages='all')
# test_health_status_response = meraki_dashboard.organizations.getOrganizationAssuranceAlerts(test_organization_id, total_pages='1')
# print(test_health_status_response)
#
# # # adding new admin to organization
# # admin_id = ''
# # new_admin_response = meraki_dashboard.organizations.createOrganizationAdmin(test_organization_id, email='Bryan.Marmolejos@heartshare.org', name='Bryan.Marmolejos', orgAccess='full',
# #                                                                             tags=[{'tag':'east', 'access': 'full'}],
# #                                                                             network = [{'id': 'L_3687885144863015328', 'access': 'full'}],
# #                                                                             authenticationMethod= 'Email')
# # print(new_admin_response)
# # this can only be done once, will return error 'Email already taken to confirm admin user has been established
#
#
# # call for list of admins for test organization
# test_organization_admin_response = meraki_dashboard.organizations.getOrganizationAdmins(test_organization_id)
#
# # display admins
# print(test_organization_admin_response)
#
# # call for network id for organization
# # network_response = meraki_dashboard.organizations.getOrganizationNetworks(organization_id, total_pages='all')
# # print(network_response)
# #
# # # creating test organization network
# # test_network_name = 'testing office'
# # product_types = ['switch', 'wireless']
#
# # # updating network info
# # update_network_response = meraki_dashboard.networks.updateNetwork(test_1_network_id,
# #                                                                   timeZone='America/New_York')
# # print(update_network_response)
#
# # claim network device
# # t1_network_id = test_1_network_id
# serial_to_test = ['Q2GD-ELAY-KRQ8']
# # claim_device_response = meraki_dashboard.networks.claimNetworkDevices(t1_network_id, serial_to_test)
# # print(claim_device_response)
#
# # get network alerts
# # alert_network_id = test_organization_id
# # type = 'wanUtilization'
# # alert_condition = {'duration': 600, 'window':1800, 'bit_rate_bps': 5000, 'interface': 'wan1'}
# # alert_recipients= {'emails': ['IT_Test5@heartshare.org', 'Kareem.Alexis@heartshare.org', 'Bryan.Marmolejos@heartshare.org']}
# # alert_response = meraki_dashboard.organizations.createOrganizationAlertsProfile(alert_network_id, type, alert_condition, alert_recipients, networkTags=['testAlert'], description='AP Offline')
# # network_tags= ['test_tag']
# # print(admin_response)
#
# # test_network_organization_response = meraki_dashboard.organizations.createOrganizationNetwork(
# #     test_organization_id, test_network_name, product_types)
# # print(test_network_organization_response)
#
# # devices available
# test_org_dashboard = meraki.DashboardAPI(apiKey)
# test_org_device_response = meraki_dashboard.organizations.getOrganizationDevicesAvailabilities(test_organization_id, total_pages='all')
# print(test_org_device_response)
#
# # retrieve network events
# test_org_network_events = test_1_network_id
# test_network_response = meraki_dashboard.networks.getNetworkEvents(test_org_network_events, productType='wireless', total_pages='3')
# print(test_network_response)
#
# # get device clients
# client_device_response = meraki_dashboard.networks.getNetworkClients(test_1_network_id, total_pages='3', serial='Q2GD-ELAY-KRQ8')
# print(client_device_response)
#
# # get webhooks for alert types
# test_alert_types = test_organization_id
# alert_type_response = meraki_dashboard.organizations.getOrganizationWebhooksAlertTypes(test_organization_id)
# print(alert_type_response)
#
# # create alert policy
#
# test1_alert_id = test_organization_id
# type = 'appOutage'
# test1_alert_condition = {'duration': 60, 'window': 600, 'bit_rate_bps':1000, 'loss_ratio': 0.1, 'latency':100, 'jitter_ms': 100, 'mos': 3.5, 'wireless': 'ap1'}
# alert_recipients = {'emails':['kareem.alexis@heartshare.org', 'bryam.marmolejos@heartshare.org']}
# alert_tags = ['tag1']
#
# alert_response = meraki_dashboard.organizations.createOrganizationAlertsProfile(test_organization_id, type, test1_alert_condition, alert_recipients, alert_tags, description='NO Wireless Activity')
#
# # removing network device
# removeAPResponse = meraki_dashboard.networks.removeNetworkDevices(serial_to_test, test_1_network_id)
# print(removeAPResponse)
#
#

#
#
#
#
#
#
#
# # test1_organization_id= '3687885144863014949'
#
#
