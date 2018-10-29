def max_num(num1, num2, num3):
	if(num1>num2 and num1>num3):
		print('num1 is greatest')
		return num1
	elif (num2>num1 and num2>num3):
		print('num2 is greatest')
		return num2
	else:
		print('num3 is greatest')
		return num3
		
print(max_num(3,5,1))