# -*- coding:utf-8 -*-
import time

while 1:
	print '??'
	h = time.localtime().tm_hour
	m = time.localtime().tm_min
	if h >= 20 and m >=59:
		exit()
	