# -*- coding:utf-8 -*-
import datetime
import os
import sys



get_data_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\current'
save_data_dir_down = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\down_0'
save_data_dir_up = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\up_0'
today = datetime.datetime.now()
aDay = datetime.timedelta(days=1)
today = today - aDay
date = today.strftime('%Y-%m-%d')
date_result = date
print date
file_read = open(get_data_dir+os.sep+date+'.txt', 'rb')
file_read.readline()
result_up = []
result_down = []
while 1:
	try:
		line = file_read.readline()
		line.strip()
		data = line.split('|')
		code = data[0]
		#print code
		pre_close = float(data[2])
		close = float(data[6])
		#print close
		maxupordown = int(data[22])
		#print maxupordown, '0000000'
		rc = close/pre_close - 1
		#print rc
		if maxupordown != 0:
			continue
		else:
			#print code[0]
			if code[0] == '6':
				exchange = '1'
			else:
				exchange = '2'
			print code, exchange, close, rc
			if rc > 0:
				result_up.append([code, exchange, close, rc])
			if rc < 0:
				result_down.append([code, exchange, close, rc])
	except:
		break

file_read.close()

file_write_down = open(save_data_dir_down+os.sep+date_result+'.txt', 'wb')
file_write_up = open(save_data_dir_up+os.sep+date_result+'.txt', 'wb')
length = len(result_down)
i = 0
while i < length:
	file_write_down.write(result_down[i][0] + ',' + result_down[i][1] + ',' + str(result_down[i][2]) + ',' + str(result_down[i][3]) +'\r\n')
	i += 1
file_write_down.close()
length = len(result_up)
i = 0
while i < length:
	file_write_up.write(result_up[i][0] + ',' + result_up[i][1] + ',' + str(result_up[i][2]) + ',' + str(result_up[i][3]) +'\r\n')
	i += 1
file_write_up.close()

ddate = date
date_list = [ddate]
type_list = ['down', 'up']
count_list = [1,2,3]
for count in count_list:
	print count
	for type in type_list:
		for date in date_list:
			date_result = date
			count_1 = count - 1
			get_data_dir = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\'+type+'_'+str(count_1)
			save_data_dir = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\'+type+'_'+str(count)
			aDay = datetime.timedelta(days=1)
			day = date.split('-')
			today = datetime.date(int(day[0]),int(day[1]),int(day[2]))
			print count, type, today
			t_1 = today - aDay
			t = t_1
			print 't-1:'
			i = 0
			while 1:
				i += 1
				if i > 5:
					print 'no corresponding file!'
					exit(0)
				try:
					date_t = t.strftime('%Y-%m-%d')
					print date_t
					file_read1 = open(get_data_dir+os.sep+date_t+'.txt', 'rb')
					break
				except:
					t = t - aDay
					continue
			print date_t

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
					if count == 1:
						sum_r = r
					else:
						sum_r = float(data[4])
					new_list = [ex,close,r,sum_r]
					t1_dict[code] = new_list
				except:
					break
			file_read1.close()

			for code in t0_dict.keys():
				if code not in t1_dict.keys():
					t0_dict.pop(code)
				else:
					t0_dict[code][3] = t0_dict[code][2] + t1_dict[code][3]

			sorted_dict = sorted(t0_dict.iteritems(), key=lambda d:d[1][3], reverse=True)			
	
			file_write = open(save_data_dir+os.sep+date_result+'.txt', 'wb')


			for n_l in sorted_dict:
				file_write.write(n_l[0]+',')
				file_write.write(n_l[1][0]+','+str(n_l[1][1])+','+str(n_l[1][2])+','+str(n_l[1][3])+'\r\n')

			file_write.close()












