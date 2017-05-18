# -*- coding:utf-8 -*-
import datetime
import os
import sys
#from datetime import datetime
#from datetime import timedelta


get_data_dir = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\down_1'
save_data_dir = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\down_3'


aDay = datetime.timedelta(days=1)
print aDay

date_result = sys.argv[1]
date = sys.argv[1]
day = date.split('-')

today = datetime.date(int(day[0]),int(day[1]),int(day[2]))
print today
t_1 = today - aDay
t = t_1
print today
print 't-1:'
while 1:
	try:
		date_t = t.strftime('%Y-%m-%d')
		print date_t
		file_read1 = open(get_data_dir+os.sep+date_t+'.txt', 'rb')
		break
	except:
		t = t - aDay
		continue
t_1 = t
t_2 = t - aDay
t = t_2
print 't-2:'
while 1:
	try:
		date_t = t.strftime('%Y-%m-%d')
		print date_t
		file_read2 = open(get_data_dir+os.sep+date_t+'.txt', 'rb')
		break
	except:
		t = t - aDay
		continue		
t_2 = t
t_3 = t - aDay
t = t_3
print 't-3:'
while 1:
	try:
		date_t = t.strftime('%Y-%m-%d')
		print date_t
		file_read3 = open(get_data_dir+os.sep+date_t+'.txt', 'rb')
		break
	except:
		t = t - aDay
		continue		
t_3 = t
file_read = open(get_data_dir+os.sep+date+'.txt', 'rb')
t0_dict = dict()
while 1:
	try:
		line = file_read.readline()
		line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		close = float(data[2])
		ex = data[1]
		r = float(data[3])
		new_list = [ex,close,r,r]
		t0_dict[code] = new_list
	except:
		break
file_read.close()

t1_dict = dict()
while 1:
	try:
		line = file_read1.readline()
		line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		close = float(data[2])
		ex = data[1]
		r = float(data[3])
		new_list = [ex,close,r]
		t1_dict[code] = new_list
	except:
		break
file_read1.close()

t2_dict = dict()
while 1:
	try:
		line = file_read2.readline()
		line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		close = float(data[2])
		ex = data[1]
		r = float(data[3])
		new_list = [ex,close,r]
		t2_dict[code] = new_list
	except:
		break
file_read2.close()

t3_dict = dict()
while 1:
	try:
		line = file_read3.readline()
		line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		close = float(data[2])
		ex = data[1]
		r = float(data[3])
		new_list = [ex,close,r]
		t3_dict[code] = new_list
	except:
		break
file_read3.close()

for code in t0_dict.keys():
	if code not in t1_dict.keys():
		t0_dict.pop(code)
	else:
		if code not in t2_dict.keys():
			t0_dict.pop(code)
		else:
			if code in t3_dict.keys():
				t0_dict.pop(code)
			else:
				t0_dict[code][3] = t0_dict[code][2] + t1_dict[code][2]

sorted_dict = sorted(t0_dict.iteritems(), key=lambda d:d[1][3], reverse=True)			
	

file_write = open(save_data_dir+os.sep+date_result+'.txt', 'wb')


for n_l in sorted_dict:
	file_write.write(n_l[0]+',')
	file_write.write(n_l[1][0]+','+str(n_l[1][1])+','+str(n_l[1][2])+','+str(n_l[1][3])+'\r\n')

file_write.close()
