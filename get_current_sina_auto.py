#encoding=utf-8
from multiprocessing import Process
import os
import time
import urllib
import datetime

des_dir = 'G:\\Filesys\\stock\\raw_data\\sina_level1\\'
today = datetime.datetime.now()
today = today.strftime('%Y%m%d')
print today
new_dir = des_dir+today
try:
	os.mkdir(new_dir)
except:
	pass

		
today2 = datetime.datetime.now().strftime('%Y-%m-%d')



def get_price(start, end):
	h = time.localtime().tm_hour
	m = time.localtime().tm_min
	cf = open('G:\\Filesys\\stock_set\\'+today2+'.txt', 'rb')
	line = cf.readline().strip()
	code_list1 = line.split(',')
	code_list = []
	for c in code_list1[:-1]:
		code = c[0:6]
		if code[0] == '6':
			code = 'sh' + code
		else:
			code = 'sz' + code
		code_list.append(code)
	code_list = code_list[:50]
	baseUrl = 'http://hq.sinajs.cn/list=' 
	code_list_100=[]
	n=0
	loop=1
	while n<(len(code_list)):
		new_str=''
		while (n/4)<loop and n<(len(code_list)):
			new_str=new_str+','+code_list[n]
			n+=1
		loop+=1
		new_str = new_str[1:]
		code_list_100.append(new_str)
	code_sub = code_list_100[start:end]
	#print start, time.strftime('%H:%M:%S',time.localtime(time.time())) 
	#print code_sub
	i=0
	#while h<15 or (h==15 and m <=5):
	while 1:
		start_time = int(round(time.time() * 1000))
		i+=1
		#i=start+1
		#print start, time.strftime('%H:%M:%S',time.localtime(time.time())) 
		if end < len(code_list_100):
			code_sub = code_list_100[start:end]
		else:
			code_sub = code_list_100[start:]
		for code in code_sub:
			try:
				print code
				urlItem = urllib.urlopen(baseUrl+code)
				open(new_dir+os.sep+str(start/5)+'.txt', 'a').write(urlItem.read())

			except:
				print 'error', start
				pass
		time.sleep(0.1)
		end_time = int(round(time.time() * 1000))
		ms = end_time - start_time
		print start, ms, start_time, end_time
		h = time.localtime().tm_hour
		m = time.localtime().tm_min

if __name__ == '__main__':
	cf = open('G:\\Filesys\\stock_set\\'+today2+'.txt', 'rb')
	line = cf.readline().strip()
	code_list1 = line.split(',')
	code_list = []
	
	for c in code_list1[:-1]:
		code = c[0:6]
		if code[0] == '6':
			code = 'sh' + code
		else:
			code = 'sz' + code
		code_list.append(code)
	baseUrl = 'http://hq.sinajs.cn/list=' 
	code_list_100=[]
	code_list = code_list[:50]
	n=0
	loop=1
	while n<(len(code_list)):
		new_str=''
		while (n/4)<loop and n<(len(code_list)):
			new_str=new_str+','+code_list[n]
			n+=1
		loop+=1
		new_str = new_str[1:]
		code_list_100.append(new_str)	
	loop=len(code_list_100)
	k=5
	m=0
	l=[]
	j=0
	while m<(loop+k):
		j+=1
		p=Process(target=get_price,args=(m,m+k))
		m+=k
		l.append(p)
		l[-1].start()
