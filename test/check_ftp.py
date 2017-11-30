#encoding:utf-8
#!/bin/bash

import os
import datetime
table='ccp_smsgw_outsms'
month=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m')
yesterday=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
path='/data/backupdb1/'+table+'/'+table+'_'+month
# os.chdir(path)
print path