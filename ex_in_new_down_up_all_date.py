# -*- coding:utf-8 -*-
import datetime
import os
import sys
#from datetime import datetime
#from datetime import timedelta

date_list = ['2015-05-27','2015-05-28','2015-05-29','2015-06-01','2015-06-02','2015-06-03','2015-06-04','2015-06-05','2015-06-08','2015-06-09','2015-06-10','2015-06-11','2015-06-12','2015-06-15','2015-06-16','2015-06-17','2015-06-18','2015-06-19','2015-06-23','2015-06-24']
type_list = ['down', 'up']
count_list = [1,2,3]
for count in count_list:
	print count
	for type in type_list:
		get_data_0_dir = 'G:\\Filesys\\script\\down_up\\'+type+'_0'+'\\forward'
		for date in date_list[count:]:
			count_1 = count - 1
			ex_get_data_dir = 'G:\\Filesys\\script\\down_up\\excl_max\\'+type+'_'+str(count_1)
			in_get_data_dir = 'G:\\Filesys\\script\\down_up\\incl_max\\'+type+'_'+str(count_1)
			ex_save_data_dir = 'G:\\Filesys\\script\\down_up\\excl_max\\'+type+'_'+str(count)
			in_save_data_dir = 'G:\\Filesys\\script\\down_up\\incl_max\\'+type+'_'+str(count)
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
					if count == 1:
						file_read1_ex = open(get_data_0_dir+os.sep+date_t+'.txt', 'rb')
						file_read1_in = file_read1_ex
					else:
						file_read1_ex = open(ex_get_data_dir+os.sep+date_t+'.txt', 'rb')
						file_read1_in = open(in_get_data_dir+os.sep+date_t+'.txt', 'rb')
					break
				except:
					t = t - aDay
					continue
			print date_t

			file_read = open(get_data_0_dir+os.sep+date+'.txt', 'rb')
			t0_dict_ex = dict()
			t0_dict_in = dict()
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
					maxupordown = int(data[4])
					sum_r = 0.0
					if maxupordown == 0:
						t0_dict_ex[code] = [ex,close,r,sum_r]
						t0_dict_in[code] = [ex,close,r,sum_r]
				except:
					break
			file_read.close()


			t1_dict_ex = dict()
			t1_dict_in = dict()
			# exclude max up or down
			while 1:
				try:
					line = file_read1_ex.readline()
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
						maxupordown = int(data[4])
					else:
						sum_r = float(data[4])
						maxupordown = -1
					new_list = [ex,close,r,sum_r,maxupordown]
					t1_dict_ex[code] = new_list
				except:
					break
			file_read1_ex.close()


			while 1:
				try:
					line = file_read1_in.readline()
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
						maxupordown = int(data[4])
					else:
						sum_r = float(data[4])
						maxupordown = -1
					new_list = [ex,close,r,sum_r,maxupordown]
					t1_dict_in[code] = new_list
				except:
					break
			file_read1_in.close()


			if count == 1:
				for code in t0_dict_ex.keys():
					if code in t1_dict_ex.keys():
						t0_dict_ex.pop(code)
					else:
						t0_dict_ex[code][3] = t0_dict_ex[code][2]
				for code in t0_dict_in.keys():
					if code in t1_dict_in.keys() and t1_dict_in[code][4]!=0:
						t0_dict_in.pop(code)
					else:
						t0_dict_in[code][3] = t0_dict_in[code][2]

			else:
				for code in t0_dict_ex.keys():
					if code not in t1_dict_ex.keys():
						t0_dict_ex.pop(code)
					else:
						t0_dict_ex[code][3] = t0_dict_ex[code][2] + t1_dict_ex[code][3]
				for code in t0_dict_in.keys():
					if code not in t1_dict_in.keys():
						t0_dict_in.pop(code)
					else:
						t0_dict_in[code][3] = t0_dict_in[code][2] + t1_dict_in[code][3]

			sorted_dict_ex = sorted(t0_dict_ex.iteritems(), key=lambda d:d[1][3], reverse=True)
			sorted_dict_in = sorted(t0_dict_in.iteritems(), key=lambda d:d[1][3], reverse=True)				
	
			file_write_ex = open(ex_save_data_dir+os.sep+date+'.txt', 'wb')
			file_write_in = open(in_save_data_dir+os.sep+date+'.txt', 'wb')


			for n_l in sorted_dict_ex:
				file_write_ex.write(n_l[0]+',')
				file_write_ex.write(n_l[1][0]+','+str(n_l[1][1])+','+str(n_l[1][2])+','+str(n_l[1][3])+'\r\n')
			for n_l in sorted_dict_in:
				file_write_in.write(n_l[0]+',')
				file_write_in.write(n_l[1][0]+','+str(n_l[1][1])+','+str(n_l[1][2])+','+str(n_l[1][3])+'\r\n')

			file_write_ex.close()
			file_write_in.close()




