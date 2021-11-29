#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2021-11-26
#
# ePowerSwitch Digital Input
# https://www.neol.com/en/products/epowerswitch/
#
# snmpwalk sample
# eps8XM-private::DigitalInputId.1 = STRING: "DI1"
# eps8XM-private::DigitalInputId.2 = STRING: "DI2"
# eps8XM-private::DigitalInputId.3 = STRING: "DI3"
# eps8XM-private::DigitalInputId.4 = STRING: "DI4"
# eps8XM-private::DigitalInputId.5 = STRING: "DI5"
# eps8XM-private::DigitalInputId.6 = STRING: "DI6"
# eps8XM-private::DigitalInputId.7 = STRING: "DI7"
# eps8XM-private::DigitalInputId.8 = STRING: "DI8"
# eps8XM-private::DigitalInputId.9 = STRING: "EM"
# eps8XM-private::DigitalInputName.1 = STRING: "53 63 68 72 61 6E 6B 20 31 20 56 6F 72 64 65 72 74 FC 72 "
# eps8XM-private::DigitalInputName.2 = STRING: "53 63 68 72 61 6E 6B 20 31 20 48 69 6E 74 65 72 74 FC 72 "
# eps8XM-private::DigitalInputName.3 = STRING: "- nc -"
# eps8XM-private::DigitalInputName.4 = STRING: "- nc -"
# eps8XM-private::DigitalInputName.5 = STRING: "- nc -"
# eps8XM-private::DigitalInputName.6 = STRING: "- nc -"
# eps8XM-private::DigitalInputName.7 = STRING: "- nc -"
# eps8XM-private::DigitalInputName.8 = STRING: "- nc -"
# eps8XM-private::DigitalInputName.9 = STRING: "- nc -"
# eps8XM-private::DigitalInputState.1 = STRING: "Closed"
# eps8XM-private::DigitalInputState.2 = STRING: "Closed"
# eps8XM-private::DigitalInputState.3 = STRING: "Open"
# eps8XM-private::DigitalInputState.4 = STRING: "Open"
# eps8XM-private::DigitalInputState.5 = STRING: "Open"
# eps8XM-private::DigitalInputState.6 = STRING: "Open"
# eps8XM-private::DigitalInputState.7 = STRING: "Open"
# eps8XM-private::DigitalInputState.8 = STRING: "Open"
# eps8XM-private::DigitalInputState.9 = STRING: "Applied"
#
# .1.3.6.1.4.1.24734.13.6.1.1.1.1 = STRING: "DI1"
# .1.3.6.1.4.1.24734.13.6.1.1.1.2 = STRING: "DI2"
# .1.3.6.1.4.1.24734.13.6.1.1.1.3 = STRING: "DI3"
# .1.3.6.1.4.1.24734.13.6.1.1.1.4 = STRING: "DI4"
# .1.3.6.1.4.1.24734.13.6.1.1.1.5 = STRING: "DI5"
# .1.3.6.1.4.1.24734.13.6.1.1.1.6 = STRING: "DI6"
# .1.3.6.1.4.1.24734.13.6.1.1.1.7 = STRING: "DI7"
# .1.3.6.1.4.1.24734.13.6.1.1.1.8 = STRING: "DI8"
# .1.3.6.1.4.1.24734.13.6.1.1.1.9 = STRING: "EM"
# .1.3.6.1.4.1.24734.13.6.1.1.2.1 = STRING: "53 63 68 72 61 6E 6B 20 31 20 56 6F 72 64 65 72 74 FC 72 "
# .1.3.6.1.4.1.24734.13.6.1.1.2.2 = STRING: "53 63 68 72 61 6E 6B 20 31 20 48 69 6E 74 65 72 74 FC 72 "
# .1.3.6.1.4.1.24734.13.6.1.1.2.3 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.2.4 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.2.5 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.2.6 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.2.7 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.2.8 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.2.9 = STRING: "- nc -"
# .1.3.6.1.4.1.24734.13.6.1.1.3.1 = STRING: "Closed"
# .1.3.6.1.4.1.24734.13.6.1.1.3.2 = STRING: "Closed"
# .1.3.6.1.4.1.24734.13.6.1.1.3.3 = STRING: "Open"
# .1.3.6.1.4.1.24734.13.6.1.1.3.4 = STRING: "Open"
# .1.3.6.1.4.1.24734.13.6.1.1.3.5 = STRING: "Open"
# .1.3.6.1.4.1.24734.13.6.1.1.3.6 = STRING: "Open"
# .1.3.6.1.4.1.24734.13.6.1.1.3.7 = STRING: "Open"
# .1.3.6.1.4.1.24734.13.6.1.1.3.8 = STRING: "Open"
# .1.3.6.1.4.1.24734.13.6.1.1.3.9 = STRING: "Applied"
#
# sample string_table
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
# sample section
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
class DigitalInput:
    name: str
    status: str


def parse_epsm_digitalinput(string_table: StringTable) -> Dict[str, DigitalInput]:
    section = {}
    for line in string_table:
        item, name, status = line

        # if name != '- nc -':  # convert name, looks like its automatically done
        #     # "53 63 68 72 61 6E 6B 20 31 20 56 6F 72 64 65 72 74 FC 72 "
        #     name = name.strip('"').strip(' ').split(' ')
        #     # ['53','63','68','72','61','6E','6B','20','31','20','56','6F','72','64','65','72','74','FC','72']
        #     name = ''.join([f'{chr(int(x, 16))}' for x in name])
        #     # 'Schrank 1 Vordertür'

        section[item.replace('DI', '')] = DigitalInput(
            name=name,
            status=status,
        )
    return section


def discovery_epsm_digitalinput(params, section: Dict[str, DigitalInput]) -> DiscoveryResult:
    for item in section:
        if params['add_not_conected']:
            yield Service(item=item)
        elif section[item].name not in ['-nc-', '- nc -']:
            yield Service(item=item)


def check_epsm_digitalinput(item, params, section: Dict[str, DigitalInput]) -> CheckResult:
    try:
        di = section[item]
    except KeyError:
        return

    infotext = f'{di.name}: {di.status}'

    if di.status.lower() == 'closed':
        yield Result(state=State(params['state_closed']), summary=infotext)
    elif di.status.lower() == 'open':
        yield Result(state=State(params['state_open']), summary=infotext)
    elif di.status.lower() == 'applied':
        yield Result(state=State(params['state_applied']), summary=infotext)
    else:
        yield Result(state=State(params['state_other']), summary=infotext)


register.snmp_section(
    name='epsm_digitalinput',
    detect=startswith('.1.3.6.1.2.1.1.2.0', '.1.3.6.1.4.1.24734.'),
    parse_function=parse_epsm_digitalinput,
    fetch=SNMPTree(
        base='.1.3.6.1.4.1.24734.13.6.1.1',  # eps8XM-private::DigitalInputEntry
        oids=[
            '1',  # DigitalInputId
            '2',  # DigitalInputName
            '3',  # DigitalInputState
        ],
    ),
)

register.check_plugin(
    name='epsm_digitalinput',
    service_name='Digital input %s',
    discovery_function=discovery_epsm_digitalinput,
    discovery_ruleset_name='discovery_epsm_digitalinput',
    discovery_default_parameters={
        'add_not_conected': True,
    },
    check_function=check_epsm_digitalinput,
    check_ruleset_name='epsm_digitalinput',
    check_default_parameters={
        'state_closed': 0,
        'state_open': 1,
        'state_applied': 0,
        'state_other': 3,
    },
)
