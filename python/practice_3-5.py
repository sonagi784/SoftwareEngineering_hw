print("2016113519 유지훈")

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(self.name, ": move")
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print(self.name, ": bark")
        
class Duck(Animal):
    def speak(self):
        print(self.name, ": quack")
        
dog = Dog("doggy")
print("Dog name :", dog.name)
dog.move()
dog.speak()

duck = Duck("donald")
print("Duck name :", duck.name)
duck.move()
duck.speak()