#encoding=utf-8
from multiprocessing import Process
import os
import time
import urllib


def get_price(start, end):
	cf = open('stock_a.txt', 'rb')
	line = cf.readline().strip()
	code_list1 = line.split(',')
	code_list = []
	for c in code_list1:
		code = c[0:6]
		if code[0] == '6':
			code = 'sh' + code
		else:
			code = 'sz' + code
		code_list.append(code)
	baseUrl = 'http://hq.sinajs.cn/list=' 
	code_list_100=[]
	n=0
	loop=1
	while n<(len(code_list)):
		new_str=''
		while (n/50)<loop and n<(len(code_list)):
			new_str=new_str+','+code_list[n]
			n+=1
		loop+=1
		new_str = new_str[1:]
		code_list_100.append(new_str)
	code_sub = code_list[start:end]
	#print start, time.strftime('%H:%M:%S',time.localtime(time.time())) 
	#print code_sub
	i=0
	
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
				urlItem = urllib.urlopen(baseUrl+code)
				#print urlItem
				open('G:\\Filesys\\script\\daily_renew\\current_stock_sina\\20150624\\'+str(start/3)+'.txt', 'a').write(urlItem.read())
				#open('/Users/shuutae/Desktop/python_code/current_price/20150623/'+str(i)+code+'.txt', 'a').write(time.strftime('%H:%M:%S',time.localtime(time.time()))) 
			except:
				print 'error', start
				pass
		time.sleep(0.1)
		end_time = int(round(time.time() * 1000))
		ms = end_time - start_time
		print start, ms, start_time, end_time
if __name__ == '__main__':
	cf = open('stock_a.txt', 'rb')
	line = cf.readline().strip()
	code_list1 = line.split(',')
	code_list = []
	for c in code_list1:
		code = c[0:6]
		if code[0] == '6':
			code = 'sh' + code
		else:
			code = 'sz' + code
		code_list.append(code)
	baseUrl = 'http://hq.sinajs.cn/list=' 
	code_list_100=[]
	n=0
	loop=1
	while n<(len(code_list)):
		new_str=''
		while (n/80)<loop and n<(len(code_list)):
			new_str=new_str+','+code_list[n]
			n+=1
		loop+=1
		new_str = new_str[1:]
		code_list_100.append(new_str)	
	loop=len(code_list_100)
	k=3
	m=0
	l=[]
	j=0
	while m<(loop+k):
		j+=1
		p=Process(target=get_price,args=(m,m+k))
		m+=k
		l.append(p)
		l[-1].start()