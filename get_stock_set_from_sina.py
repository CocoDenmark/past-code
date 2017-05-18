#encoding=utf-8
import os
import time
import urllib
import datetime

dir1 = 'G:\\Filesys\\stock_set'
today = datetime.datetime.now()
today = today.strftime('%Y-%m-%d')
baseUrl = 'http://hq.sinajs.cn/list=' 
i=0
code_list = []
while i < 14:
	code_list.append('')
	i += 1


fail_list = []
time1 = time.time()

i = 1
p = 0


tail = range(500)
for t in tail:
	code_list[0] = code_list[0] + ',' + 'sz000' + str(t).zfill(3)
	code_list[1] = code_list[1] + ',' + 'sz002' + str(t).zfill(3)
	code_list[2] = code_list[2] + ',' + 'sz300' + str(t).zfill(3)
	code_list[3] = code_list[3] + ',' + 'sh600' + str(t).zfill(3)
	code_list[4] = code_list[4] + ',' + 'sh601' + str(t).zfill(3)
	code_list[5] = code_list[5] + ',' + 'sh603' + str(t).zfill(3)
	code_list[12] = code_list[12] + ',' + 'sz001' + str(t).zfill(3)
tail = range(500,1000)
for t in tail:
	code_list[6] = code_list[6] + ',' + 'sz000' + str(t).zfill(3)
	code_list[7] = code_list[7] + ',' + 'sz002' + str(t).zfill(3)
	code_list[8] = code_list[8] + ',' + 'sz300' + str(t).zfill(3)
	code_list[9] = code_list[9] + ',' + 'sh600' + str(t).zfill(3)
	code_list[10] = code_list[10] + ',' + 'sh601' + str(t).zfill(3)
	code_list[11] = code_list[11] + ',' + 'sh603' + str(t).zfill(3)
	code_list[13] = code_list[13] + ',' + 'sz001' + str(t).zfill(3)

f = open(dir1+os.sep+today+'.txt', 'wb')

i = 0
count = 0
for line in code_list:
	while 1:
		try:
			urlItem = urllib.urlopen(baseUrl+line[1:])
			print urlItem.info()
			break
		except:
			continue
	for line in urlItem:
		print line
		d = line.split('"')
		if d[1] != '':
			f.write(d[0][13:19]+',')
			print d[0][13:19]
			count += 1
f.close()

print count
time2 = time.time()
print str(time2-time1)