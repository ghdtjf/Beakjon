class 전화기():
    def __init__(self):
        self.isOpen = False
        self.dialog = ""

    def getDialog(self):
        return self.dialog
    
    def 버튼누르기(self, 입력):
        if self.isOpen == True:
            self.dialog = 입력

    def 전원제어(self):
        # 꺼져 있을 때
        if self.isOpen == False:
            self.isOpen = True
        # 켜져 있을 때
        else:
            self.isOpen = False
            self.dialog = ""

phone = 전화기()
phone.전원제어()
phone.버튼누르기(input("입력>"))
print(phone.getDialog())
phone.전원제어()
