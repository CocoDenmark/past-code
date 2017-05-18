#encoding=utf-8
import os
import time
import urllib
import datetime
dirA = 'G:\\filesys\\stock\\stock_list\\stock_a'
dirB = 'G:\\filesys\\stock\\stock_list\\stock_b'
dirG = 'G:\\filesys\\stock\\stock_list\\stock_growth'
dirS = 'G:\\filesys\\stock\\stock_list\\stock_small'
dir_list = [dirA, dirB, dirG, dirS]
today = datetime.datetime.now()
today = today.strftime('%Y-%m-%d')
baseUrl = 'http://hq.sinajs.cn/list=' 
code_listA = []
code_listB = []
code_listG = []
code_listS = []
a = ''
b = ''
g = ''
s = ''
fail_list = []
code_list = [code_listA, code_listB, code_listG, code_listS]

c = [a,b,g,s]
code = [[],[],[],[]]

a_c = 0
b_c = 0
s_c = 0
g_c = 0
i = 1
while i < 900999:
	stock = str(i).zfill(6)
	if stock[0] == '6' or stock[0] == '9':
		stock = 'sh' + stock
	else:
		stock = 'sz' + stock
	if stock[2:5] == '601' or stock[2:5] == '600':
		a = a + ',' + stock
		a_c += 1
		if a_c >= 100:
			code[0].append(a)
			a = ''
			a_c = 0
	elif stock[2:5] == '300':
		g = g + ',' + stock
		g_c += 1
		if g_c >= 100:
			code[2].append(g)
			g = ''
			g_c = 0
	elif stock[2:5] == '900':
		b = b + ',' + stock
		b_c += 1
		if b_c >= 100:
			code[1].append(b)
			b = ''
			b_c = 0
	elif stock[2:5] == '000':
		a = a + ',' + stock
		a_c += 1
		if a_c >= 100:
			code[0].append(a)
			a = ''
			a_c = 0
	elif stock[2:5] == '002':
		s = s + ',' + stock
		s_c += 1
		if s_c >= 100:
			code[3].append(s)
			s = ''
			s_c = 0
	elif stock[2:5] == '200':
		b = b + ',' + stock
		b_c += 1
		if b_c >= 100:
			code[1].append(b)
			b = ''
			b_c = 0
	i += 1
code[0].append(a)
code[1].append(b)
code[2].append(g)
code[3].append(s)

file_a = open(dirA+os.sep+today+'.txt', 'wb')
file_b = open(dirB+os.sep+today+'.txt', 'wb')
file_g = open(dirG+os.sep+today+'.txt', 'wb')
file_s = open(dirS+os.sep+today+'.txt', 'wb')	
file_list = [file_a, file_b, file_g, file_s]

i = 0
while i < 4:
	for stock in code[i]:
		urlItem = urllib.urlopen(baseUrl+stock[1:])
		print urlItem.info()
		j = 0
		for line in urlItem:
			print j,line
			j+=1
			d = line.split('"')
			if d[1] != '':
				file_list[i].write(d[0][11:19]+',')
				print d[0][11:19]
	i += 1
for f in file_list:
	f.close()