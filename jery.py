# -*- coding:utf-8 -*-
# This python script download data automatically from wind Python API and report via emails.
# 2015-05-27
# created by Miao Zhou at 3zcapital

# import package
import sys
from WindPy import w
import time
from datetime import datetime
from datetime import timedelta
import os

# reload the system to encode by utf-8 dealling with Chinese characters
reload(sys)
sys.setdefaultencoding('utf8')

# the first time stamp to mark the start time
time1 = time.time()
start_time = str(time.asctime(time.localtime(time.time())))

# read all the stock code from stock_a.txt, which is also from wind
code_file = open('stock_a.txt', 'rb')
line = code_file.readline()
line = line.strip()
code_list = line.split(',')
print 'total:', len(code_list)

error_file = open('G:\\Filesys\\script\\daily_renew\\For_Jery\\error_file.txt', 'wb')
# start wind
w.start(waitTime=60)

fail_list = list()
sum = 0

# here starts to download data and write txt file for each stock
for code in code_list:
	open_file = open('G:\\Filesys\\script\\daily_renew\\For_Jery'+os.sep+code[0:6]+'.txt', 'rb')
	open_file.readline()
	last_time = open_file.read()
	open_file.close()
	d = w.wsd(code, "pre_close, close, ev, mkt_cap_ard, pb_lf", "2006-12-29", "2006-12-29", "Fill=Previous;PriceAdj=B")
	
# this is what happen when something wrong with the network connection
	if d.ErrorCode != 0:
		print 'error at ', code
		error_file.write(code+'|')
		time.sleep(2)
		continue

# here begins to write the downloaded data into txt files
	length = len(d.Fields)
	write_file = open('G:\\Filesys\\script\\daily_renew\\For_Jery'+os.sep+code[0:6]+'_1.txt', 'wb')
	write_file.write('DATE|')
	k = 0
	for fields in d.Fields:
		write_file.write(fields)
		if k < (length-1):
			write_file.write('|')
		k += 1
	write_file.write('\r\n')
	
	i = 0
	for date in d.Times:
		day = str(date)
		write_file.write(day[0:10]+'|')
	
		j = 0
		while j<length:
			try:
				 d.Data[j][i] = d.Data[j][i].encode('utf-8')
			except:
				None
			write_file.write(str(d.Data[j][i]))
			if j < (length-1):
				write_file.write('|')
			j += 1
		write_file.write('\r\n')
		i += 1
	print code
	write_file.write(last_time)
	write_file.close()		
error_file.close()





