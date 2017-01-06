#import所需函式庫
import math
import sys
import os
from pyfiglet import figlet_format 
from termcolor import colored, cprint


#接收input
cprint(figlet_format('dice.py'),'cyan')          

p = int(input('p面骰 >'))
m = int(input('m顆 >'))
q = int(input('q面骰 >'))
n = int(input('n顆 >'))	
#檢查值的正確性
if p <= 0 or q <= 0 or m <= 0 or n <= 0 :
	print('數值不可為零')
	exit()
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


#輸出結果

with open("m_result.txt","w") as file:		
	file.truncate()
	for item in m_result_print:
		file.write("%s\n" % item)

with open("n_result.txt","w") as file:
	file.truncate()
	for item in n_result_print:
		file.write("%s\n" % item)	

cprint(str(p)+' 面骰骰 '+str(m)+' 顆的分布 ','green')
for item in m_result_print_color:
	print(item,end = '')
	if((m_result_print_color.index(item)+1) % 5 == 0):
		print(' ',end='\n')	
for i in range(2):
	print('')
cprint(str(q)+' 面骰骰 '+str(n)+' 顆的分布 ','cyan')
for item in n_result_print_color:
	print(item,end = '')
	if((n_result_print_color.index(item)+1) % 5 == 0):
		print(' ',end='\n')
for i in range(2):
	print('')
print("贏的次數: ", win_times)
print("平手的次數: ", even_times)
print("輸的次數: ", lose_times)
print("總次數: ",win_total)
print("勝率 (%) : ", round(win_times / win_total * 100,2)," %")#round()為四捨五入之函式