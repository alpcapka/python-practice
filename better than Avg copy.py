C=int(input())
A=[]
B=[]
D=[]
for i in range(C):
    A.append(list(map(int,input().split())))
    B.append(sum(A[i][1:])/A[i][0])
    D.append(0)
    for j in range(1,len(A[i])):
        if B[i] < A[i][j]:
            D[i] += 1
    print(format(D[i]/A[i][0], '3.3%'))

    print(A[0][1])