# -*- coding:utf-8 -*-
# This python script deals with the error file, in which the download-failed codes are recorded.
# 2015-07-24
# created by Yue Zhao at 3zcapital

# import package
import sys
import time
import os
from multiprocessing import Process


def data_read(namea,nameb):
        check=dict() 
        r_f = open(namea+os.sep+nameb, 'rb')
        done = 0
        f=1
        while 1:
                info=range(100000)
                p=100000
                if done:
                        break
                i=0
                while i <100000:
                        try:
                                line = r_f.readline()  #读第一行
                                if (line == '') or (line == '\n'):
                                        done = 1
                                        p=i
                                        break
                                code = line[13:19]   #    code:     300129
                                time=line[-16:-7]    #     time：   ,14:39:57
                                if (int(time[1:3])==15):
                                        if(int(a[4:6])==6):
                                                done = 1
                                                p=i
                                                break
                                if code in check:
                                        if check[code] == time:
                                                continue
                                        else:
                                                check[code] = time
                                else:
                                        check[code] = time
                                xx=line.find(',',24)
                                main=line[xx:-27]        #  main：  ,14.030,14.240,14.270,18000,14.280
                                info[i]=code+time+main       #     300129,14:39:57,14.030,14.240,14.270,18000,14.280
                        except:
                                break
                        i=i+1
		print (nameb,f,i)
                for d in info[0:p]:
                        try:
                                code = d[0:6]
                                wf = open(namea+os.sep+code+'.txt','a')
                                wf.write(d[7:]+'\n')
                                wf.close()
                        except:
                                wf.close()
                                break
                f=f+1
        r_f.close()   #关文件

filename='G:\\data_backup\\s'
date=os.listdir(filename)
for datei in date:
        num = os.listdir(filename+'\\'+datei)
        for num_i in num:
                data_read(filename+'\\'+datei,num_i)
        
