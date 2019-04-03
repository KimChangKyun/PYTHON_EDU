import time
result = 0

a = int(input("숫자를 입력하세요: "))
b = int(input("숫자를 입력하세요: "))
type = int(input("어떤 연산을 하실건가요 ? \n\t 1.덧셈 \n\t 2.뺄셈 \n\t 3.곱셈 \n\t 4.나눗셈1 \n\t5.나눗셈2 \n\t6.나머지 \n"))

if(type == 1):
	result = a + b
elif(type == 2):
	result = a - b
elif(type == 3):
	result = a * b
elif(type == 4):
	result = a // b
elif(type == 5):
	result = a / b
elif(type == 6):
	result = a % b
else:
	print("잘못입력하였습니다.")
print("결과값 : " + str(result))
time.sleep(30)