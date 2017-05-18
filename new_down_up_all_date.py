# -*- coding:utf-8 -*-
import datetime
import os
import sys
#from datetime import datetime
#from datetime import timedelta

date_list = ['2015-05-27','2015-05-28','2015-05-29','2015-06-01','2015-06-02','2015-06-03','2015-06-04','2015-06-05','2015-06-08','2015-06-09','2015-06-10','2015-06-11','2015-06-12','2015-06-15','2015-06-16','2015-06-17','2015-06-18','2015-06-19','2015-06-23','2015-06-24','2015-06-25']
type_list = ['down', 'up']
count_list = [1,2,3]
for count in count_list:
	print count
	for type in type_list:
		get_data_0_dir = 'G:\\Filesys\\script\\down_up\\'+type+'_0'
		for date in date_list[count:]:
			count_1 = count - 1
			get_data_dir = 'G:\\Filesys\\script\\down_up\\'+type+'_'+str(count_1)
			save_data_dir = 'G:\\Filesys\\script\\down_up\\'+type+'_'+str(count)
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

			file_read = open(get_data_0_dir+os.sep+date+'.txt', 'rb')
			t0_dict = dict()
			while 1:
				try:
					line = file_read.readline()
					line.strip()
					data = line.split(',')
					if len(data) == 1:
						break
					code = data[0]
					print code
					close = float(data[2])
					ex = data[1]
					r = float(data[3])
					maxupordown = float(data[4])
					sum_r = 0.0
					if maxupordown == 0.0:
						t0_dict[code] = [ex,close,r,sum_r]
						t0_dict[code] = [ex,close,r,sum_r]
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

			if count == 1:
				for code in t0_dict.keys():
					if code in t1_dict.keys():
						t0_dict.pop(code)
					else:
						t0_dict[code][3] = t0_dict[code][2]

			else:
				for code in t0_dict.keys():
					if code not in t1_dict.keys():
						t0_dict.pop(code)
					else:
						t0_dict[code][3] = t0_dict[code][2] + t1_dict[code][3]

			sorted_dict = sorted(t0_dict.iteritems(), key=lambda d:d[1][3], reverse=True)
	
			file_write = open(save_data_dir+os.sep+date+'.txt', 'wb')


			for n_l in sorted_dict:
				file_write.write(n_l[0]+',')
				file_write.write(n_l[1][0]+','+str(n_l[1][1])+','+str(n_l[1][2])+','+str(n_l[1][3])+'\r\n')

			file_write.close()




