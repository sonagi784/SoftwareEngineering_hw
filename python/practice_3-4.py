print("2016113519 유지훈")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calcArea(self):
        area = self.width * self.height
        return area
rect1 = Rectangle(5, 5)
print("Rec1's width :", rect1.width, " & height :", rect1.height)
print("-> Rec1's area :", rect1.calcArea())

rect2 = Rectangle(2, 6)
print("Rec2's width :", rect2.width, " & height :", rect2.height)
print("-> Rec2's area :", rect2.calcArea())