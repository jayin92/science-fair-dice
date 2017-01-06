#import所需函式庫
import math
import sys
import os
from termcolor import colored, cprint
import xlsxwriter
mode = input("請選擇面數或顆數 面數選1 顆數選2 >")
if mode == "1":
	num = int(input("請輸入想要測試之面數的最大值 >"))
	m = int(input("請輸入想要測試之顆數 > "))	
	n = m
	workbook = xlsxwriter.Workbook('result(face).xlsx')
	worksheet = workbook.add_worksheet()
	for p in range(1,num+1):
		for q in range(1,num+1):	
		
			#不進位直式的函式	
			def muti(q,k):
				#q為陣列 k為整數
				result_len = len(q) + (len(str(k))-1)#計算對齊後的長度	
				result_list = []#定義回傳陣列
				for j in range(result_len):#將回傳陣列的每個元素都設為0 且0的數量為對齊後的長度
					result_list.append(0)
				for i in range(len(str(k))):#整數必須轉成string才能判斷其長度
					temp_q = list(q) #若直接將一個陣列賦值給另一個陣列 將會出現問題 故必須使用list()函數		 
					#將兩個陣列對齊 (24~28)
					for h in range(i):
						temp_q.append('0')				
					for l in range(result_len - len(temp_q)):
						temp_q.insert(0,'0')
					#將元素相加		
					for h in range(result_len):		
						result_list[h] = int(temp_q[h]) + result_list[h]
				#回傳結果
				return result_list
			#次方運算(不進位)
			def power(p,m):
				p_math = 0
				temp = 0
				#利用骰子面數創造111...111(1的個數為骰子面數)
				for i in range(p):		
					p_math = p_math*10 + 1
				temp = list(str(p_math))#將111...111轉成陣列
				#重複呼叫muti以算出結果 (指數)
				for k in range(1,m):
					temp = muti(temp,p_math)
				return temp #return 結果
				
				
			#定義變數	
			pm = m*p
			qn = n*q
			m_result = []
			n_result = []
			m_result_print_color = []
			n_result_print_color = []
			m_result_print = []
			n_result_print = []
			#輸入參數 並透過power與muti函式 return值為陣列
			for i in power(p,m):
				m_result_print_color.append(str(i)+colored('  X'+str(pm),'red')+', ')#可視化陣列
				m_result_print.append(str(i)+'  X'+str(pm))
				m_result.append(int(i))#判斷贏 平手 輸之陣列	
				pm = pm-1
				
			for k in power(q,n):
				n_result_print_color.append(str(k)+colored('  X'+str(qn),'red')+', ')#可視化陣列
				n_result_print.append(str(k)+'  X'+str(qn))
				n_result.append(int(k))#判斷贏 平手 輸之陣列
				qn = qn-1

			#將陣列對齊
			if p*m > q*n:
				math_len = p*m - n + 1	
				for i in range(math_len-len(m_result)):
					m_result.append(0)		
				for k in range(math_len-len(n_result)):
					n_result.insert(0, 0)
			if p*m < q*n:
				math_len = q*n - m + 1
				for i in range(math_len-len(n_result)):
					n_result.append(0)
				for k in range(math_len-len(m_result)):
					m_result.insert(0, 0)


			#將陣列元素翻轉以方便判斷
			m_result = m_result[::-1]
			n_result = n_result[::-1]
			#定義各個變數
			win_total = 0
			win_times = 0
			even_times = 0
			lose_times = 0
			temp_n = 0
			temp_m = 0

			#將所有 結果陣列 元素取出並相加
			for i in m_result:
				temp_m = temp_m + i
			for i in n_result:
				temp_n = temp_n + i
			#算出所有組合的次數 
			win_total = temp_m * temp_n
			#k>i k==i k<i 分別代表 贏 平手 輸的情況
			for k in range(len(m_result)):
				for i in range(len(n_result)):
					if k > i:
						win_times = win_times + (m_result[k] * n_result[i])
					if k == i:
						even_times = even_times + (m_result[k] * n_result[i])
					if k < i:
						lose_times = lose_times + (m_result[k] * n_result[i])

			#約分成最簡分數
			divisor = math.gcd(win_total, win_times)#math.gcd()為求最大公因數之函數 為內建函式庫之函式
			#約分
			win_times_temp = win_times / divisor
			win_total_temp = win_total / divisor

			#輸出結果

			
			
			worksheet.write(q,p,round(win_times / win_total * 100,4))



			print(m,"vs",n)
			print(test)
			print("")
			workbook.close()
