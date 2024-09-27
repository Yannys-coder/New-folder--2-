from abc import ABC, abstractmethod

class animals(ABC):
    def move(self):
        pass
class human(animals):
    def move(self):
        print("I can walk and talk")

class dog(animals):
    def move(self):
        print("I can bark")

class cat(animals):
    def move(self):
        print("I can say meow")

x = human()
x.move()

x = dog()
x.move()

x = cat()
x.move()   