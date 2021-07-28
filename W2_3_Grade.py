print("학점계산기")
name = input("이름을 적어주세요")
score = int(input("점수를 적어주세요"))

if  score <=100 and score>=95 :
    grade = "A+"
elif score <=94 and score>=90 :
    grade ="A"
elif score <=89 and score>=85 :
    grade ="B+"
elif score <=84 and score>=80 :
     grade ="B"
elif score <=79 and score>=75 :
    grade ="C+"
elif score<= 74 and score>=70 :
    grade="C"
elif score<= 69 and score>=65 :
    grade="D+"
elif score<= 64 and score>=60 :
    grade="D"
else : grade = "F"

print("이름:"+ str(name)+ "\n점수:"+str(score)+"\n학점:"+grade)
