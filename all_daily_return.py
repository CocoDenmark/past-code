# -*- coding: utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta

get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\forward_daily\\forward_daily'
save_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\market_return'
flag = 0
f_l = os.listdir(get_data_dir)

for f in f_l:
	if f == '2007-01-04.txt':
		flag = 1
	if flag == 0:
		continue
	date = f[0:10]
	print f
	file_read = open(get_data_dir+os.sep+f, 'rb')
	return_dict = dict()
	i = 0
	while 1:
		try:
			i = 1
			line = file_read.readline()
			line.strip()
			data = line.split('|')
			code = data[0]
			if code == 'CODE':
				continue
			if data[3] == 'None' or data[6] == 'None':
				continue
			if data[2] == 'None':
				continue
			pre_close = float(data[2])
			close = float(data[6])
			maxupordown = int(data[19])
			trade_status = data[17]
			dd1 = '交易'
			if trade_status != dd1:
				#print '!!!!!!'
				tr = 0
			else:
				tr = 1
			rc = close/pre_close - 1
			return_dict[code] = [rc, maxupordown, tr]
		except:
			break

	file_read.close()


	n = 0.0
	ave = 0.0
	for code in return_dict.keys():
		if return_dict[code][2] == 0:
			continue
		ave = (ave*n+return_dict[code][0])/(n+1)
		n += 1
	open(save_data_dir+os.sep+'market_return.csv','a').write(date+','+str(ave)+','+str(n)+'\n')
