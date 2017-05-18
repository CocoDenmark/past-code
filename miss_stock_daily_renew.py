# -*- coding:utf-8 -*-
# This python script download data automatically from wind Python API and report via emails.
# 2015-05-27
# created by Miao Zhou at 3zcapital

# import package
import sys
from WindPy import w
import time
from datetime import datetime
from datetime import timedelta
import os
import smtplib  
from email.MIMEText import MIMEText  
from email.Utils import formatdate  
from email.Header import Header  

# reload the system to encode by utf-8 dealling with Chinese characters
reload(sys)
sys.setdefaultencoding('utf8')

# the first time stamp to mark the start time
time1 = time.time()
start_time = str(time.asctime(time.localtime(time.time())))

# read all the stock code from stock_a.txt, which is also from wind
code_file = open('stock_a.txt', 'rb')
line = code_file.readline()
line = line.strip()
code_list = line.split(',')
#print code_list, len(code_list)
print 'total:', len(code_list)

# start wind
w.start(waitTime=60)
tomorrow = datetime.now()
aDay = timedelta(days=1)
tod = tomorrow - aDay
today = tod.strftime('%Y-%m-%d')
#print today
#today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
body = ''

# here begins the trade data (without rehabilitation) download process by setting the destinate dir
base_dir = 'G:\\Filesys\\stock\\trade\\No_Rehabilitation\\data\\daily\\current\\'
error_file = open('G:\\Filesys\\stock\\trade\\No_Rehabilitation\\error_file\\fail_daily_renew_'+today+'.txt','wb')

renew_dict = list()
fail_list = list()
sum = 0

# here starts to download data and write txt file for each stock
for code in code_list:

	d = w.wsd(code, "pre_close,open,high,low,close,volume,amt,dealnum,chg,pct_chg,swing,vwap,adjfactor,close2,close3,turn,free_turn,last_trade_day,rel_ipo_chg,rel_ipo_pct_chg,maxupordown,trade_status,susp_reason", today, today, "Fill=Previous", "showblank=-1")
	
# this is what happen when something wrong with the network connection
	if d.ErrorCode != 0:
		print 'error at ', code
		error_file.write(code+'|')
		fail_list.append(code)
		time.sleep(2)
		continue

# here begins to write the downloaded data into txt files
	length = len(d.Fields)
	renew_line = code[0:6]+'|'

	i = 0
	for date in d.Times:
		renew_line = renew_line + str(date)+'|'
	
		j = 0
		while j<length:
			try:
				 d.Data[j][i] = d.Data[j][i].encode('utf-8')
			except:
				None
			renew_line = renew_line + str(d.Data[j][i])
			if j < (length-1):
				renew_line = renew_line + '|'
			j += 1
		i += 1
	renew_dict.append(renew_line)
	print 'trade: ', code
	sum += 1	
error_file.close()

renew_file = open(base_dir + today + '.txt', 'wb')
title = 'CODE|DATE'
for f in d.Fields:
	title = title + '|' + f
renew_file.write(title+'\r\n')
for c in renew_dict:
	renew_file.write(c+'\r\n')
renew_file.close()
body = body + '-----STOCK-TRADE-DAILY-----\r\n' + 'Total: ' + str(len(code_list)) + '\r\n' + 'Succeeded: ' + str(sum) + '\r\n' + 'Failed: ' + str(len(fail_list)) + '\r\n' + '\r\n'

# here begins the trade data (forward rehabilitation) download process by setting the destinate dir
base_dir = 'G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\data\\daily\\current\\'
error_file = open('G:\\Filesys\\stock\\trade\\Forward_Rehabilitation\\error_file\\fail_daily_renew_'+today+'.txt','wb')


fail_list = list()
renew_dict = list()
sum = 0

# here starts to download data and write txt file for each stock
for code in code_list:

	d = w.wsd(code, "pre_close,open,high,low,close,volume,amt,dealnum,chg,pct_chg,swing,vwap,adjfactor,turn,free_turn,trade_status,susp_reason,maxupordown", today, today, "Fill=Previous;PriceAdj=F", "showblank=-1")
	
# this is what happen when something wrong with the network connection
	if d.ErrorCode != 0:
		print 'error at ', code
		error_file.write(code+'|')
		fail_list.append(code)
		time.sleep(2)
		continue

