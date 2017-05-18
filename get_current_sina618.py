#encoding=utf-8
from multiprocessing import Process
import os
import time
import urllib
import datetime

data_dir = 'G:\\filesys\\script\\daily_renew\\low_high'


if 1:

	code_list = []
	cf = open(data_dir+os.sep+'result.csv', 'rb')
	i = 0
	ll = ''
	while 1:
		try:
			if i == 800:
				code_list.append(ll[1:])
				ll = ''
				i = 0
			line = cf.readline().strip()
			data = line.split(',')
			if len(data) == 1:
				break
			code = data[0]
			if code[0] == '6':
				code = 'sh' + code
			else:
				code = 'sz' + code
			ll = ll + ',' + code
			i += 1
		except:
			break
	cf.close()

	baseUrl = 'http://hq.sinajs.cn/list=' 

	current_d = dict()
	for ll in code_list:
		urlItem = urllib.urlopen(baseUrl+ll)
		get = urlItem.read().strip()
		get = get.split(';')
		for g in get[:-1]:
			data = g.split('"')
			print data
			data[0] = data[0].split('_')
		
			code = data[0][2][2:8]
			print code
			data[1] = data[1].split(',')
			price = data[1][3]
			time = data[1][31]
			current_d[code] = [price,time]

	cf_n = os.listdir(data_dir+'\\current')
	cf = open(data_dir+'\\current\\'+cf_n[-1], 'rb')
	result = open(data_dir+'\\current\\'+cf_n[-1][:-4]+'2.csv', 'wb')


	while 1:
		try:
			line = cf.readline().strip()
			line1 = line
			data = line.split(',')
			if len(data) == 1:
				break
			code = data[0]
			try:
				line1 = line1 + ',' + current_d[code][1] +','+ current_d[code][0] +'\n'
			except:
				pass
			result.write(line1)
		except:
			break
	cf.close()
	result.close()





