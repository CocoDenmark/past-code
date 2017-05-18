# -*- coding:utf-8 -*-
# This python script deals with the error file, in which the download-failed codes are recorded.
# 2015-07-24
# created by Yue Zhao at 3zcapital

# import package
import sys
import time
import os


namea = 'G:\\Filesys\\script\\daily_renew\\current_stock_sina'

nameb = sys.argv[1]
f_l = os.listdir(namea+os.sep+nameb)
for f_n in f_l:
        check=dict() 
        r_f = open(namea+os.sep+nameb+os.sep+f_n, 'rb')
        done = 0
        f=1
        while 1:
                info=range(500000)
                p=500000
                if done:
                        break
                for i in range(500000):
                        try:
                                line = r_f.readline()  #读第一行
                                if (line == '') or (line == '\n'):
                                        done = 1
                                        p=i
                                        break
                                code = line[13:19]   #    code:     300129
                                xx=line.find(',',24)
                                main=line[xx:-27]        #  main：  ,14.030,14.240,14.270,18000,14.280
                                time=line[-16:-7]    #     time：   ,14:39:57
                                info[i]=code+time+main       #     300129,14:39:57,14.030,14.240,14.270,18000,14.280
                                
                        except:
                                break
		print (nameb,f,i)
                for d in info[0:p]:
                        try:
                                code = d[0:6]
                                if code in check:
                                        if check[code]== d[7:15]:
                                                break
                                        else:
                                                check[code]=d[7:15]
                                else:
                                        check[code]=d[7:15]    
                                wf = open(namea+os.sep+code+'.txt','a')
                                wf.write(d[7:]+'\n')
                                wf.close()
                        except:
                                break
                f=f+1
        r_f.close()   #关文件


        
