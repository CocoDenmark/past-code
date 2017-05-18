# -*- coding:utf-8 -*-
# This python script download data automatically from wind Python API and report via emails.
# 2015-05-27
# created by Miao Zhou at 3zcapital

import os

dir_get = 'G:\\Filesys\\script\\daily_renew\\low_high\\ab'
dir_save = 'G:\\Filesys\\script\\daily_renew\\low_high\\add'

f_l = os.listdir(dir_get)
for f_n in f_l:
	f = open(dir_get+os.sep+f_n, 'rb')
	w = open(dir_save+os.sep+f_n, 'wb')
	l = f.readline().strip()
	w.write(l+'\r\n')
	
	while 1:
		try:
			line = f.readline().strip()
			new_line = line
			data = line.split('|')
			if len(data) == 1:
				break
			if data[2] == 'None':
				continue
			else:
				w.write(new_line+'\r\n')
		except:
			break
	f.close()
	w.close()
	print f_n
				
			
			