# 현재날짜기준으로 생년월일(8자리)로 만 나이와 일반 나이을 알아내는 프로그램 작성
# 현재날짜 기준이기 때문에 날짜가 변하더라도 나이가 달라질 수 있도록 만들 것.
# 입력 예시1 : 19881021
# 출력 예시1 : 만 32세, 34세
# 입력 예시2 : 19891019
# 출력 예시2 : 만 32세, 33세



import datetime

dt_now = datetime.datetime.now()
time = input()
time2 = list(time)
y = int(''.join(time2[0:4]))
m = int(''.join(time2[4:6]))
d = int(''.join(time2[6:8]))



if dt_now.month == m and d <= dt_now.day:
    print('만', int(dt_now.year) - y, '세', int(dt_now.year) - y+1, '세' )
elif dt_now.month == m and d > dt_now.day:
    print('만', int(dt_now.year) - y-1, '세', int(dt_now.year) - y+1, '세' )
elif dt_now.month < m and d <= dt_now.day:
    print('만', int(dt_now.year) - y-1, '세', int(dt_now.year) - y+1, '세' )
elif dt_now.month < m and d > dt_now.day:
    print('만', int(dt_now.year) - y-1, '세', int(dt_now.year) - y+1, '세' )
elif dt_now.month > m and d <= dt_now.day:
    print('만', int(dt_now.year) - y, '세', int(dt_now.year) - y+1, '세' )
elif dt_now.month > m and d > dt_now.day:
    print('만', int(dt_now.year) - y, '세', int(dt_now.year) - y+1, '세' )