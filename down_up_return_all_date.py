# -*- coding:utf-8 -*-
import datetime
import os
import sys
#from datetime import datetime
#from datetime import timedelta

aDay = datetime.timedelta(days=1)

date_list = ['2015-05-27','2015-05-28','2015-05-29','2015-06-01','2015-06-02','2015-06-03','2015-06-04','2015-06-05','2015-06-08','2015-06-09','2015-06-10','2015-06-11','2015-06-12','2015-06-15','2015-06-16','2015-06-17','2015-06-18','2015-06-19','2015-06-23','2015-06-24','2015-06-25']
type_list = ['down', 'up']
count_list = [1,2,3]
premium_list = [0.96, 0.97, 0.98, 0.99, 0.995, 1, 1.005, 1.01, 1.015, 1.02, 1.04, 1.06, 1.08, 1.1, 1.11]


for premium in premium_list:
	for type in type_list:
		for count in count_list:
			save_premium_dir = 'G:\\Filesys\\script\\down_up\\strategy_summary\\'+type+'_'+str(count)+os.sep+str(premium)
			save_type_dir = 'G:\\Filesys\\script\\down_up\\strategy_summary\\'+ type+'_'+str(count)
			try:
				os.mkdir(save_type_dir)
			except:
				pass
			try:
				os.mkdir(save_premium_dir)
			except:
				pass
			for date in date_list[count:-1]:
				get_price_dir = 'G:\\Filesys\\stock\\trade\\Backward_Rehabilitation\\data\\daily\\current'
				get_price_dir_open_position = 'G:\\Filesys\\stock\\trade\\no_Rehabilitation\\data\\daily\\current'
				get_stock_dir = 'G:\\Filesys\\script\\down_up\\'+type+'_'+str(count)

				day = date.split('-')
				today = datetime.date(int(day[0]),int(day[1]),int(day[2]))
				today_str = date

				tomorrow = today + aDay
				t = tomorrow
				i = 0
				flag = 0
				while 1:
					i += 1
					if i > 5:
						print 'no corresponding file!'
					try:
						date_t = t.strftime('%Y-%m-%d')
						price_tomorrow_f = open(get_price_dir+os.sep+date_t+'.txt', 'rb')
						flag = 1
						break
					except:
						t = t + aDay
						continue
				tomorrow = t
				tomorrow_str = date_t
				print tomorrow_str,today_str,type,count
				buy_list = []
				buy_list_f = open(get_stock_dir+os.sep+today_str+'.txt', 'rb')
				buy_price_f = open(get_price_dir_open_position+os.sep+today_str+'.txt', 'rb')
				buy_price = dict()
				buy_price_f.readline()
				while 1:
					try:
						line = buy_price_f.readline()
						line = line.strip()
						data = line.split('|')
						if len(data) == 1:
							break
						code = data[0]
						price = data[6]
						buy_price[code] = price
					except:
						break
				buy_price_f.close()
				print len(buy_price.keys())
				open_position_today_f = open(save_premium_dir+os.sep+'open_position_'+today_str+'_'+str(premium)+'.csv', 'wb')
				open_position_today_f.write('order,stock,cost\n')
				i = 0
				while 1:
					try:
						line = buy_list_f.readline()
						line = line.strip()
						data = line.split(',')
						if len(data) == 1:
							break
						code = data[0]
						cost = buy_price[code]
						i += 1
						open_position_today_f.write(str(i)+','+code+','+cost+'\n')
						buy_list.append(code)
					except:
						break
				open_position_today_f.write('total,'+str(i)+'\n')
				buy_list_f.close()
				open_position_today_f.close()

				if flag == 1:
					ave_r = 0.0
					ave_f_r = 0.0
					total_f = 0
					total = 0
					total_sell = 0
					close_position_tomorrow_f = open(save_premium_dir+os.sep+'close_position_'+tomorrow_str+'_'+str(premium)+'.csv', 'wb')
					close_position_tomorrow_f.write('order,code,pre_close,close,high,low,r,sell_flag\n')
					price_tomorrow_f.readline()
					while 1:
						try:
							line = price_tomorrow_f.readline()
							line = line.strip()
							data = line.split('|')
							if len(data) == 1:
								break
							code = data[0]
							if code not in buy_list:
								continue
							else:
								index = buy_list.index(code) + 1
								pre_close = float(data[2])
								high = float(data[4])
								low = float(data[5])
								close = float(data[6])
								if high >= pre_close*premium:
									r = float(premium - 1)
									sell = 1
									total_sell += 1
								else:
									r = float((close-pre_close)/pre_close)
									ave_f_r = (ave_f_r*total_f+r)/(total_f+1)
									total_f += 1
									sell = 0
							#print code, r
								ave_r = (ave_r*total+r)/(total+1)
								total += 1
								close_position_tomorrow_f.write(str(index)+','+code+','+str(pre_close)+','+str(close)+','+str(high)+','+str(low)+','+str(r*100)+'%,'+str(sell)+'\n')
						except:
							break
					close_position_tomorrow_f.close()
					if total == 0:
						continue
					sum_pre_type_count_f = open(save_premium_dir+os.sep+str(premium)+'_summary.csv', 'a')
					sum_pre_type_count_f.write(tomorrow_str+','+str(ave_r*100)+'%,'+str(total)+','+str(total_sell)+','+str(total_sell/total*100)+'%,'+str(ave_f_r*100)+'%\n')
					sum_pre_type_count_f.close()
					sum_date_f = open(save_type_dir+os.sep+tomorrow_str+'_summary.csv', 'a')
					sum_date_f.write(type+','+str(count)+','+str(premium)+','+str(ave_r*100)+'%,'+str(total)+','+str(total_sell)+','+str(total_sell/total*100)+'%,'+str(ave_f_r*100)+'%\n')
					sum_date_f.close()