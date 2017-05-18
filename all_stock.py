# -*- coding: utf-8 -*-
import datetime
import os
import sys


get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily_f'
f_l = os.listdir(get_data_dir)
days = [1,2,3,4,5,6,7,8,9,10]

for day in days[0:1]:	
	save_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\return\\'+str(day)+'_day'
	try:
		os.mkdir(save_data_dir)
	except:
		pass
	for f_n in f_l[:-1]:
		d = dict()
		flag = 0
		f = open(get_data_dir+os.sep+f_n, 'rb')
		f.readline()

		while 1:
			try:
				line = f.readline().strip()
				data = line.split('|')
				if len(data) == 1:
					break
				if data[1] == 'nan' and data[2] == 'nan':
					flag = 1
					break
				if data[1] == 'None' or data[5] == 'None':
					continue
				date = data[0][0:10]
				#print date
				date = datetime.date(int(date[0:4]),int(date[5:7]),int(date[8:10]))
				#print date
				trade_status = data[16]
				dd1 = '交易'
				if trade_status != dd1:
					r = 0.0
					updown = '0'
				else:
					r = (float(data[5]) - float(data[1])) / float(data[1])
					updown = data[-1]
				d[date] = [date,r,updown]

			except:
				break
		if flag == 1:
			flag = 0
			continue
		k = sorted(d.keys())
		w = open(save_data_dir+os.sep+f_n[6:12]+'.txt', 'wb')
		for date in k:
			w.write(str(d[date][0])+','+str(d[date][1])+','+d[date][2]+'\r\n')
		w.close()
		print f_n[6:12]
				





