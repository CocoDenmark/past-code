# -*- coding: utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta

get_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily\\current'
save_data_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily_f'
'''
ff = open('G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily\\history1\\'+'last.txt','rb')
l = ff.readline()
ll = l.split(';')
sd = dict()
for lll in ll[:-1]:
	e = lll.split(',')
	sd[e[0]] = e[1]
ff.close()
#print sd'''
f_l = os.listdir(get_data_dir)
i = 0
f_l = ['2015-07-02.txt', '2015-07-03.txt']
for f_n in f_l:
	print f_n
	f = open(get_data_dir+os.sep+f_n,'rb')
	f.readline()
	while 1:
		try:	
			i += 1
			line1 = f.readline().strip()
			data =line1.split('|')
			if len(data) == 1:
				break
			code = data[0]
			if code[0] == '6':
				c = code + '.SH'
			else:
				c = code + '.SZ'
			newl = ''
			for da in data[1:]:	
				newl = newl +'|' + da
			open(save_data_dir+os.sep+'daily_'+c+'.txt','a').write(newl[1:]+'\n')
			
		except:
			break
	f.close()
	
