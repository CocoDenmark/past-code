# -*- coding:utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta



data_dir = 'G:\\Filesys\\script\\daily_renew\\j'

date1 = sys.argv[1]
date2 = sys.argv[2]

print date1, date2
file_read1 = open(data_dir+os.sep+date1+'.txt', 'rb')
file_read2 = open(data_dir+os.sep+date2+'.txt', 'rb')
stock_dict = dict()

while 1:
	try:
		line = file_read2.readline()
		line = line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		ex = data[1]
		pre_close = float(data[2])
		r = float(data[3])
		stock_dict[code] = [ex, pre_close, r, 0, 0]
	except:
		break

while 1:
	try:
		line = file_read1.readline()
		line = line.strip()
		data = line.split(',')
		if len(data) == 1:
			break
		code = data[0]
		r = float(data[3])
		if stock_dict.has_key(code) == True:
			stock_dict[code][4] = 1
			stock_dict[code][3] = r + stock_dict[code][2]
			print code
	except:
		break

for code in stock_dict.keys():
	if stock_dict[code][4] == 0:
		del(stock_dict[code])


#sorted_dict = stock_dict
sorted_dict = sorted(stock_dict.iteritems(), key=lambda d:d[1][3], reverse=True)
write_file = open(data_dir+os.sep+'2_day'+os.sep+date2+'.txt', 'wb')
print 11
'''
for code in sorted_dict.keys():
	write_file.write(code+',')
	write_file.write(sorted_dict[code][0]+','+str(sorted_dict[code][1])+','+str(sorted_dict[code][2])+','+str(sorted_dict[code][3])+'\r\n')
'''

for n_l in sorted_dict:
	write_file.write(n_l[0]+',')
	write_file.write(n_l[1][0]+','+str(n_l[1][1])+','+str(n_l[1][2])+','+str(n_l[1][3])+'\r\n')

write_file.close()

