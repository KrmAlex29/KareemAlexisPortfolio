from Meraki_Test import apiKey as merakiAPIKey, organization_id as HSOID, meraki_dashboard as hsDashboard, organization_url as orgURL, organization_network_id as orgNID
import meraki
import requests

def print_network_locations():
    hsNetIDs = [
        'L_678917643826106118','L_3687885144863015376','L_678917643826102426','L_573083052582897663',
        'L_573083052582897325','N_573083052582916040','L_678917643826107691','L_573083052582897792',
        'L_678917643826106964','N_573083052582918122','L_678917643826107394','L_678917643826106264',
        'L_678917643826103448','L_678917643826105561','L_678917643826107113','L_573083052582897806',
        'L_678917643826107448','L_3687885144863015017','L_573083052582897818','L_573083052582897793',
        'L_573083052582897690','L_573083052582897805','L_678917643826107491','N_678917643826102635',
        'L_678917643826108276','L_678917643826108465','L_678917643826108466','L_573083052582897734',
        'L_573083052582897809','L_573083052582897777','L_678917643826107083','L_573083052582897222',
        'L_573083052582897737','L_573083052582897331','L_678917643826109655','N_678917643826113447',
        'L_678917643826107344','L_678917643826107603','L_678917643826107364','L_678917643826106210',
        'L_678917643826109061','L_678917643826107053','L_678917643826107298','L_678917643826107493',
        'L_573083052582897735','L_3687885144863015099','L_678917643826107407','N_3687885144863015002',
        'L_3687885144863015123','L_573083052582897491','L_678917643826106456','L_678917643826107336',
        'L_678917643826109881','L_573083052582897808','L_573083052582897489','L_678917643826106209',
        'L_678917643826109267','L_678917643826107233','N_678917643826116427','L_678917643826107139',
        'L_678917643826107335','L_573083052582897490','L_678917643826107143','L_3687885144863015375',
        'L_678917643826107501','L_573083052582897227','L_678917643826109886','L_678917643826108657'
    ]

    boerumNet_IDs = [
        'N_678917643826120778','L_678917643826109891','L_678917643826109890','L_678917643826109816',
        'N_678917643826119081','N_829788231343014975','L_829788231343014277','L_829788231343014278'
    ]

    locations = {
        "HS Location": hsNetIDs,
        "Boerum Location": boerumNet_IDs
    }

    for location_name, id_list in locations.items():
        print(f"\n{location_name}:")
        for net_id in id_list:
            print(f"  - {net_id}")

# print_network_locations()
# updatedNetworkAlerts = {

# "defaultDestinations": {
#         "emails": [
#             "bryan.marmolejos@heartshare.org",
#             "kareem.alexis@heartshare.org",
#             "kar.lau@heartshare.org",
#             "jimmy.ponce@heartshare.org",
#             "louis.appiah@heartshare.org",
#             "daizeren.ji@heartshare.org",
#             "paul.rivera@heartshare.org",
#             "Kelvin.Guevara-Dawal@heartshare.org"
#         ],
#         "allAdmins": True
#     },
#     "alerts": [
#         {
#             "type": "portDown",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": False
#             },
#             "filters": {
#                 "timeout": 10,
#                 "selector": "any port"
#             }
#         },
#         {
#             "type": "uplinkIp6Conflict",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "weeklyPresence",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "usageAlert",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {
#                 "threshold": 104857600,
#                 "period": 1200
#             }
#         },
#         {
#             "type": "onboarding",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {
#                 "selector": '{"smartSensitivity":"medium", "smartEnabled":false, "eventReminderPeriodSecs":10800, "configs":[]}'
#             }
#         },
#         {
#             "type": "gatewayDown",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {
#                 "timeout": 10
#             }
#         },
#         {
#             "type": "powerSupplyDown",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {
#                 "timeout": 10
#             }
#         },
#         {
#             "type": "switchDown",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {
#                 "timeout": 10
#             }
#         },
#         {
#             "type": "gatewayToRepeater",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {}
#         },
#         {
#             "type": "repeaterDown",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {
#                 "timeout": 10
#             }
#         },
#         {
#             "type": "rpsBackup",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {}
#         },
#         {
#             "type": "udldError",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {}
#         },
#         {
#             "type": "portError",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {
#                 "selector": "any port",
#                 "timeout": 10
#             }
#         },
#         {
#             "type": "portSpeed",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             }
#         },
#         {
#             "type": "vpnConnectivityChange",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": True,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "settingsChanged",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": True,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "clientFailedToConnectToSSID",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "allAdmins": True
#             },
#             "filters": {
#                 "ssid": "HHS-Production",
#                 "threshold": 5
#             }
#         },
#         {
#             "type": "newDhcpServer",
#             "enabled": True,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "rogueAp",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": True,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "switchCriticalTemperature",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {}
#         },
#         {
#             "type": "highWirelessUsage",
#             "enabled": False,
#             "alertDestinations": {
#                 "emails": [],
#                 "snmp": False,
#                 "allAdmins": False,
#                 "httpServerIds": []
#             },
#             "filters": {
#                 "selector": '{"configs":[]}'
#             }
#         }
#     ]
# }

# for networkID in hsNetIDs:
#     try:
#         update_admins = hsDashboard.networks.updateNetworkAlertsSettings(networkID,defaultDestinations=updatedNetworkAlerts['defaultDestinations'],
#                                                                          alerts=updatedNetworkAlerts['alerts'])
#         # update_response = hsDashboard.networks.updateNetworkAlertsSettings(networkID,defaultDestinations=updatedNetworkAlerts['defaultDestinations'],
#         #                                                                    alerts=updatedNetworkAlerts['alerts'])
#         #                                                                           + [
#         #         {
#         #             "type": "clientPoorSignalStrength",
#         #             "enabled": False,
#         #             "alertDestinations": {
#         #                 "emails": [
#         #                     'bryan.marmolejos@heartshare.org', 'kareem.alexis@heartshare.org',
#         #                     'kar.lau@heartshare.org', 'jimmy.ponce@heartshare.org',
#         #                     'louis.appiah@heartshare.org', 'daizeren.ji@heartshare.org',
#         #                     'paul.rivera@heartshare.org'
#         #                 ],
#         #                 "allAdmins": False
#         #             },
#         #             "filters": {
#         #                 'ssid': 'HHS-Production',
#         #                 'durationMinutes': 20,
#         #                 "snrThreshold": 15
#         #             }
#         #         }
#         #     ]
#         # )
#         # print(f"Alert settings updated: {networkID}")
#         print((f"Admin list updated {networkID}"))
#     except Exception as e:
#         print(f"Error updating admins for: {networkID}: {e} ")





