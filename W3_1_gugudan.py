number = int(input("몇 단? : "))
val=1
while number * val <= 50:
	print(str(number)+"X"+str(val)+"="+str(number * val))
	val = val+2
	if val > 10:
		print("구구단 끝")
		break
