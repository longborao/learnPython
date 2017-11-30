# -*- encoding: utf-8 -*-
import datetime
import re
from copy import deepcopy

# today = datetime.date.today()
# del_days=datetime.timedelta(1)
# yesterday=today - del_days
# date_format='%Y-%m-%d'
# print yesterday.strftime(date_format)
def read_file(path):
    linux_type_dict = dict()
    with open(path, 'rb') as f:
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
        return linux_type_dict
def html_text():
    filePath='D:\\Desktop\\test.txt'
    dict=read_file(filePath)
    print dict
    for key in dict:
        if (dict[key].strip()).isdigit():
            dict[key]=format(int(dict[key]),',')
            print dict[key]
        else:
            pass
    print dict

    htmlstr = """
        <html>
    	    <head>
    	    <title 哈哈/>
    	        <style type="text/css">
    	        table.gridtable {}
                table.gridtable th {}
                table.gridtable td {}

    	        </style>

    	    </head>
            <body>

                <table width="50%" border="1" cellspacing="0" cellpadding="1">

                    <tr>
                        <th scope="col">类型</th>
                        <th scope="col">当日新增</th>
    					<th scope="col">当日总数</th>
    					<th scope="col">历史总数</th>
                    </tr>

                    <tr>
                        <th scope="col">短信表(用户数)</th>
                        <th scope="col">{}</th>
    					<th scope="col">none</th>
    					<th scope="col">{}</th>
                    </tr>

                    <tr>
                        <th scope="col">呼叫表(用户数)</th>
                        <th scope="col">{}</th>
    					<th scope="col">none</th>
    					<th scope="col">{}</th>
                    </tr>
                </table>
            </body>
        </html>
        """.format(
        "{font-family: verdana,arial,sans-serif;font-size:11px;color:#333333;border-width: 1px;border-color: #666666;border-collapse: collapse;}",
        "{border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #dedede;}",
        "{border-width: 1px;padding: 8px;border-style: solid;border-color: #666666;background-color: #ffffff;}",
        dict['smsnewusers'], dict['smstotalusers'], dict['callnewusers'], dict['calltotalusers'])
    return htmlstr
x='ee'
x.isdigit()
print html_text()