password = 'A123456'
x = 0
y = 4
while x < 4 :
	password = input ('請輸入密碼')
	password = str(password)
	if password == 'A123456':
		print ('登入成功')
		x = x + 5
	else:
		x = x + 1
		y = y - 1
		print ('錯誤！您還有', y ,'次機會')
		while x == 4 :
			print ('錯誤您沒有機會了')
			break


