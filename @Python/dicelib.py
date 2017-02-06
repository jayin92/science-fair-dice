from termcolor import colored, cprint

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
def createList(rawList,maxPoint):	
	result = []
	result_print = []
	result_print_color = []
	for i in rawList:		
		result.append(int(i))#判斷贏 平手 輸之陣列	
		result_print.append(str(i)+'  X'+str(maxPoint))
		result_print_color.append(str(i)+colored('  X'+str(maxPoint),'red')+', ')#可視化陣列
		maxPoint = maxPoint-1

	return [result, result_print, result_print_color]
def listAlign(m_result,n_result,m,n,pm,qn):
	if pm > qn:
		math_len = pm - n + 1	
		for i in range(math_len-len(m_result)):
			m_result.append(0)		
		for k in range(math_len-len(n_result)):
			n_result.insert(0, 0)
	if pm < qn:
		math_len = qn - m + 1
		for i in range(math_len-len(n_result)):
			n_result.append(0)
		for k in range(math_len-len(m_result)):
			m_result.insert(0, 0)
def newLine(n):
	for i in range(n):
		print('')
def printList(list):
	for item in list:
		print(item,end = '')
		if((list.index(item)+1) % 5 == 0):
			print(' ',end='\n')
