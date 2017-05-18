# -*- coding:utf-8 -*-
import datetime
import os
import sys
#from datetime import datetime
#from datetime import timedelta
import time


import smtplib  
from email.MIMEText import MIMEText  
from email.Utils import formatdate  
from email.Header import Header 

tod = datetime.datetime.now()
aDay = datetime.timedelta(days=1)
tod = tod - aDay - aDay
dateee = tod.strftime('%Y-%m-%d')
date_list = [dateee]
type_list = ['down', 'up']
count_list = [1,2,3]
premium_list = [0.990, 0.995, 1.00, 1.005, 1.01, 1.015, 1.02, 1.04, 1.06, 1.08, 1.1, 1.11]

body = ''

for type in type_list:
	for count in count_list:
		body = body + '\r\n\r\n'+type + ' - ' + str(count) + ' --------------'+'--------------\r\n'	
		for premium in premium_list:
			premium_dir = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\'+type+'_'+str(count)+os.sep+str(premium)
			try:
				os.mkdir(premium_dir)
			except:
				pass
			for date in date_list:
				get_price_dir = 'G:\\Filesys\\stock\\trade\\Backward_Rehabilitation\\data\\daily\\current'
				get_stock_dir = 'G:\\Filesys\\script\\daily_renew\\j\\down_up\\'+type+'_'+str(count)

				day = date.split('-')
				today = datetime.date(int(day[0]),int(day[1]),int(day[2]))

				stock_dict = dict()
				stock_f = open(get_stock_dir+os.sep+date+'.txt', 'rb')
				stock_f.readline()
				s_stock = 0
				while 1:
					try:
						line = stock_f.readline()
						line = line.strip()
						data = line.split(',')
						if len(data) == 1:
							break
						code = data[0]
						days = 0
						pre_close = 0
						close = 0
						high = 0
						low = 0
						r = 0
						sell = 0
						stock_dict[code] = [days, pre_close, close, high, low, r, sell]
						s_stock += 1
					except:
						break
				stock_f.close()
				print 'get stock, date:', date, s_stock

				flag = 0
				s_f_stock = 0
				try:
					date_t = today.strftime('%Y-%m-%d')
					stock_f = open(premium_dir+os.sep+date_t+'_'+str(premium)+'_fail.csv', 'rb')
					flag = 1
				except:
					pass

				if flag == 1:
					while 1:
						try:
							line = stock_f.readline()
							line = line.strip()
							data = line.split(',')
							if len(data) == 1:
								break
							code = data[0]
							days = int(data[1]) + 1
							s_f_stock += 1
							if code in stock_dict.keys():
								stock_dict[code][0] = days
							else:
								stock_dict[code] = [days,0,0,0,0,0,0]
						except:
							break

					stock_f.close()
				print 'get stock failed to sell at:', date_t, s_f_stock
				tomorrow = today + aDay
				t = tomorrow
				i = 0
				while 1:
					i += 1
					if i > 5:
						print 'no corresponding file!'
					try:
						date_t = t.strftime('%Y-%m-%d')
						price_f = open(get_price_dir+os.sep+date_t+'.txt', 'rb')
						break
					except:
						t = t + aDay
						continue
				tomorrow_t = date_t
				price_dict = dict()

				all_stock = 0
				price_f.readline()
				while 1:
					try:
						line = price_f.readline()
						line = line.strip()
						data = line.split('|')
						if len(data) == 1:
							break
						code = data[0]
						#print code
						if code not in stock_dict.keys():
							continue
						else:
							pre_close = float(data[2])
							high = float(data[4])
							low = float(data[5])
							close = float(data[6])
							if high >= pre_close*premium:
								r = float(premium - 1)
								sell = 1
							else:
								r = float((close-pre_close)/pre_close)
								sell = 0
							stock_dict[code][1] = pre_close
							stock_dict[code][2] = close
							stock_dict[code][3] = high
							stock_dict[code][4] = low
							stock_dict[code][5] = r
							#print code, r
							stock_dict[code][6] = sell
							all_stock += 1		
					except:
						break
				print 'get price at:', tomorrow_t, all_stock
				price_f.close()
				position_f = open(premium_dir+os.sep+date+'_'+str(premium)+'_position.csv', 'wb')
				summary_f = open(premium_dir+os.sep+tomorrow_t+'_'+str(premium)+'_summary.csv', 'wb')
				fail_f = open(premium_dir+os.sep+tomorrow_t+'_'+str(premium)+'_fail.csv', 'wb')
				ave_r_0 = 0.0
				ave_r_sell = 0.0
				no_r_sell = 0
				no_r_0 = 0
				ave_r_1 = 0.0
				no_r_1 = 0
				fail_count = 0
				for code in stock_dict.keys():
					days = stock_dict[code][0]
					if days == 0:
						ave_r_0 = (ave_r_0*no_r_0+stock_dict[code][5])/(no_r_0+1)
						no_r_0 += 1
						if stock_dict[code][6] == 1:
							ave_r_sell = (ave_r_sell*no_r_sell+stock_dict[code][5])/(no_r_sell+1)
							no_r_sell += 1
					else:
						ave_r_1 = (ave_r_1*no_r_1+stock_dict[code][5])/(no_r_1+1)
						no_r_1 += 1
					position_f.write(code+','+str(stock_dict[code][0])+','+str(stock_dict[code][1])+'\r\n')
					summary_f.write(code+','+str(stock_dict[code][0])+','+str(stock_dict[code][1])+','+str(stock_dict[code][2])+','+str(stock_dict[code][3])+','+str(stock_dict[code][4])+','+str(stock_dict[code][5])+','+str(stock_dict[code][6])+'\r\n')
					if stock_dict[code][6] == 0:
						fail_f.write(code+','+str(stock_dict[code][0])+','+str(stock_dict[code][5])+'\r\n')
						fail_count += 1
				print tomorrow_t, ave_r_0, no_r_0, ave_r_sell, no_r_sell
				print tomorrow_t, ave_r_1, no_r_1
				print 'fail:', fail_count
				position_f.close()
				summary_f.close()
				fail_f.close()

				premium_summary_f = open(premium_dir+os.sep+str(premium)+'_summary.csv', 'a')
				premium_summary_f.write(tomorrow_t+','+str(no_r_0)+','+str(ave_r_0)+','+str(no_r_sell)+','+str(ave_r_sell)+','+str(no_r_1)+','+str(ave_r_1)+'\r\n')
				premium_summary_f.close()
	
				date_summary_f = open(get_stock_dir+os.sep+tomorrow_t+'_summary.csv', 'a')
				date_summary_f.write(str(premium)+','+str(no_r_0)+','+str(ave_r_0)+','+str(no_r_sell)+','+str(ave_r_sell)+','+str(no_r_1)+','+str(ave_r_1)+'\r\n')
				date_summary_f.close()
				body = body + 'Premium='+str(premium).ljust(5)+'   Total: '+str(no_r_0).ljust(5)+'   Return: '+(str(ave_r_0*100)[:9]+'%').ljust(12)+'   Succeed: '+str(no_r_sell).ljust(5)+ '\r\n'


# here begins to send the reporting email 
smtpHost = 'smtp.ym.163.com'  
smtpPort = '25'  
sslPort  = '465'  
fromMail = 'miao.zhou@3zcapital.com'  
toMail   = ['miao.zhou@3zcapital.com', 'jery.xuan@3zcapital.com']
#toMail = ['miao.zhou@3zcapital.com']
username = 'miao.zhou@3zcapital.com'  
password = '19920229'  
 

   
# set the essential info. of the email
encoding = 'utf-8' 
subject = '[XYZ - Daily Report]  ' + (tod+aDay).strftime('%Y-%m-%d')

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



