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

# start wind
w.start(waitTime=60)
#tomorrow = datetime.now()
#aDay = timedelta(days=1)
#tod = tomorrow - aDay
#today = tod.strftime('%Y-%m-%d')
#print today
#today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
today = '2015-07-22'

# here begins the trade data (without rehabilitation) download process by setting the destinate dir
base_dir = 'G:\\Filesys\\stock\\standards\\data\\'
error_file = open('G:\\Filesys\\stock\\standards\\error_file\\fail_daily_renew_'+today+'.txt','wb')

renew_dict = list()
fail_list = list()
sum = 0


code_file = open('G:\\Filesys\\stock_set\\'+'2015-07-22'+'.txt', 'rb')
line = code_file.readline()
line = line.strip()
code_l = line.split(',')
code_list = []
for c in code_l[:-1]:
	if c[0] == '6':
		code = c+'.SH'
	else:
		code = c+'.SZ'
	code_list.append(code)
print 'total:', len(code_list)
# here starts to download data and write txt file for each stock
for code in code_list:

	d = w.wsd(code,  "industry_gicscode,pb_mrq,pb_lf", "2015-07-22", "2015-07-22", "industryType=1;Fill=Previous")
	
# this is what happen when something wrong with the network connection
	if d.ErrorCode != 0:
		print 'error at ', code
		error_file.write(code+'|')
		fail_list.append(code)
		time.sleep(2)
		continue

# here begins to write the downloaded data into txt files
	length = len(d.Fields)
	renew_line = code[0:6]+'|'

	i = 0
	for date in d.Times:
		renew_line = renew_line + str(date)+'|'
	
		j = 0
		while j<length:
			try:
				 d.Data[j][i] = d.Data[j][i].encode('utf-8')
			except:
				None
			renew_line = renew_line + str(d.Data[j][i])
			if j < (length-1):
				renew_line = renew_line + '|'
			j += 1
		i += 1
	renew_dict.append(renew_line)
	print 'standards: ', code
	sum += 1	
error_file.close()

renew_file = open(base_dir + today + '.txt', 'wb')
title = 'CODE|DATE'
for f in d.Fields:
	title = title + '|' + f
renew_file.write(title+'\r\n')
for c in renew_dict:
	renew_file.write(c+'\r\n')
renew_file.close()
