def std_weight(height, gender):
    if gender == "남자":
        return float(height / 100) * float(height / 100) * float(22)
    elif gender == "여자":
        return float(height / 100) * float(height / 100) * float(21)

height = int(input("키 입력(cm) : ")) # 키 입력

while(1): # 성별 입력
    gender = str(input("성별 입력 (남자 / 여자) : "))

    if(gender != '남자' and gender != '여자'):
        print("다시 입력하세요\n")
        continue

    break

weight = '%0.2f' % std_weight(height, gender)


print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
