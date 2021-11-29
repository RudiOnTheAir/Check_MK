#snmp_info['epsm_door'] = (
#        # die Basis-OID
#        ".1.3.6.1.4.1.24734.10.6.4.1",
#        # die unteren Zweige
#        [ "3" ], #, "8" ],
#)
epsm_humidity_dl = (90, 95)
def inventory_epsm_humidity_r2(info):
    if info:
    #import pprint; pprint.pprint(info)
    # DEBUG
        #print "epsm_humidity_aufruf"
        inv = []
        hum = info[0][0]
        inv.append(("", hum, epsm_humidity_dl))
        return inv


def check_epsm_humidity_r2(_no_item, params, info):
    warn, crit = params
    #print warn
    #print crit
    wert = info[0][0]
    current_stat = int(wert)
    output = "Humidity " + wert + " %"
    levels = " - warn/crit at %s%%/%s%%" % (warn, crit)
    perfdata = ("Humidity", current_stat, warn, crit, 5, 100)

    if crit and current_stat >= crit:
        return 2, output+levels, [perfdata]
    elif warn and current_stat >= warn:
        return 1, output+levels, [perfdata]
    else:
        return 0, output, [perfdata]
    return 3, "UNKNOWN - humidity unknown"

check_info['epsm_humidity_r2'] = {
    "check_function"          : check_epsm_humidity_r2,
    "inventory_function"      : inventory_epsm_humidity_r2,
    "service_description"     : "humidity sensor",
    "snmp_info"               : (".1.3.6.1.4.1.24734.13.4.1.1.4", [ "1702" ]),
    #"snmp_scan_function"      : lambda oid: oid(".1.3.6.1.2.1.1.2.0").startswith(".1.3.6.1.4.1.24734."),
    "has_perfdata"            : True,
}