# here begins to write the downloaded data into txt files
	length = len(d.Fields)
	renew_line = code[0:6]+'|'

	i = 0
	for date in d.Times:
		renew_line = renew_line + str(date)+'|'
	
		j = 0
		while j<length:
			try:
				 d.Data[j][i] = d.Data[j][i].encode('utf-8')
			except:
				None
			renew_line = renew_line + str(d.Data[j][i])
			if j < (length-1):
				renew_line = renew_line + '|'
			j += 1
		i += 1
	renew_dict.append(renew_line)
	print 'trade_f: ', code
	sum += 1	
error_file.close()

renew_file = open(base_dir + today + '.txt', 'wb')
title = 'CODE|DATE'
for f in d.Fields:
	title = title + '|' + f
renew_file.write(title+'\r\n')
for c in renew_dict:
	renew_file.write(c+'\r\n')
renew_file.close()
error_file.close()
body = body + '-----STOCK-TRADE-DAILY--Forward Rehabilitation-----\r\n' + 'Total: ' + str(len(code_list)) + '\r\n' + 'Succeeded: ' + str(sum) + '\r\n' + 'Failed: ' + str(len(fail_list)) + '\r\n' + '\r\n'


# here begins the trade data (backward rehabilitation) download process by setting the destinate dir
base_dir = 'G:\\Filesys\\stock\\trade\\Backward_Rehabilitation\\data\\daily\\current\\'
error_file = open('G:\\Filesys\\stock\\trade\\Backward_Rehabilitation\\error_file\\fail_daily_renew_'+today+'.txt','wb')


fail_list = list()
renew_dict = list()
sum = 0

# here starts to download data and write txt file for each stock
for code in code_list:

	d = w.wsd(code, "pre_close,open,high,low,close,volume,amt,dealnum,chg,pct_chg,swing,vwap,adjfactor,turn,free_turn,trade_status,susp_reason,maxupordown", today, today, "Fill=Previous;PriceAdj=B", "showblank=-1")
	
# this is what happen when something wrong with the network connection
	if d.ErrorCode != 0:
		print 'error at ', code
		error_file.write(code+'|')
		fail_list.append(code)
		time.sleep(2)
		continue

# here begins to write the downloaded data into txt files
	length = len(d.Fields)
	renew_line = code[0:6]+'|'

	i = 0
	for date in d.Times:
		renew_line = renew_line + str(date)+'|'
	
		j = 0
		while j<length:
			try:
				 d.Data[j][i] = d.Data[j][i].encode('utf-8')
			except:
				None
			renew_line = renew_line + str(d.Data[j][i])
			if j < (length-1):
				renew_line = renew_line + '|'
			j += 1
		i += 1
	renew_dict.append(renew_line)
	print 'trade_b: ', code
	sum += 1	
error_file.close()

renew_file = open(base_dir + today + '.txt', 'wb')
title = 'CODE|DATE'
for f in d.Fields:
	title = title + '|' + f
renew_file.write(title+'\r\n')
for c in renew_dict:
	renew_file.write(c+'\r\n')
renew_file.close()
body = body + '-----STOCK-TRADE-DAILY--Backward Rehabilitation-----\r\n' + 'Total: ' + str(len(code_list)) + '\r\n' + 'Succeeded: ' + str(sum) + '\r\n' + 'Failed: ' + str(len(fail_list)) + '\r\n' + '\r\n'


# the download and write-into-file process for stock-hold data

base_dir = 'G:\\Filesys\\stock\\hold\\data\\daily\\current\\'
error_file = open('G:\\Filesys\\stock\\hold\\error_file\\fail_daily_renew_'+today+'.txt','wb')

