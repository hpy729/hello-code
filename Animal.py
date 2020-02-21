class Animal():
    kind = ''
    
    def __init__(self,name):
        self.name=name

    def voice(self):
        return 'wawowawo!'

class Dog(Animal):
    kind = 'canidae'
    
    def voice(self):
        return 'woof-woof!'
    bark = voice
    
class Cat(Animal):
    kind = 'felidae'
    
    def voice(self):
        return 'meow-meow!'
    mew = voice
    
a = Animal('キュゥべえ')
c = Cat('Garfield')
d = Dog('Snoopy')

for i in [a, c, d]:
    print(i.name,':',i.voice())
    

