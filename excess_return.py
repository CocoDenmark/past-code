# -*- coding: utf-8 -*-
import datetime
import os
import sys
import datetime

get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\return\\1_day'
previous_l = [1,2,3,4,5]
start_pre = ['2015-01-05', '2014-12-31','2014-12-30','2014-12-29','2014-12-26']
start_date = datetime.date(2014,12,1)
f_l = os.listdir(get_data_dir)

return_dict_sh = dict()
return_dict_sz = dict()
return_dict_g = dict()
return_dict_s = dict()
dict_list = [return_dict_sh, return_dict_sz,return_dict_g,return_dict_s]
for f_n in f_l:
	f = open(get_data_dir+os.sep+f_n, 'rb')
	code = f_n[0:6]
	if code[0] == '6':
		type = 0
	elif code[0:3] == '000':
		type = 1
	elif code[0:3] == '002':
		type = 3
	elif code[0] == '3':
		type = 2
	dict_list[type][code] = [[],[]]
	while 1:
		try:
			line = f.readline()
			line = line.strip()
			data = line.split(',')
			if len(data) == 1:
				break
			data[0] = data[0].split('-')
			date = datetime.date(int(data[0][0]),int(data[0][1]),int(data[0][2]))
			if date >= start_date:
				dict_list[type][code][0].append(date)
				dict_list[type][code][1].append(float(data[1]))
		except:
			break
	f.close()

get_market_dir = 'G:\\Filesys\\stock\\makert_return'

f_l = ['sh.txt','sz_main.txt','sz_growth.txt','sz_smail.txt']
market_return = [[[],[]],[[],[]],[[],[]],[[],[]]]
i = 0
while i < 4:
	f = open(get_market_dir+os.sep+f_l[i], 'rb')
	while 1:
		try:
			line = f.readline()
			line = line.strip()
			data = line.split(',')
			if len(data) == 1:
				break
			data[0] = data[0].split('-')
			date = datetime.date(int(data[0][0]),int(data[0][1]),int(data[0][2]))
			if date >= start_date:
				market_return[i][0].append(date)
				market_return[i][1].append(float(data[1]))
		except:
			break
	f.close()
	i += 1

pre_return = [[],[],[],[]]				
for pre in previous_l:
	i = 0
	while i < 4:
		start_location = market_return[i][0].index(start_pre[pre-1])
		j = start_location 
		date = market_return[i][0][j]
		while j+pre < len(market_return[i][0]:
			trade_date = market_return[i][j+pre-1]
			pre_return[i].append([trade_date,[]])
			for code in dict_list[i].keys():
				if date not in dict_list[i][code][0]:
					continue
				else:
					l = dict_list[i][code][0].index(date)
				flag = 1
				day = 0
				r = 1.0
				while day < pre:
					ri = dict_list[i][code][1][l]
					if ri == 0.0:
						flag = 0
						break
					r = r*(1+ri)
					day += 1
					l += 1
				if flag == 0:
					continue
				pre_return[i][-1][1].append([code,r-1])
			j += 1




				

