class Calculator: #사칙연산 클래스
	def add(self,num1,num2): #덧셈
		return num1 + num2
	def minus(self,num1,num2): #뺄셈
		return num1 - num2
	def multiple(self,num1,num2): #곱셈
		return num1 * num2
	def division1(self,num1,num2): #나눗셈1
		return num1 // num2
	def division2(self,num1,num2): #나눗셈2
		return num1 / num2
	def remainder(self,num1,num2): #나머지
		return num1 % num2
		
		

printInput = "결과값 : "
while(True): #무한반복
	print("===========================================================")
	a = int(input("숫자를 입력하세요: "))
	print("===========================================================")
	b = int(input("숫자를 입력하세요: "))
	print("===========================================================")
	type = int(input("어떤 연산을 하실건가요 ? \n\t 1.덧셈 \n\t 2.뺄셈 \n\t 3.곱셈 \n\t 4.나눗셈1 \n\t5.나눗셈2 \n\t6.나머지 \n"))
	print("===========================================================")
	try:
		call = Calculator()
		print(printInput)
		if(type == 1):
			print(call.add(a,b))
		elif(type == 2):
			print(call.minus(a,b))
		elif(type == 3):
			print(call.multiple(a,b))
		elif(type == 4):
			print(call.division1(a,b))
		elif(type == 5):
			print(call.division2(a,b))
		elif(type == 6):
			print(call.remainder(a,b))
		else:
			print("잘못입력하였습니다.");
	except Exception as e:
		print("에러" + e)
	print("===========================================================")
	yn = int(input("그만하시겠습니까? \n\t 1.계속하기 \n\t 2.그만하기 \n"))
	print("===========================================================")
	if(yn == 1):
		print("계속 진행합니다.")
	elif(yn == 2):
		break #반복문 탈출
	print("===========================================================")