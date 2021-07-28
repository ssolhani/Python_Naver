print("연봉계산기")
# 월급 입력
monthly_payment = int(input("급여를 적어주세요: "))
yearly_payment = (monthly_payment*12)


if yearly_payment <=1200: tax = int(yearly_payment*0.94)
elif yearly_payment <=4600 : tax = int(yearly_payment*0.85)
elif yearly_payment <= 8800 :tax =  int(yearly_payment*0.76)
elif yearly_payment <=15000: tax = int(yearly_payment*0.65)
elif yearly_payment <=30000: tax = int(yearly_payment*0.62)
elif yearly_payment <= 50000: tax = tax = int(yearly_payment*0.6)
else: tax = int(yearly_payment*0.58)

print("나의 세전연봉:" + str(yearly_payment) +"만원입니다")
print("나의 세후연봉:" + str(tax) +"만원입니다")


     
