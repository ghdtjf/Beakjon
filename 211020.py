# 사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)을 프로그램 작성
# 입력 예시1 : 1 + 2
# 입력 예시2 : 5 / 2
# 입력 예시3 : 3 * 9
# 출력 예시1 : 1 + 2 = 3
# 출력 예시2 : 5 / 2 = 2
# 출력 예시3 : 3 * 9 = 27


num = input()

for i in num:
    if i in ('+'):
        a = (num.split('+'))
        x = int(a[0])
        y = int(a[1])
        print(num, '=', '{}'.format(x+y))
    elif i in ('-'):
        a = num.split('-')
        x = int(a[0])
        y = int(a[1])
        print(num, '=', '{}'.format(x-y))
    elif i in ('*'):
        a = num.split('*')
        x = int(a[0])
        y = int(a[1])
        print(num, '=', '{}'.format(x*y))
    elif i in ('/'):
        a = num.split('/')
        x = int(a[0])
        y = int(a[1])
        print(num, '=', '{}'.format(x//y))