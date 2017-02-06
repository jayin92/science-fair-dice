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