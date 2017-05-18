# -*- coding: utf-8 -*-
import datetime
import os
import sys
dir_getlist = 'f:\\miao\\stock_list\\'
f = open(dir_getlist+os.sep+'hs300.txt','rb')
line = f.readline().strip()
list_300 = line.split(',')
f.close()

f = open(dir_getlist+os.sep+'shang50.txt','rb')
line = f.readline().strip()
list_50 = line.split(',')
f.close()

f = open(dir_getlist+os.sep+'zhong500.txt','rb')
line = f.readline().strip()
list_500 = line.split(',')
f.close()

code_list = [list_300, list_50, list_500]

#stock_return_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\return\\1_day'
stock_return_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily\\return_new'
stock = dict()

for cc in code_list:
	for code in cc:
		f = open(stock_return_dir+os.sep+code[0:6]+'.txt', 'rb')
		stock[code] = dict()
		while 1:
			try:
				line = f.readline().strip()
				data = line.split(',')
				if len(data) == 1:
					break
				date = datetime.date(int(data[0][0:4]), int(data[0][5:7]), int(data[0][8:10]))
				if date < datetime.date(2000,1,1):
					continue
				stock[code][date] = float(data[1])
			except:
				break
		f.close()

date_list = sorted(stock['000002.SZ'].keys())

i = 0
print 'here!!!!!!'
for cc in code_list:
	f = open('G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\market_return\\'+ str(i)+'.txt', 'wb')
	print '111'
	i = i + 1
	print date_list
	for date in date_list:
		print date
		ave = 0.0
		n = 0.0
		for code in cc:
			try:
				ave = (ave*n + stock[code][date])/(n+1)
				n = n + 1
			except:
				continue
		f.write(str(date)+','+str(ave)+','+str(n)+'\r\n')
	f.close()
		

			


				

		