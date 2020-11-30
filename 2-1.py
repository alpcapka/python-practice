N = input("N : ")
K = input("K : ")
arr = []
count = 0

for i in range(1, int(N)+1):
    if int(N) % i == 0:
        arr.append(i)
        count += 1
    arr.sort()

if count < int(K):
    print(-1)
     
else:
    print(arr[int(K)-1])