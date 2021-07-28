# 아래의 코드를 추가하면 됩니다
import random

# rsp == rock scissors paper
print("가위바위보 게임 시작")
my = input("가위,바위,보 중 하나를 적어주세요")
computer = random.choice(["가위","바위","보"])

if my == "가위" :
    if computer == "가위" :
        print("나: 가위 컴퓨터: 가위 비겼어요")
    elif computer == "바위" :
        print("나: 가위 컴퓨터 : 바위 컴퓨터가 이겼어요" )
    else:
        print("나: 가위 컴퓨터 : 보 내가 이겼어요" )
elif my == "바위":
    if computer == "바위":
        print("나: 바위 컴퓨터: 바위 비겼어요")
    elif computer == "보" :
        print("나: 바위 컴퓨터 : 보 컴퓨터가 이겼어요" )
    else:
        print("나: 바위 컴퓨터 : 가위 내가 이겼어요" )
elif my == "보":
    if computer == "보":
        print("나: 보 컴퓨터: 보 비겼어요")
    elif computer == "가위" :
        print("나: 보 컴퓨터 : 가위 컴퓨터가 이겼어요" )
    else:
        print("나: 보 컴퓨터 : 바위 내가 이겼어요" )
