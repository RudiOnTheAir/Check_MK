#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2021-11-26
#
# ePowerSwitch Groups  (OBJECT IDENTIFIER ::= {eps8XM 3 })
# https://www.neol.com/en/products/epowerswitch/

#.1.3.6.1.2.1.1.1.0 = STRING: ePowerSwitch 8XM
#.1.3.6.1.2.1.1.2.0 = OID: .1.3.6.1.4.1.24734.1
#
# snmpwalk sample
# eps8XM-private::AnalogInputId.1 = STRING: "T1"
# eps8XM-private::AnalogInputId.2 = STRING: "H2"

# eps8XM-private::AnalogInputName.1 = STRING: "Temperatur DUE_VIF"
# eps8XM-private::AnalogInputName.2 = STRING: "Feuchtigkeit DUE_VIF"

# eps8XM-private::AnalogInputIntegerValue.1 = STRING: "23"
# eps8XM-private::AnalogInputIntegerValue.2 = STRING: "32"

#.1.3.6.1.4.1.24734.13.4.1.1.1.1701 = STRING: "T1"
#.1.3.6.1.4.1.24734.13.4.1.1.1.1702 = STRING: "H2"
#.1.3.6.1.4.1.24734.13.4.1.1.2.1701 = STRING: "Temperatur DUE_VIF"
#.1.3.6.1.4.1.24734.13.4.1.1.2.1702 = STRING: "Feuchtigkeit DUE_VIF"
#.1.3.6.1.4.1.24734.13.4.1.1.3.1701 = Opaque: Float: 23.220001
#.1.3.6.1.4.1.24734.13.4.1.1.3.1702 = Opaque: Float: 31.969963
#.1.3.6.1.4.1.24734.13.4.1.1.4.1701 = INTEGER: 23
#.1.3.6.1.4.1.24734.13.4.1.1.4.1702 = INTEGER: 32
#.1.3.6.1.4.1.24734.13.4.1.1.5.1701 = Hex-STRING: 20 B0 43 
#.1.3.6.1.4.1.24734.13.4.1.1.5.1702 = STRING: " %RH"

from typing import Dict

from cmk.base.plugins.agent_based.agent_based_api.v1.type_defs import (
    DiscoveryResult,
    CheckResult,
    StringTable,
)

from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    SNMPTree,
    register,
    Service,
    Result,
    State,
    startswith,
)
from dataclasses import dataclass


@dataclass
class Temp:
    name: str
    status: str


def parse_epsm_group(string_table: StringTable) -> Dict[str, Temp]:
    section = {}
    for line in string_table:
        item, name, status = line

        # if name != '- nc -':  # convert name, looks like its automatically done
        #     # "53 63 68 72 61 6E 6B 20 31 20 56 6F 72 64 65 72 74 FC 72 "
        #     name = name.strip('"').strip(' ').split(' ')
        #     # ['53','63','68','72','61','6E','6B','20','31','20','56','6F','72','64','65','72','74','FC','72']
        #     name = ''.join([f'{chr(int(x, 16))}' for x in name])
        #     # 'Schrank 1 Vordertür'

        section[item.replace('G', '')] = Temp(
            name=name,
            status=status,
        )
    return section


def discovery_epsm_group(params, section: Dict[str, Temp]) -> DiscoveryResult:
    for item in section:
        if params['add_not_conected']:
            yield Service(item=item)
        elif section[item].name not in ['-nc-', '- nc -']:
            yield Service(item=item)


def check_epsm_group(item, params, section: Dict[str, Temp]) -> CheckResult:
    try:
        di = section[item]
    except KeyError:
        return

    infotext = f'{temp.name}: {temp.status}'

    if temp.status.lower() == 'on':
        yield Result(state=State(params['state_on']), summary=infotext)
    elif temp.status.lower() == 'off':
        yield Result(state=State(params['state_off']), summary=infotext)
#    elif temp.status.lower() == 'applied':
#        yield Result(state=State(params['state_applied']), summary=infotext)
    else:
        yield Result(state=State(params['state_other']), summary=infotext)


register.snmp_section(
    name='epsm_temp',
    detect=startswith('.1.3.6.1.2.1.1.2.0', '.1.3.6.1.4.1.24734.'),
    parse_function=parse_epsm_group,
    fetch=SNMPTree(
        base='.1.3.6.1.4.1.24734.13.4.1.1',  # eps8XM-private::TempEntry
        oids=[
            '1701',  # TempId
            '1702',  # TempName
#            '3',  # TempState
        ],
    ),
)

register.check_plugin(
    name='epsm_temp',
    service_name='Temp status %s',
    discovery_function=discovery_epsm_group,
    discovery_ruleset_name='discovery_epsm_temp',
    discovery_default_parameters={
        'add_not_conected': True,
    },
    check_function=check_epsm_temp,
    check_ruleset_name='epsm_temp',
    check_default_parameters={
        'state': 1701,
#        'state_off': 1,
#        'state_applied': 0,
#        'state_other': 3,
    },
)
