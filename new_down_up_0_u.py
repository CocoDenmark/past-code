# -*- coding: utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta

get_data_dir = 'G:\\Filesys\\stock\\trade\\forward_Rehabilitation\\data\\daily\\current'
save_data_dir_down = 'G:\\Filesys\\script\\down_up\\down_0'
save_data_dir_up = 'G:\\Filesys\\script\\down_up\\up_0'
tomorrow = datetime.now()
aDay = timedelta(days=1)
tod = tomorrow - aDay
date = tod.strftime('%Y-%m-%d')
date = sys.argv[1]
print date
file_read = open(get_data_dir+os.sep+date+'.txt', 'rb')
file_read.readline()
result_up = []
result_down = []
i = 0
while 1:
	try:
		i = 1
		line = file_read.readline()
		line.strip()
		data = line.split('|')
		code = data[0]
		#print code
		pre_close = float(data[2])
		close = float(data[6])
		#print close
		maxupordown = int(data[19])
		#trade_status = data[17].decode('utf-8')
		trade_status = data[17]
		#print '交易'
		#print trade_status
		#dd1 = unicode("交易")
		dd1 = '交易'
		#print dd1
		#print type(trade_status),type(dd1)
		if trade_status != dd1:
			print '!!!!!!'
			continue
		#print trade_status
		#print maxupordown, '0000000'
		rc = close/pre_close - 1
		#print rc
		if maxupordown != 0:
			maxupordown = 1
			
		else:
			maxupordown = 0
		if code[0] == '6':
			exchange = '1'
		else:
			exchange = '2'
		print code, exchange, close, rc, maxupordown
		if rc > 0:
			result_up.append([code, exchange, close, rc, maxupordown])
		if rc < 0:
			result_down.append([code, exchange, close, rc, maxupordown])
	except:
		break

file_read.close()

file_write_down = open(save_data_dir_down+os.sep+date+'.txt', 'wb')
file_write_up = open(save_data_dir_up+os.sep+date+'.txt', 'wb')
length = len(result_down)
i = 0
while i < length:
	file_write_down.write(result_down[i][0] + ',' + result_down[i][1] + ',' + str(result_down[i][2]) + ',' + str(result_down[i][3]) + ',' + str(result_down[i][4])+'\r\n')
	i += 1
file_write_down.close()
length = len(result_up)
i = 0
while i < length:
	file_write_up.write(result_up[i][0] + ',' + result_up[i][1] + ',' + str(result_up[i][2]) + ',' + str(result_up[i][3]) + ',' + str(result_up[i][4])+'\r\n')
	i += 1
file_write_up.close()