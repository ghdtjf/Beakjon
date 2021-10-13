#if 4 < 3:
#    print("Hello World.")
#else:
#    print("Hi, there.")
print("Hi, there.")


#if True :
#    print("1")
#    print("2")
#else :
#    print("3")
#print("4")
print("1")
print("2")
print("4")


#if True :
#    if False:
#        print("1")
#        print("2")
#    else:
#        print("3")
#else :
#    print("4")
#print("5")
print("3")
print("5")


# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
# 단 출력 값의 범위는 0~255이다.

# 결괏값이 0보다 작은 값이되는 경우 0을 출력하고
# 255보다 큰 값이 되는 경우 255를 출력해야 한다.

data = int(input())
data -= 20
if 0 <= data and data <= 255:
    print(data)
elif data < 0:
    print(0)
else:
    print(255)


# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# (input() 함수를 사용할 것. 잘 모르겠다면 python input 함수 사용법 이라고 검색해서 사용법을 다시 익힐 것.)
fruit = ["사과", "포도", "홍시"]
data = input('좋아하는 과일은?')
if data in fruit:
    print('정답입니다')
else:
    print('오답입니다')


# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 006의 moive_rand 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
print(movie_rank)

# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# movie_rank 리스트에서 '럭키'를 삭제하라.
del movie_rank[3]
print(movie_rank)

# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
del movie_rank[2 : 4]
print(movie_rank)

# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)


# 다음 리스트에서 최댓값과 최솟값을 출력하라. 
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))
print(max(nums))

# 다음 리스트의 합을 출력하라.
num = [1,2,3,4,5]
print(sum(num))

# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 다음 리스트의 평균을 출력하라.
import numpy
nums = [1, 2, 3, 4, 5]
average = numpy.mean(nums)
print(f"average : {average}")

# 다음 코드를 for문으로 작성하라.
print("-------")
print("-------")
print("-------")
print("-------")
for list in [1,2,3,4]:
    print("-------")


# # 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
for i in [10,20,30]:
    print(i)
    print("-------")

# 다음 예시문을 통해 예상 되는 대로 반복문을 활용한 코드를 작성해보세요.
# 101
# 103
# 105
# 107
# 109
# 200
# 202
# 204
# 206
# 208
# ...
# 800
# 802
# 804
# 806
# 808
# 901
# 903
# 905
# 907
# 909

for i in range(1, 9+1):
    for j in range(0, 9+1):
        if i % 2 == j % 2:
            print(i, 0, j)

# 리스트에는 동물이름이 문자열로 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라.

리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.

리스트 = ["가", "나", "다", "라"]
for i in reversed(리스트):
   print(i)

