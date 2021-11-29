#snmp_info['epsm_door'] = (
#        # die Basis-OID
#        ".1.3.6.1.4.1.24734.10.6.4.1",
#        # die unteren Zweige
#        [ "3" ], #, "8" ],
#)
epsm_temp_dl = (35, 40)
def inventory_epsm_temp_r2(info):
    if info:
    # DEBUG
        #print "epsm_temp_aufruf"
        inv = []
        temp = info[0][0]
        inv.append(("", temp, epsm_temp_dl))
        return inv


def check_epsm_temp_r2(_no_item, params, info):
    warn, crit = params
    #print warn
    #print crit
    wert = info[0][0]
    current_stat = int(wert)
    output = "Temperature " + wert + " C"
    levels = " - warn/crit at %sC/%sC" % (warn, crit)
    perfdata = ("Temperature", current_stat, warn, crit, -10, 60)
    if crit and current_stat >= crit:
        return 2, output+levels, [perfdata]
    elif warn and current_stat >= warn:
        return 1, output+levels, [perfdata]
    else:
		return 0, output, [perfdata]
    return 3, "UNKNOWN - temperature unknown"

check_info['epsm_temp_r2'] = {
    "check_function"          : check_epsm_temp_r2,
    "inventory_function"      : inventory_epsm_temp_r2,
    "service_description"     : "temperature sensor",
    "snmp_info"               : (".1.3.6.1.4.1.24734.13.4.1.1.4", [ "1701" ]),
    #"snmp_scan_function"      : lambda oid: oid(".1.3.6.1.2.1.1.2.0").startswith(".1.3.6.1.4.1.24734."),
	"has_perfdata"            : True,
}

