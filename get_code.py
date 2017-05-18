# -*- coding:utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta



data_dir = 'G:\\Filesys\\script\\daily_renew\\j\\2_day\\'

date2 = sys.argv[1]

file_read2 = open(data_dir+os.sep+date2+'.txt', 'rb')
w_f = open(data_dir+os.sep+date2+'_code_set1.txt', 'wb')
stock_dict = dict()

while 1:
	try:
		line = file_read2.readline()
		line = line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		w_f.write(code+',')
	except:
		break

w_f.close()
file_read2.close()
