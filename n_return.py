# -*- coding: utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta
from collections import deque

get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\return\\1_day'
f_l = os.listdir(get_data_dir)
days = [2,3,4,5,6,7,8,9,10,15,30]

for day in days[5:]:
	print day	
	save_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\return\\'+str(day)+'_day'
	try:
		os.mkdir(save_data_dir)
	except:
		pass
	flag = 0
	for f_n in f_l:
		#print f_n
		f = open(get_data_dir+os.sep+f_n, 'rb')
		q = deque([])
		new_list = []
		ave = 0.0
		n = 0.0
		i = 1
		ff = 1
		while i <= (day):
			try:
				line = f.readline().strip()
				data = line.split(',')
				if len(data) == 1:
					break
				q.append(float(data[1]))
				date = data[0]
				i += 1
			except:
				ff = 0
		if ff == 0 or len(q)<day:
			continue
		ave = 0.0
		qq = 0
		while qq<day:
			ave = ave+ q[int(qq)]
			qq += 1		
		new_list.append([date,float(ave/day)])
		q.popleft()
		while 1:
			try:
				line = f.readline().strip()
				data = line.split(',')
				if len(data) == 1:
					break
				if data[1] == 'nan':
					flag = 1
					break
				date = data[0]
				r = float(data[1])
				q.append(r)
				ave = 0.0
				qq = 0
				while qq<day:
					ave = ave+ q[int(qq)]
					qq += 1		
				new_list.append([date,float(ave/day)])
				q.popleft()
			except:
				break
		if flag == 1:
			flag = 0
			continue
		w = open(save_data_dir+os.sep+f_n, 'wb')
		for l in new_list:
			w.write(l[0]+','+str(l[1])+'\r\n')
		w.close()
				





