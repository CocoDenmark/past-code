# -*- coding:utf-8 -*-
# created by: Miao Zhou
# 4/20/2015
# used to download data from Wind and store data in csv format
# this file cannot deal with unicode&utf-8, which means do not download data with Chinese characters from wind or it requires extra work


import sys
from WindPy import w
import datetime
import time
import csv
import os
reload(sys)
sys.setdefaultencoding('utf8')

today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
dir1 = 'G:\\Filesys\\script\\daily_renew\\low_high'

f = open(dir1+os.sep+'absense.txt', 'rb')
line = f.readline().strip()
print line
code = line.split(',')
code_list =[]
for c in code[:-1]:
	if c[0] == '6':
		code_list.append(c+'.SH')
	else:
		code_list.append(c+'.SZ')
f.close()


# ------------------------get data from wind and write to csv files
# start wind
w.start(waitTime=60)

error_file = open(dir1 + os.sep + 'ab\\fail_list_daily.txt','wb')


start_point = 0

for code in code_list[start_point:]:
# get data
	try:
		ipo = w.wsd(code,"ipo_date", today, today,"Period=Q;Fill=Previous")
		ipo_date = str(ipo.Data[0][0].year) + '-' + str(ipo.Data[0][0].month).zfill(2) + '-' + str(ipo.Data[0][0].day).zfill(2)
	except:
		ipo_date = '1991-01-01'
	d = w.wsd(code, "pre_close,open,high,low,close,volume,amt,dealnum,chg,pct_chg,swing,vwap,adjfactor,turn,free_turn,trade_status,susp_reason,maxupordown", ipo_date, today, "Fill=Previous;PriceAdj=F")

	
	if d.ErrorCode != 0:
		print 'error at ', code
		error_file.write(code+'|')
		time.sleep(2)
		continue

	if d.Data[0][0] == 'nan' and d.Data[1][0] == 'nan':
		print code,'!!!!!!!!'
		continue
	if d.Data[0][0] == -1 and d.Data[1][0] == -1:
		print code,'!!!!!!!!'
		continue


	length = len(d.Fields)
	txt_file = open(dir1 + os.sep + 'ab\\daily_'+code+'.txt', 'wb')
	txt_file.write('DATE|')
	k = 0
	for fields in d.Fields:
		txt_file.write(fields)
		if k < (length-1):
			txt_file.write('|')
		k += 1
	txt_file.write('\r\n')
	i = 0
	for date in d.Times:
		txt_file.write(str(date)+'|')
	
		j = 0
		while j<length:
			try:
				 d.Data[j][i] = d.Data[j][i].encode('utf-8')
			except:
				None
			txt_file.write(str(d.Data[j][i]))
			if j < (length-1):
				txt_file.write('|')
			j += 1
		txt_file.write('\r\n')
		i += 1
	
	print code
	txt_file.close()
w.stop()
error_file.close()
