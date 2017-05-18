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
import smtplib  
from email.MIMEText import MIMEText  
from email.Utils import formatdate  
from email.Header import Header  

# reload the system to encode by utf-8 dealling with Chinese characters
reload(sys)
sys.setdefaultencoding('utf8')

# the first time stamp to mark the start time
time1 = time.time()
start_time = str(time.asctime(time.localtime(time.time())))
today = sys.argv[1]
# read all the stock code from stock_a.txt, which is also from wind
code_file = open('G:\\Filesys\\stock\\makert_return\\'+today+'.txt', 'rb')
line = code_file.readline()
line = line.strip()
code_list = line.split(',')
#print code_list, len(code_list)
print 'total:', len(code_list)

# start wind
w.start(waitTime=60)



# here begins the trade data (forward rehabilitation) download process by setting the destinate dir
base_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily\\current\\'
error_file = open('G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\error_file\\fail_daily_renew_'+today+'.txt','a')


fail_list = list()
renew_dict = list()
sum = 0

# here starts to download data and write txt file for each stock
for code in code_list:
	if code[0] == '6':
		code = code+'.SH'
	else:
		code = code+'.SZ'
	d = w.wsd(code, "pre_close,open,high,low,close,volume,amt,dealnum,chg,pct_chg,swing,vwap,adjfactor,turn,free_turn,trade_status,susp_reason,maxupordown", today, today, "Fill=Previous;PriceAdj=F", "showblank=-1")
	print d
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
	print 'trade_f: ', code
	sum += 1	
error_file.close()

renew_file = open(base_dir + today + '.txt', 'a')
title = 'CODE|DATE'
for f in d.Fields:
	title = title + '|' + f
#renew_file.write(title+'\r\n')
for c in renew_dict:
	renew_file.write(c+'\r\n')
renew_file.close()
error_file.close()


