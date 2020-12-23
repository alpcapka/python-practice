#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

#예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

#1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#3. 2에서 나온 배열의 3번째 숫자는 5입니다.

n = int(input()) # commands의 길이
commands = []
array = list(map(int, input().split()))  # array 입력

for i in range(n):
    inputCommands = list(map(int, input().split()))
    commands.append(inputCommands) # commands 입력


def solution(array, commands):
    answer = []

    for i in range (n):
        inputarray = []
        m = commands[i][1]-commands[i][0] + 1 # 몇개 자를지
        for j in range(m):
            inputarray.append(array[commands[i][0]-1+j]) # i번째 숫자부터 j번째 숫자까지 자르고
            inputarray.sort() # 정렬
        answer.append(inputarray[commands[i][2]-1])

    return answer

print(solution(array, commands))