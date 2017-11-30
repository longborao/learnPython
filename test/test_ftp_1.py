# -*- coding: utf-8 -*-
import re
from copy import deepcopy

linux_type_dict = dict()
with open('D:\\Desktop\\test.txt', 'rb') as f:
    linux_type_list = f.read().strip().split('\n')


if linux_type_list is not None:
    linux_type_list_to_purge = deepcopy(linux_type_list)
    for member in linux_type_list_to_purge:
        if re.search('^#+.*', member) is not None:
            member_to_purge = member
            linux_type_list.remove(member_to_purge)
    for member in linux_type_list:
        sub_member = member.split('=')
        linux_type_dict[sub_member[0]] = sub_member[1].strip('"')
    print linux_type_dict
    print linux_type_dict['callnewusers']
