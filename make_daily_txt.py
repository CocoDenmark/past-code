# -*- coding: UTF-8 -*- 

import os
get_data_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\history'
save_data_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\current'

f_l = os.listdir(get_data_dir)
absent_f = open(save_data_dir+os.sep+'last_date.csv', 'wb')
date_list = []
for f_n in f_l:
        code = f_n[6:12]
        f = open(get_data_dir+os.sep+f_n, 'rb')
        title = f.readline().strip()
        title = 'CODE|'+title
        while 1:
                try:
                        line = f.readline()
                        line = line.strip()
                        data = line.split('|')
                        if len(data) == 1:
                                break
                        date = data[0][0:10]
                        if data[1] == 'None' and data[2] == 'None':
                                continue
                        wf = open(save_data_dir+os.sep+date+'.txt', 'a')
                        if date not in date_list:
                                wf.write(title+'\n')
                                date_list.append(date)
                        new_line = code + '|' + line
                        wf.write(new_line+'\n')
                        wf.close()
                except:
                        break
        absent_f.write(code+','+date+'\n')
        print code
        f.close()
absent_f.close()

                                
