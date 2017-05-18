# -*- coding: utf-8 -*-
import datetime
import os
import sys



get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily_f'
save_data_dir = 'G:\\Filesys\\script\\daily_renew\\low_high'
get_current_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\current'

f_l = os.listdir(get_data_dir)
date1 = datetime.date(2014,9,9)
date2 = datetime.date(2014,10,24)
date3 = datetime.date(2015,4,1)
date4 = datetime.date(2015,6,1)
date5 = datetime.date(2014,6,10)
for f_n in f_l:
	print f_n
	f = open(get_data_dir+os.sep+f_n,'rb')
	f.readline()
	i1 = 0
	i2 = 0
	i3 = 0
	i4 = 0
	flag = 1
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

			if date < date1:
				continue
			elif date2 < date and date < date3:
				continue
			trade_status = data[16]
			dd1 = '交易'
			if trade_status != dd1:
				continue
			else:
				high = float(data[3])
				low = float(data[4])	
				close = float(data[5])
				if date < date2:
					if i1 == 0:
						high1_temp = high
						high1_date = date
						high1_close_temp = close
						high1_close_date = date
						i1 = 1
					else:
						if high >= high1_temp:
							high1_temp = high
							high1_date = date
						if close >= high1_close_temp:
							high1_close_temp = close
							high1_close_date = date
				if date3<date and date<date5:
					if i2 == 0:
						high2_temp = high
						high2_date = date
						high2_close_temp = close
						high2_close_date = date
						i2 = 1
					else:
						if high >= high2_temp:
							high2_temp = high
							high2_date = date
						if close >= high2_close_temp:
							high2_close_temp = close
							high2_close_date = date

				if date >= date5:
					if i4 == 0:
						high4_temp = high
						high4_date = date
						high4_close_temp = close
						high4_close_date = date
						low4_temp = low
						low4_date = date
						low4_close_temp = close
						low4_close_date = date
						i4 = 1
					else:
						if high >= high4_temp:
							high4_temp = high
							high4_date = date
						if close >= high4_close_temp:
							high4_close_temp = close
							high4_close_date = date
						if low <= low4_temp:
							low4_temp = low
							low4_date = date
						if close <= low4_close_temp:
							low4_close_temp = close
							low4_close_date = date

		except:
			break
	f.close()
	if flag == 0:
		continue
	f = open(save_data_dir+os.sep+'result_2014_2015.csv','a')
	code = f_n[6:12]
	if code[0:3] == '002':
		ex = 3
	elif code[0:3] == '000':
		ex = 1
	elif code[0] == '3':
		ex = 2
	elif code[0] == '6':
		ex = 0

	f.write(code+','+str(ex)+','+str(high1_temp)+','+str(high1_date)+','+str(high1_close_temp)+','+str(high1_close_date))
	f.write(','+str(high2_temp)+','+str(high2_date)+','+str(high2_close_temp)+','+str(high2_close_date))

	f.write(','+str(high4_temp)+','+str(high4_date)+','+str(high4_close_temp)+','+str(high4_close_date)+','+str(low4_temp)+','+str(low4_date)+','+str(low4_close_temp)+','+str(low4_close_date)+'\n')			
	f.close()
	print code
