#encoding=utf-8
import os
import time
import urllib
import datetime
dirA = 'G:\\filesys\\stock\\stock_list\\stock_a'
dirB = 'G:\\filesys\\stock\\stock_list\\stock_b'
dirG = 'G:\\filesys\\stock\\stock_list\\stock_growth'
dirS = 'G:\\filesys\\stock\\stock_list\\stock_small'
today = datetime.datetime.now()
today = today.strftime('%Y-%m-%d')
baseUrl = 'http://hq.sinajs.cn/list=' 
code_listA = []
code_listB = []
code_listG = []
code_listS = []
fail_list = []
code_list = [code_listA, code_listB, code_listG, code_listS]
i = 1
while i < 900999:
	stock = str(i).zfill(6)
	if stock[0] == '6' or stock[0] == '9':
		stock = 'sh' + stock
	else:
		stock = 'sz' + stock
	try:
		urlItem = urllib.urlopen(baseUrl+stock)
		line = urlItem.read().split('"')
		if line[1] == '':
			continue
		else:		
			print stock
			if stock[0:3] == '601' or stock[0:3] == '600':
				code_listA.append(stock)
			elif stock[0:3] == '300':
				code_listG.append(stock)
			elif stock[0:3] == '900':
				code_listB.append(stock)
			elif stock[0:3] == '000':
				code_listA.append(stock)
			elif stock[0:3] == '002':
				code_listS.append(stock)
			elif stock[0:3] == '200':
				code_listB.append(stock)
	except:
		fail_list.append(stock)
		pass
	i += 1
file_a = open(dirA+os.sep+today+'.txt', 'wb')
file_b = open(dirB+os.sep+today+'.txt', 'wb')
file_g = open(dirG+os.sep+today+'.txt', 'wb')
file_s = open(dirS+os.sep+today+'.txt', 'wb')	
file_list = [file_a, file_b, file_g, file_s]
i = 0
while i < 4:
	for stock in code_list[i]:
		file_list[i].write(stock+',')
	i += 1
while len(fail_list) > 0:
	for stock in fail_list:
		print stock
		fail_list.pop(stock)
		