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
f_sh = open(save_data_dir+os.sep+'sh_return_open_preopen.csv', 'wb')
f_sz = open(save_data_dir+os.sep+'sz_return_open_preopen.csv', 'wb')
f_small = open(save_data_dir+os.sep+'small_return_open_preopen.csv', 'wb')
f_growth = open(save_data_dir+os.sep+'growth_return_open_preopen.csv', 'wb')
j = 0
pre_open = dict()
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
			open_p = float(data[3])
			close = float(data[6])
			maxupordown = int(data[19])
			trade_status = data[17]
			dd1 = '交易'
			if trade_status != dd1:
				#print '!!!!!!'
				tr = 0
			else:
				tr = 1
			
			try:
				pre = pre_open[code]
				pre_open[code] = open_p
			except:
				pre_open[code] = open_p
				continue
			rc = open_p/pre - 1
			#print code, rc
			return_dict[code] = [rc, maxupordown, tr]
		except:
			break

	file_read.close()


	sh_n = 0.0
        sh_ave = 0.0
        small_n = 0.0
        small_ave = 0.0
        growth_n = 0.0
        growth_ave = 0.0
        sz_n = 0.0
        sz_ave = 0.0
	for code in return_dict.keys():
		if return_dict[code][2] == 0:
			continue
		if code[0] == '6':
                        sh_ave = (sh_ave*sh_n+return_dict[code][0])/(sh_n+1)
                        sh_n += 1
                elif code[0:3] == '002':
                        small_ave = (small_ave*small_n+return_dict[code][0])/(small_n+1)
                        small_n += 1
                elif code[0:3] == '300':
                        growth_ave = (growth_ave*growth_n+return_dict[code][0])/(growth_n+1)
                        growth_n += 1
                else:
                        sz_ave = (sz_ave*sz_n+return_dict[code][0])/(sz_n+1)
                        sz_n += 1
	f_sz.write(date+','+str(sz_ave)+','+str(sz_n)+'\n')
	f_sh.write(date+','+str(sh_ave)+','+str(sh_n)+'\n')
	f_small.write(date+','+str(small_ave)+','+str(small_n)+'\n')
	f_growth.write(date+','+str(growth_ave)+','+str(growth_n)+'\n')

f_sz.close()
f_sh.close()
f_small.close()
f_growth.close()
