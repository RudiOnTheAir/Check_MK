#snmp_info['epsm_door'] = (
#        # die Basis-OID
#        ".1.3.6.1.4.1.24734.10.6.4.1",
#        # die unteren Zweige
#        [ "3" ], #, "8" ],
#)

def inventory_epsm_door_r2(info):
    if info:
        # DEBUG
        #print "epsm_door_aufruf"
        return [ (None, None) ]


def check_epsm_door_r2(_no_item, _no_params, info):
    if info[0][0] == "Open":
        #print info[0][0]
        return 2, "door contact open"
    elif info[0][0] == "Closed":
        return 0, "door contact closed"
    else:
        return 3, "door contact status unknown"



check_info['epsm_door_r2'] = {
    "check_function"          : check_epsm_door_r2,
    "inventory_function"      : inventory_epsm_door_r2,
    "service_description"     : "door contact",
    "snmp_info"               : (".1.3.6.1.4.1.24734.13.6.1.1", [ "3" ]),
    #"snmp_scan_function"      : lambda oid: oid(".1.3.6.1.2.1.1.2.0").startswith(".1.3.6.1.4.1.24734."),
}
