a = 2
b = 10

class forWhile:
	#1) for문과 for문
	def for_for(self): 
		list = []
		list = [("%d*%d=%d"%(i,j,i*j)) for i in range(a,b) for j in range(a, b)]
		return list
	#2) for문과 while문
	def for_while(self): 
		list = []
		for i in range(a,b) :
			j = a
			while j < b :
				list.append(str(i) + "*" + str(j) + "=" + str(i*j))
				j += 1
		return list
	#3) while문과 for문
	def while_for(self):
		list = []
		i = a
		while i < b :
			for j in range(a,b) :
				list.append(str(i) + "*" + str(j) + "=" + str(i*j))
			i += 1
		return list
	#4) while문과 while문
	def while_while(self):
		list = []
		i = a
		while i < b :
			j = a
			while j<10 :
				list.append(str(i) + "*" + str(j) + "=" + str(i*j))
				j += 1
			i += 1 
		return list


forWhile = forWhile()

print("#1) for문과 for문")
print(forWhile.for_for())
print("#2) for문과 while문")
print(forWhile.for_while())
print("#3) while문과 for문")
print(forWhile.while_for())
print("#4) while문과 while문")
print(forWhile.while_while())

input()
