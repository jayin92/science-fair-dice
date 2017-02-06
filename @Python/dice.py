#import所需函式庫
import math
import sys
import os
import time
from dicelib import *
from pyfiglet import figlet_format 
from termcolor import colored, cprint


#接收input
cprint(figlet_format('dice.py'),'cyan') 
print("  ")         
cprint("骰子皆為6面",'magenta','on_white')
print("  ")     
p = 6
m = int(input('進攻方骰子顆數 >'))
q = p
#q = int(input('q面骰 >'))
n = int(input('防守方骰子顆數 >'))	
#檢查值的正確性
if p <= 0 or q <= 0 or m <= 0 or n <= 0 :
	print('數值不可為零')
	exit()
#不進位直式的函式	

	
tStart = time.time()	
#定義變數	
m_result = []
m_result_print = []
m_result_print_color = []

pm = m*p
qn = n*q

m_list = createList(power(p,m),pm)
m_result = m_list[0] 
m_result_print = m_list[1]
m_result_print_color = m_list[2]

n_list = createList(power(q,n),qn)
n_result = n_list[0] 
n_result_print = n_list[1]
n_result_print_color = n_list[2]
#將陣列對齊
listAlign(m_result,n_result,m,n,pm,qn)


#定義各個變數
win_total = 0
win_times = 0
even_times = 0
lose_times = 0


#將所有 結果陣列 元素取出並相加
sum_m = sum(m_result)
sum_n = sum(n_result)
m_result = m_result[::-1]
n_result = n_result[::-1]
#算出所有組合的次數 
win_total = sum_m * sum_n
#k>i k==i k<i 分別代表 贏 平手 輸的情況
for k in range(len(m_result)):
	for i in range(len(n_result)):
		if k > i:
			win_times += m_result[k] * n_result[i]
		if k == i:
			even_times += m_result[k] * n_result[i]
		if k < i:
			lose_times += m_result[k] * n_result[i]

tEnd = time.time()

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
printList(m_result_print_color)
newLine(2)
cprint(str(q)+' 面骰骰 '+str(n)+' 顆的分布 ','cyan')
printList(n_result_print_color)
newLine(2)

print("贏的次數: ", win_times)
print("平手的次數: ", even_times)
print("輸的次數: ", lose_times)
print("總次數: ",win_total)
print("勝率 (%) : ", round(win_times / win_total * 100,4)," %")#round()為四捨五入之函式
print("運算時間 : "+str(round(tEnd - tStart,3))+" 秒")