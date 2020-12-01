Case = int(input())
Ratiolist = []

for i in range(Case):
    Studentcnt = 0
    Hap = 0
    Avg = 0
    Ratio = 0
    info = list(map(int, input().split())) # 학생의 수, N명의 점수 입력

    for j in range(info[0]):
        Hap += info[j+1] # N명의 점수 합
    
    Avg = Hap // info[0] # 점수 평균

    for k in range(info[0]):
        if(info[k+1] > Avg):
            Studentcnt += 1 # 평균 점수보다 높은 점수의 학생들 수

    Ratio = "%.3f" % (Studentcnt / info[0] * 100) # 평균을 넘는 학생들의 비율

    Ratiolist.append(Ratio)

for i in range(Case):
    print(Ratiolist[i] + "%")