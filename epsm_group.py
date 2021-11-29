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
# eps8XM-private::GroupId.1 = STRING: "G1"
# eps8XM-private::GroupId.2 = STRING: "G2"
# eps8XM-private::GroupId.3 = STRING: "G3"
# eps8XM-private::GroupId.4 = STRING: "G4"
# eps8XM-private::GroupId.5 = STRING: "G5"
# eps8XM-private::GroupId.6 = STRING: "G6"


# eps8XM-private::GroupName.1 = STRING: "KVM-Switch"
# eps8XM-private::GroupName.2 = STRING: "SWITC-1"
# eps8XM-private::GroupName.3 = STRING: "SWITC-2"
# eps8XM-private::GroupName.4 = STRING: "DM-1"
# eps8XM-private::GroupName.5 = STRING: "DM-2"
# eps8XM-private::GroupName.6 = STRING: "KVM Konsole"

# eps8XM-private::GroupState.1 = STRING: "On"
# eps8XM-private::GroupState.2 = STRING: "On"
# eps8XM-private::GroupState.3 = STRING: "On"
# eps8XM-private::GroupState.4 = STRING: "On"
# eps8XM-private::GroupState.5 = STRING: "On"
# eps8XM-private::GroupState.6 = STRING: "On"

#.1.3.6.1.4.1.24734.13.3.1.1.1.1 = STRING: "G1"
#.1.3.6.1.4.1.24734.13.3.1.1.1.2 = STRING: "G2"
#.1.3.6.1.4.1.24734.13.3.1.1.1.3 = STRING: "G3"
#.1.3.6.1.4.1.24734.13.3.1.1.1.4 = STRING: "G4"
#.1.3.6.1.4.1.24734.13.3.1.1.1.5 = STRING: "G5"
#.1.3.6.1.4.1.24734.13.3.1.1.1.6 = STRING: "G6"
#.1.3.6.1.4.1.24734.13.3.1.1.2.1 = STRING: "KVM-Switch"
#.1.3.6.1.4.1.24734.13.3.1.1.2.2 = STRING: "SWITC-1"
#.1.3.6.1.4.1.24734.13.3.1.1.2.3 = STRING: "SWITC-2"
#.1.3.6.1.4.1.24734.13.3.1.1.2.4 = STRING: "DM-1"
#.1.3.6.1.4.1.24734.13.3.1.1.2.5 = STRING: "DM-2"
#.1.3.6.1.4.1.24734.13.3.1.1.2.6 = STRING: "KVM Konsole"
#.1.3.6.1.4.1.24734.13.3.1.1.3.1 = STRING: "On"
#.1.3.6.1.4.1.24734.13.3.1.1.3.2 = STRING: "On"
#.1.3.6.1.4.1.24734.13.3.1.1.3.3 = STRING: "On"
#.1.3.6.1.4.1.24734.13.3.1.1.3.4 = STRING: "On"
#.1.3.6.1.4.1.24734.13.3.1.1.3.5 = STRING: "On"
#.1.3.6.1.4.1.24734.13.3.1.1.3.6 = STRING: "On"
#.1.3.6.1.4.1.24734.13.3.1.1.4.1 = STRING: "0=On
#1=Off
#2=Restart"
#.1.3.6.1.4.1.24734.13.3.1.1.4.2 = STRING: "0=On
#1=Off
#2=Restart"
#.1.3.6.1.4.1.24734.13.3.1.1.4.3 = STRING: "0=On
#1=Off
#2=Restart"
#.1.3.6.1.4.1.24734.13.3.1.1.4.4 = STRING: "0=On
#1=Off
#2=Restart"
#.1.3.6.1.4.1.24734.13.3.1.1.4.5 = STRING: "0=On
#1=Off
#2=Restart"
#.1.3.6.1.4.1.24734.13.3.1.1.4.6 = STRING: "0=On
#1=Off
#2=Restart"
#.1.3.6.1.4.1.24734.13.3.1.1.5.1 = INTEGER: 1
#.1.3.6.1.4.1.24734.13.3.1.1.5.2 = INTEGER: 1
#.1.3.6.1.4.1.24734.13.3.1.1.5.3 = INTEGER: 1
#.1.3.6.1.4.1.24734.13.3.1.1.5.4 = INTEGER: 1
#.1.3.6.1.4.1.24734.13.3.1.1.5.5 = INTEGER: 1
#.1.3.6.1.4.1.24734.13.3.1.1.5.6 = INTEGER: 1
#
# sample string_table (NOT for this check..!!)
# [
#  ['DI1', 'Schrank 1 Vordertür', 'Closed'],
#  ['DI2', 'Schrank 1 Hintertür', 'Closed'],
#  ['DI3', '- nc -', 'Open'],
#  ['DI4', '- nc -', 'Open'],
#  ['DI5', '- nc -', 'Open'],
#  ['DI6', '- nc -', 'Open'],
#  ['DI7', '- nc -', 'Open'],
#  ['DI8', '- nc -', 'Open'],
#  ['EM', '- nc -', 'Applied']
#  ]
#
# sample section (NOT for this check..!!)
# {
#  '1': DigitalInput(name='Schrank 1 Vordertür', status='Closed'),
#  '2': DigitalInput(name='Schrank 1 Hintertür', status='Closed')
#  }
#


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
class Group:
    name: str
    status: str


