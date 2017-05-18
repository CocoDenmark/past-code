# -*- coding: utf-8 -*-
import datetime
import os
import sys
from datetime import datetime
from datetime import timedelta

get_data_dir = 'G:\\Filesys\\stock\\trade\\forward_Rehabilitation\\data\\daily\\current'
save_data_dir = 'G:\\Filesys\\stock\\makert_return'

date = sys.argv[1]
print date
file_read = open(get_data_dir+os.sep+date+'.txt', 'rb')
file_read.readline()
return_dict = dict()
i = 0
while 1:
	try:
		i = 1
		line = file_read.readline()
		line.strip()
		data = line.split('|')
		code = data[0]
		pre_close = float(data[2])
		close = float(data[6])
		maxupordown = int(data[19])
		trade_status = data[17]
		dd1 = '交易'
		if trade_status != dd1:
			print '!!!!!!'
			tr = 0
		else:
			tr = 1
		rc = close/pre_close - 1
		return_dict[code] = [rc, maxupordown, tr]
	except:
		break

file_read.close()

dir_a = 'G:\\Filesys\\stock\\stock_list\\stock_a'
dir_g = 'G:\\Filesys\\stock\\stock_list\\stock_growth'
dir_s = 'G:\\Filesys\\stock\\stock_list\\stock_small'

f_g = open(dir_g+os.sep+date+'.txt', 'rb')
line = f_g.readline()
line = line.strip()
g_list = line.split(',')
f_g.close()

f_a = open(dir_a+os.sep+date+'.txt', 'rb')
line = f_a.readline()
line = line.strip()
a_list = line.split(',')
f_a.close()

f_s = open(dir_s+os.sep+date+'.txt', 'rb')
line = f_s.readline()
line = line.strip()
s_list = line.split(',')
f_s.close()

sh_n = 0.0
sh_ave = 0.0
sz_n = 0.0
sz_ave = 0.0
for code in a_list[:-1]:
	code = code[2:]
	if code not in return_dict.keys():
		print code, date
		open(save_data_dir+os.sep+date+'.txt','a').write(code+',')
		continue
	if return_dict[code][2] == 0:
		continue
	if code[0] == '6':
		sh_ave = (sh_ave*sh_n+return_dict[code][0])/(sh_n+1)
		sh_n += 1
	else:
		sz_ave = (sz_ave*sz_n+return_dict[code][0])/(sz_n+1)
		sz_n += 1

open(save_data_dir+os.sep+'sh.csv','a').write(date+','+str(sh_ave)+','+str(sh_n)+'\n')
open(save_data_dir+os.sep+'sz_main.csv','a').write(date+','+str(sz_ave)+','+str(sz_n)+'\n')

g_n = 0.0
g_ave = 0.0
s_n = 0.0
s_ave = 0.0
for code in g_list[:-1]:
	code = code[2:]
	if code not in return_dict.keys():
		open(save_data_dir+os.sep+date+'.txt','a').write(code+',')
		print code, date
		continue
	if return_dict[code][2] == 0:
		continue
	g_ave = (g_ave*g_n+return_dict[code][0])/(g_n+1)
	g_n += 1
for code in s_list[:-1]:
	code = code[2:]
	if code not in return_dict.keys():
		open(save_data_dir+os.sep+date+'.txt','a').write(code+',')
		print code, date
		continue
	if return_dict[code][2] == 0:
		continue		
	s_ave = (s_ave*s_n+return_dict[code][0])/(s_n+1)
	s_n += 1
		

open(save_data_dir+os.sep+'sz_smail.csv','a').write(date+','+str(s_ave)+','+str(s_n)+'\n')
open(save_data_dir+os.sep+'sz_growth.csv','a').write(date+','+str(g_ave)+','+str(g_n)+'\n')
