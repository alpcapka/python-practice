from random import *

Drive_time = 0
count = 0


for i in range(1, 51):
    Drive_time = randint(5, 50)
    if(5 <= Drive_time <= 15):
        print("[O] ", i, "번째 손님 (소요시간 : ", Drive_time, "분)")
        count += 1
    else:
        print("[ ] ", i, "번째 손님 (소요시간 : ", Drive_time, "분)")
    
print("\n총 탑승 승객 : ", count, " 분")    