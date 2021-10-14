class Box():
    # 맴버 변수
    __size = { 'x': 0, 'y': 0 }
    # 맴버 변수
    __design = ""
    
    def setDesign(self, design="", size=(0,0)):
        self.__size['x'] = size[0]
        self.__size['y'] = size[1]
        self.__design = design
    
    def create(self):
        print(self.__design, self.__size, "완성!")
    
    def getDesign(self):
        print(self.__design)
    
    def getSize(self):
        print(self.__size)

    # 생성자
    def __init__(self):
        self.__size = { 'x': 0, 'y': 0 }
        self.__design = ""

boxs = list()

for i in range(5):
    box = Box()
    box.setDesign("불닭볶음면_%d" % i, (250 - i, 250 - i))
    boxs.append(box)

for box in boxs:
    box.create()