else:
	num = int(input("請輸入想要測試之顆數的最大值 >"))
	p = int(input("請輸入想要測試之面數 > "))	
	q = p
	workbook = xlsxwriter.Workbook('result(face).xlsx')
	worksheet = workbook.add_worksheet()
	for m in range(1,num+1):
		for n in range(1,num+1):	
		
			#不進位直式的函式	
			def muti(q,k):
				#q為陣列 k為整數
				result_len = len(q) + (len(str(k))-1)#計算對齊後的長度	
				result_list = []#定義回傳陣列
				for j in range(result_len):#將回傳陣列的每個元素都設為0 且0的數量為對齊後的長度
					result_list.append(0)
				for i in range(len(str(k))):#整數必須轉成string才能判斷其長度
					temp_q = list(q) #若直接將一個陣列賦值給另一個陣列 將會出現問題 故必須使用list()函數		 
					#將兩個陣列對齊 (24~28)
					for h in range(i):
						temp_q.append('0')				
					for l in range(result_len - len(temp_q)):
						temp_q.insert(0,'0')
					#將元素相加		
					for h in range(result_len):		
						result_list[h] = int(temp_q[h]) + result_list[h]
				#回傳結果
				return result_list
			#次方運算(不進位)
			def power(p,m):
				p_math = 0
				temp = 0
				#利用骰子面數創造111...111(1的個數為骰子面數)
				for i in range(p):		
					p_math = p_math*10 + 1
				temp = list(str(p_math))#將111...111轉成陣列
				#重複呼叫muti以算出結果 (指數)
				for k in range(1,m):
					temp = muti(temp,p_math)
				return temp #return 結果
				
				
			#定義變數	
			pm = m*p
			qn = n*q
			m_result = []
			n_result = []
			m_result_print_color = []
			n_result_print_color = []
			m_result_print = []
			n_result_print = []
			#輸入參數 並透過power與muti函式 return值為陣列
			for i in power(p,m):
				m_result_print_color.append(str(i)+colored('  X'+str(pm),'red')+', ')#可視化陣列
				m_result_print.append(str(i)+'  X'+str(pm))
				m_result.append(int(i))#判斷贏 平手 輸之陣列	
				pm = pm-1
				
			for k in power(q,n):
				n_result_print_color.append(str(k)+colored('  X'+str(qn),'red')+', ')#可視化陣列
				n_result_print.append(str(k)+'  X'+str(qn))
				n_result.append(int(k))#判斷贏 平手 輸之陣列
				qn = qn-1

			#將陣列對齊
			if p*m > q*n:
				math_len = p*m - n + 1	
				for i in range(math_len-len(m_result)):
					m_result.append(0)		
				for k in range(math_len-len(n_result)):
					n_result.insert(0, 0)
			if p*m < q*n:
				math_len = q*n - m + 1
				for i in range(math_len-len(n_result)):
					n_result.append(0)
				for k in range(math_len-len(m_result)):
					m_result.insert(0, 0)


			#將陣列元素翻轉以方便判斷
			m_result = m_result[::-1]
			n_result = n_result[::-1]
			#定義各個變數
			win_total = 0
			win_times = 0
			even_times = 0
			lose_times = 0
			temp_n = 0
			temp_m = 0

			#將所有 結果陣列 元素取出並相加
			for i in m_result:
				temp_m = temp_m + i
			for i in n_result:
				temp_n = temp_n + i
			#算出所有組合的次數 
			win_total = temp_m * temp_n
			#k>i k==i k<i 分別代表 贏 平手 輸的情況
			for k in range(len(m_result)):
				for i in range(len(n_result)):
					if k > i:
						win_times = win_times + (m_result[k] * n_result[i])
					if k == i:
						even_times = even_times + (m_result[k] * n_result[i])
					if k < i:
						lose_times = lose_times + (m_result[k] * n_result[i])

			#約分成最簡分數
			divisor = math.gcd(win_total, win_times)#math.gcd()為求最大公因數之函數 為內建函式庫之函式
			#約分
			win_times_temp = win_times / divisor
			win_total_temp = win_total / divisor

			#輸出結果

			
			
			worksheet.write(n,m,round(win_times / win_total * 100,4))



			print(m,"vs",n)
			
			print("")
	for i in range(num):
		worksheet.write(0,i+1,i+1)
		worksheet.write(i+1,0,i+1)


	workbook.close()
