from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5,51)
    if 5<=time and time <=15: # 매칭 성공
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt+=1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}".format(cnt))