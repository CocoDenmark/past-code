# -*- coding:utf-8 -*-
# This python script deals with the error file, in which the download-failed codes are recorded.
# 2015-05-29
# created by Miao Zhou at 3zcapital

# import package
import sys
import time
import os
import datetime

 
dir1 = 'G:\\filesys\\script\\daily_renew\\current_stock_sina\\'
date = sys.argv[1]
dir1 = dir1+date
print dir1

try:
	os.mkdir(dir1+os.sep+'data')
except:
	pass
c = ['0','6','3']
file_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
close1 = datetime.time(hour=11,minute=31,second=0)
open2 = datetime.time(hour=12,minute=59,second=0)
close2 = datetime.time(hour=15,minute=1,second=0)


time1 = time.time()
for f in file_list:
	r_f = open(dir1+os.sep+f+'.txt', 'rb')	
	time_stamp = ''
	end = 0
	while end == 0:
		count = 0
		data_block = {}
		while count < 50000:
			try:
				line = r_f.readline()
				line = line.strip()
				if len(line)==1 or len(line)==0:
					end = 1
					break	
				if len(line)<24:
					continue
				ctime=line[-13:-5]
				code = line[13:19]
				if  code[0] not in c:
					print line
					continue
				if code not in data_block.keys():
					data_block[code] = []
				if len(data_block[code]) > 0 and data_block[code][-1][0:8]== ctime:
					continue
				xx=line.find(',')
				main=line[xx:-25]
				data_block[code].append(ctime+main)
				count += 1
			except:
				continue
		print f,count
		for code in data_block.keys():	
			try:
				ff = open(dir1+os.sep+'data'+os.sep+code+'.txt', 'a')	
				for line in data_block[code]:
					ff.write(line+'\r\n')
				ff.close()
			except:
				continue
	r_f.close()
time2 = time.time()
l = 'Run Time: ' + str(time2-time1) + ' seconds'
print l