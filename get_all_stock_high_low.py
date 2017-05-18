# -*- coding: utf-8 -*-
import datetime
import os
import sys



get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily_f'
save_data_dir = 'G:\\Filesys\\script\\daily_renew\\low_high'
get_current_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\current'

d = dict()
curf = open(get_current_dir+os.sep+'2015-07-01.txt', 'rb')
curf.readline()
while 1:
	try:
		line = curf.readline().strip()
		data = line.split('|')
		if len(data) == 1:
			break
		code = data[0]
		cl = float(data[6])
		trade_status = data[-2]
		dd1 = '交易'
		if trade_status != dd1:
			d[code] = [-1]
		else:
			d[code] = [cl]
	except:
		break

curf.close()

curf = open(get_current_dir+os.sep+'2015-07-02.txt', 'rb')
curf.readline()
while 1:
	try:
		line = curf.readline().strip()
		data = line.split('|')
		if len(data) == 1:
			break
		code = data[0]
		trade_status = data[-2]
		dd1 = '交易'
		if trade_status != dd1:
			d[code].append(-1)
		else:
			d[code].append(data[6])
	except:
		break

curf.close()

curf = open(get_current_dir+os.sep+'2015-07-03.txt', 'rb')
curf.readline()
while 1:
	try:
		line = curf.readline().strip()
		data = line.split('|')
		if len(data) == 1:
			break
		code = data[0]
		trade_status = data[-2]
		dd1 = '交易'
		if trade_status != dd1:
			d[code].append(-1)
		else:
			d[code].append(data[6])
	except:
		break

curf.close()


f_l = os.listdir(get_data_dir)
start_point = datetime.date(2015,6,10)
for f_n in f_l:
	print f_n
	f = open(get_data_dir+os.sep+f_n,'rb')
	f.readline()
	i = 0
	flag = 1
	pre_date = datetime.date(1991,1,1)
	current_sta = 1
	while 1:
		try:	
			line1 = f.readline().strip()
			data =line1.split('|')
			if len(data) == 1:
				break
			if data[1] == 'nan':
				flag = 0
				break
			data[0] = data[0].split('-')
			date = datetime.date(int(data[0][0]),int(data[0][1]),int(data[0][2][0:2]))
			if date < start_point:
				continue
			if date == pre_date:
				continue
			trade_status = data[16]
			dd1 = '交易'
			if trade_status != dd1:
				if current_sta != 0:
					current_date = date
				current_sta = 0
				continue
			else:
				current_sta = 1
				current_date = date
				pre_date = date
				high = float(data[3])
				low = float(data[4])	
				close = float(data[5])
				if i == 0:
					low_temp = low
					low_date = date
					low_close_temp = close
					low_close_date = date
					high_temp = high
					high_date = date
					high_close_temp = close
					high_close_date = date
					i = 1
				else:
					if high >= high_temp:
						high_temp = high
						high_date = date
					if low <= low_temp:
						low_temp = low
						low_date = date
					if close >= high_close_temp:
						high_close_temp = close
						high_close_date = date
					if close <= low_close_temp:
						low_close_temp = close
						low_close_date = date
		except:
			break
	f.close()
	if flag == 0 or i == 0:
		continue
	f = open(save_data_dir+os.sep+'result.csv','a')
	code = f_n[6:12]
	if code[0:3] == '002':
		ex = 3
	elif code[0:3] == '000':
		ex = 1
	elif code[0] == '3':
		ex = 2
	elif code[0] == '6':
		ex = 0

	high618 = high_temp * 0.618
	per = (low_temp - high618)/high618

	f.write(code+','+str(ex)+','+str(high_temp)+','+str(high_date)+','+str(high_close_temp)+','+str(high_close_date)+','+str(low_temp)+','+str(low_date)+','+str(low_close_temp)+','+str(low_close_date)+','+','+str(high618)+','+str(per)+','+str(current_sta)+','+str(current_date))			
	

	cu = d[code]
	for current in cu:
		if float(current) == -1:
			cuper = '-1'
		else:
			cuper = (float(current)-high618)/high618
		f.write(','+str(current)+','+str(cuper))
	f.write('\n')
	f.close()
	print code
