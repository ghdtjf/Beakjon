# 리모컨 만들기
# 리모컨이 켜진 상태에서는 채널 돌리기, 버튼 누르기 동작
# 리모컨이 꺼진 상태에서는 채널 돌리기, 버튼 누르기 동작 안함

# class 리모컨():
#     def __init__(self):
#         self.전원 = False
#         self.채널 = '1'

#     def 전원제어(self):
#         if self.전원 == False:
#             self.전원 = True
#         else:
#             self.전원 = False
    
#     def 버튼제어(self, 채널):
#         if self.전원 == True:
#             self.채널 = 채널
#             self.채널표시()
    
#     def 채널표시(self):
#         print(self.채널+"채널입니다.")

# 티비 = 리모컨()
# 티비.전원제어()
# 티비.버튼제어(input())
# 티비.전원제어()


# class 손선풍기():
#     def __init__(self):
#         self.전원 = False
#         self.단계 = int()
#     def 전원제어(self):
#         if self.전원 == False:
#             self.전원 = True
#             print('전원켜짐')
#         else:
#             self.전원 = False
#             self.단계 = 0
#             print('전원꺼짐')
#     def 버튼제어(self):
#         if self.전원 == True:
#             if self.단계 == 3:
#                 self.단계 = 0
#             else:
#                 self.단계 += 1

#             # self.단계 = (self.단계+1) % 4

#             # self.단계 = int(self.단계) + 1
#             # if (int(self.단계) + 1) > 4:
#             #     self.단계 = 0
#             print(int(self.단계), '단계입니다')
#         # else:
#         #     self.단계 = 0
#         #     print('전원꺼짐')

        

# 선풍기본체 = 손선풍기()
# 선풍기본체.전원제어()
# 선풍기본체.버튼제어()
# 선풍기본체.버튼제어()
# 선풍기본체.버튼제어()
# 선풍기본체.버튼제어()
# 선풍기본체.버튼제어()
# 선풍기본체.버튼제어()
# 선풍기본체.버튼제어()
# 선풍기본체.전원제어()

# 볼륨조절기 오른쪽 돌림 = 소리커짐 / 왼쪽 돌림 =  소리 작아짐 / 범위 = 0~100

class 볼륨조절기:
    def __init__(self):
        self.볼륨 = 0
    def 오른쪽돌리기(self):
        if self.볼륨 < 100:
            self.볼륨 += 1
        print(self.볼륨)
    def 왼쪽돌리기(self):
        if 0 < self.볼륨:
            self.볼륨 -= 1
        print(self.볼륨)

    

스피커 = 볼륨조절기()
스피커.오른쪽돌리기()
스피커.오른쪽돌리기()
스피커.오른쪽돌리기()
스피커.오른쪽돌리기()
스피커.오른쪽돌리기()
스피커.오른쪽돌리기()
스피커.오른쪽돌리기()
스피커.왼쪽돌리기()
스피커.왼쪽돌리기()
스피커.왼쪽돌리기()
스피커.왼쪽돌리기()


# class 선풍기():
#     def __init__(self):
#         self.전원 = False
#         self.약풍 = False
#         self.중풍 = False
#         self.강풍 = False
#     def 전원제어(self):
#         if self.전원 == False:
#             self.전원 = True
#         else:
#             self.전원 = False
#     def 약풍버튼(self):
#         if self.전원 == True:
#             self.약풍 = True
#             self.강풍 = False
#             self.중풍 = False
#             print('약풍')
#     def 중풍버튼(self):
#         if self.전원 == True:
#             self.중풍 = True
#             self.약풍 = False
#             self.강풍 = False
#             print('중풍')
#     def 강풍버튼(self):
#         if self.전원 == True:
#             self.강풍 = True
#             self.약풍 = False
#             self.중풍 = False
#             print('강풍')
#     def 정지버튼(self):
#         if self.전원 == True:
#             self.강풍 = False
#             self.약풍 = False
#             self.중풍 = False
#             print('정지')


# 스텐드 = 선풍기()
# 스텐드.전원제어()
# 스텐드.강풍버튼()
# 스텐드.약풍버튼()
# 스텐드.정지버튼()