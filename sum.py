# -*- coding:utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta


get_data_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\current'
save_data_dir = 'G:\\Filesys\\script\\daily_renew\\j'

tomorrow = datetime.now()
aDay = timedelta(days=1)
tod = tomorrow - aDay
date = tod.strftime('%Y-%m-%d')

date_result = tod.strftime('%Y%m%d')
#date = '2015-06-19'
print date
file_read = open(get_data_dir+os.sep+date+'.txt', 'rb')
file_read.readline()
result = []
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
		if rc >= 0 :
			continue
		else:
			#print 'here'
			if maxupordown != 0:
				continue
			else:
				#print code[0]
				if code[0] == '6':
					exchange = '1'
				else:
					exchange = '2'
				print code, exchange, close, rc
				result.append([code, exchange, close, rc])
	except:
		break

file_read.close()

file_write = open(save_data_dir+os.sep+date_result+'.txt', 'wb')

length = len(result)
i = 0
while i < length:
	#print result[i][0]
	file_write.write(result[i][0] + ',' + result[i][1] + ',' + str(result[i][2]) + ',' + str(result[i][3]) +'\r\n')
	i += 1
file_write.close()