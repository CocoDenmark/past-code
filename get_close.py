# -*- coding:utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta
from WindPy import w



data_dir = 'G:\\Filesys\\script\\daily_renew\\j\\2_day\\'

date2 = sys.argv[1]
today = sys.argv[2]

file_read2 = open(data_dir+os.sep+date2+'_code_set1.txt', 'rb')
w_f = open(data_dir+os.sep+today+'_close_price.txt', 'wb')

line = file_read2.readline()
line = line.strip()
code_list = line.split(',')

w.start(waitTime=60)

for code in code_list[0:2]:
	if code[0] == '6':
		c = code+'.SH'
	else:
		c = code+'.SZ'
	d = w.wsd(code, "close", today, today, "Fill=Previous", "showblank=-1")
	print d
	print d.Data
	price = d.Data[0][0]
	w_f.write(code+','+str(price)+'\r\n')
	print code

file_read2.close()
w_f.close()