fail_list = list()
renew_dict = list()
sum = 0
for code in code_list:
	wind_data = list()
	d = w.wsd(code, "total_shares,free_float_shares,float_a_shares,share_restricteda,share_totala,share_restrictedb,share_totalb,share_h,share_oversea,share_totaltradable,share_totalrestricted,share_nontradable,share_ntrd_prfshare,share_rtd_state,share_rtd_statejur,share_rtd_subotherdomes,share_rtd_domesjur,share_rtd_inst,share_rtd_domesnp,share_rtd_subfrgn,share_rtd_frgnjur,share_rtd_frgnnp,holder_top10pct,holder_top10quantity,holder_top10liqquantity,holder_controller,holder_name", today, today, "order=0;Fill=Previous", "showblank=-1")
	wind_data.append(d)
	d = w.wsd(code, "holder_quantity,holder_pct,holder_sharecategory", today, today, "order=1;Fill=Previous")
	wind_data.append(d)
	d = w.wsd(code, "holder_liqname", today, today, "order=0;Fill=Previous")
	wind_data.append(d)
	d = w.wsd(code, "holder_liqquantity,holder_liqsharecategory,holder_num,holder_avgnum,holder_avgpct,holder_havgpctchange,holder_qavgpctchange,holder_havgchange,holder_qavgchange,holder_avgpctchange", today, today, "order=1;shareType=1;Fill=Previous")
	wind_data.append(d)


	if d.ErrorCode != 0:
		print 'error at ', code, d.ErrorCode
		error_file.write(code+'|')
		time.sleep(2)
		fail_list.append(code)


	renew_line = code[0:6] + '|'
	i = 0


	for date in wind_data[1].Times:
		renew_line = renew_line + str(date) + '|'
		j = 0
		k = 1
		for d in wind_data:
			length = len(d.Fields)
			j = 0
			while j < length:
				try:
					d.Data[j][i] = str(d.Data[j][i])
					d.Data[j][i] = d.Data[j][i].encode('utf-8')
				except:
					None
				renew_line = renew_line + d.Data[j][i]
				if k < 4:
					renew_line = renew_line + '|'
				if k == 4:
					if j < (length-1):
						renew_line = renew_line + '|'
				j += 1
			k += 1
		i += 1
	
	print 'hold: ', code
	sum += 1
	renew_dict.append(renew_line)
error_file.close()

renew_file = open(base_dir + today + '.txt', 'wb')
title = 'CODE|DATE'
for dd in wind_data:
	for f in dd.Fields:
		title = title + '|' + f
renew_file.write(title+'\r\n')
for c in renew_dict:
	renew_file.write(c+'\r\n')
renew_file.close()


body = body + '-----STOCK-HOLD-DAILY-----\r\n' + 'Total: ' + str(len(code_list)) + '\r\n' + 'Succeeded: ' + str(sum) + '\r\n' + 'Failed: ' + str(len(fail_list)) + '\r\n' + '\r\n'


# the second time stamp 
time2 = time.time()

# here begins to send the reporting email 
smtpHost = 'smtp.ym.163.com'  
smtpPort = '25'  
sslPort  = '465'  
fromMail = 'miao.zhou@3zcapital.com'  
toMail   = ['muchen.li@3zcapital.com', 'miao.zhou@3zcapital.com', 'meng.ma@3zcapital.com', 'qiang.zhang@3zcapital.com', 'chunxiang.su@3zcapital.com', 'junwei.yang@3zcapital.com']
#toMail = ['miao.zhou@3zcapital.com']
username = 'miao.zhou@3zcapital.com'  
password = '19920229'  
 

   
# set the essential info. of the email
encoding = 'utf-8' 
today = time.strftime('%Y-%m-%d', time.localtime(time.time())) 
subject = '[DATABASE DAILY RENEW - stock]  ' + today
body = body + 'Time Started : ' + start_time + '\r\n' 
body = body + 'Run Time: ' + str(time2-time1) + ' seconds'
print subject
print body

# initialize the email object  
 
mail = MIMEText(body,'plain',encoding)  
mail['Subject'] = Header(subject,encoding)  

mail['From'] = fromMail   
mail['Date'] = formatdate()  
   
try:  
    # here use the ordinary way to connet to the SMTP server with encryption
    smtp = smtplib.SMTP(smtpHost,smtpPort)
    smtp.ehlo()  
    smtp.login(username,password)  
   
    # alternative tls encryption  
    #smtp = smtplib.SMTP(smtpHost,smtpPort)  
    #smtp.ehlo()  
    #smtp.starttls()  
    #smtp.ehlo()  
    #smtp.login(username,password)  
   
    # alternative ssl encryption  
    #smtp = smtplib.SMTP_SSL(smtpHost,sslPort)  
    #smtp.ehlo()  
    #smtp.login(username,password)  
   
    # email sending
    for tm in toMail: 
        mail['To'] = tm 
        smtp.sendmail(fromMail,tm,mail.as_string())  
    smtp.close()  
    print 'OK'  
except Exception:  
    print 'Error: unable to send email'





