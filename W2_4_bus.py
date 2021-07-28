print("버스요금계산기")
a = int(input("나이를 입력해주세요 "))
pay = input("결제유형: 카드 or 현금")


if pay =="카드":
    if a<8 and a>0: bus= "무료"
    elif a<14 and a>=8 : bus="450원"
    elif a <20 and a>=14 : bus="720원"
    elif a<75 and a>=20 : bus="1200"
    elif a>=75 : bus="무료"
    elif a<=0 : bus="나이를 다시입력해주세요"

if pay =="현금":
    if a<8 and a>0: bus="무료"
    elif a<14 and a>=8 : bus="450원"
    elif a <20 and a>=14 :bus= "1000원"
    elif a<75 and a>=20 : bus="1300"
    elif a>=75 : bus="무료"
    elif a<=0 : bus= "나이를 다시입력해주세요"

print("나이: "+str(a)+"\n결제유형: "+pay+"\n버스요금: "+ bus )
