A = int(input())
B = int(input())
C = int(input())

mp = A * B * C
mp = list(map(int, list(str(mp))))

for i in range(0, 10):
    count = 0
    for j in range(len(mp)):
        if(mp[j] == i):
            count += 1
    print(count)