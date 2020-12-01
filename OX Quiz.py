Start = int(input())
scorelist = []
cnt = 0
score = 0

for i in range(Start):
    string = list(map(str, input()))
    for j in range(len(string)):
        if(string[j] == 'O'):
            cnt += 1
            score += cnt
        elif(string[j] == 'X'):
            cnt = 0
    scorelist.append(score)
    cnt = 0
    score = 0

for i in range(Start):
    print(scorelist[i])            
