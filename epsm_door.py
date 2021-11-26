#!/usr/bin/python3

# Plugin fuer Anbindung ePowerswitch 8XM an CMK 2.x

from typing import Dict, List, Mapping, Tuple

from .agent_based_api.v1 import (
    SNMPTree,
    register,
    Service,
    Result,
    State,
    any_of,
    startswith,
    contains,
)

DETECT_FUNCTION = any_of(
    contains(".1.3.6.1.4.1.24734.", "ePowerSwitch 8XM"),
    startswith(".1.3.6.1.4.1.24734.", "ePowerSwitch 8XM"),
)

def parse_epsm_door_function(string_table):
    print(string_table)  # TEST
    data = {}
    for line in string_table:
        data[line[0]] = line[1]
    return data

#    return {
#        line[0]: line[1]
#        for line in table
#    }


def discovery_epsm_door_function(section):
    for item in section:
        yield Service(item=item)

    #yield from (Serviec(item=item) for item in section)

def check_epsm_door_function(item, section):
    if item not in section:
        return
    data = section[item]
    yield Result(
        state=State.OK, # State.OK, State.WARN, State.CRIT, State.UNKOWN
        summary="Message"
    )


register.snmp_section(
    name="epsm_door",
    detect=DETECT_FUNCTION,
    parse_function=parse_epsm_door_function,
    fetch=[
        SNMPTree(
            base=".1.3.6.1.4.1.24734.13.6.1.1",
            oids=[
                "3",
             ],
        ),
    ],
)


register.check_plugin(
    name="epsm_door",
    service_name="EPowerswitch_8XM %s",
    discovery_function=discovery_epsm_door_function,
    check_function=check_epsm_door_function,
    #cluster_check_function=my_cluster_check_function,
)



