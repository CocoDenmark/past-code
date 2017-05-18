# -*- coding: utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta

get_data_dir1 = 'G:\\Filesys\\stock\\stock_list'
get_data_dir2 = 'G:\\Filesys\\script\\daily_renew\\low_high'

ff = open(get_data_dir1+os.sep+'2015-05-25.txt', 'rb')

line = ff.readline().strip()
code_list = line.split(',')
code_list = code_list[0:-1]
code_list1 = []
for c in code_list:
	#print c
	code_list1.append(c[2:])
ff.close()

w = open(get_data_dir2+os.sep+'absense.txt','wb')
f = open(get_data_dir2+os.sep+'result.csv','rb')
i = 0
code_list2 = []
while 1:
	try:
		line = f.readline().strip()
		if line == '':
			break
		code = line[0:6]
		code_list2.append(code)
	except:
		break
for c in code_list1:
	if c not in code_list2:
		print c
		w.write(c+',')