def parse_epsm_group(string_table: StringTable) -> Dict[str, Group]:
    section = {}
    for line in string_table:
        item, name, status = line

        # if name != '- nc -':  # convert name, looks like its automatically done
        #     # "53 63 68 72 61 6E 6B 20 31 20 56 6F 72 64 65 72 74 FC 72 "
        #     name = name.strip('"').strip(' ').split(' ')
        #     # ['53','63','68','72','61','6E','6B','20','31','20','56','6F','72','64','65','72','74','FC','72']
        #     name = ''.join([f'{chr(int(x, 16))}' for x in name])
        #     # 'Schrank 1 Vordertür'

        section[item.replace('G', '')] = Group(
            name=name,
            status=status,
        )
    return section


def discovery_epsm_group(params, section: Dict[str, Group]) -> DiscoveryResult:
    for item in section:
        if params['add_not_conected']:
            yield Service(item=item)
        elif section[item].name not in ['-nc-', '- nc -']:
            yield Service(item=item)


def check_epsm_group(item, params, section: Dict[str, Group]) -> CheckResult:
    try:
        di = section[item]
    except KeyError:
        return

    infotext = f'{di.name}: {di.status}'

    if di.status.lower() == 'on':
        yield Result(state=State(params['state_on']), summary=infotext)
    elif di.status.lower() == 'off':
        yield Result(state=State(params['state_off']), summary=infotext)
#    elif di.status.lower() == 'applied':
#        yield Result(state=State(params['state_applied']), summary=infotext)
    else:
        yield Result(state=State(params['state_other']), summary=infotext)


register.snmp_section(
    name='epsm_group',
    detect=startswith('.1.3.6.1.2.1.1.2.0', '.1.3.6.1.4.1.24734.'),
    parse_function=parse_epsm_group,
    fetch=SNMPTree(
        base='.1.3.6.1.4.1.24734.13.3.1.1',  # eps8XM-private::GroupEntry
        oids=[
            '1',  # GroupId
            '2',  # GroupName
            '3',  # GroupState
        ],
    ),
)

register.check_plugin(
    name='epsm_group',
    service_name='Group status %s',
    discovery_function=discovery_epsm_group,
    discovery_ruleset_name='discovery_epsm_group',
    discovery_default_parameters={
        'add_not_conected': True,
    },
    check_function=check_epsm_group,
    check_ruleset_name='epsm_group',
    check_default_parameters={
        'state_on': 0,
        'state_off': 1,
#        'state_applied': 0,
#        'state_other': 3,
    },
)
