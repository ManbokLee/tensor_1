# 상속

class Pet(object):

    def __init__(self, name, species): # __ <- 이게 private
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self): # <- 클래스를 문자로 사용하게 되는 경우 리턴 값
        return "동물정보: %s(%s)" % (self.name, self.species)

class Dog(Pet): # 상속
    def __init__(self, bow):
        self.bow = bow
    def __str__(self):
        return "동물정보: %s" % self.bow 


class Cat(Pet):
    def __init__(self, yam):
        self.yam = yam
    def __str__(self):
        return "동물정보: %s" % self.yam 

'''
catPet = Pet('노랑고양이', '코리안숏헤어')
dogPet = Pet('누렁이', '똥개')
print(catPet)
print(dogPet)

cat = Cat('노랑고양이')
dog = Dog('누렁이')

print(cat)
print(dog)
'''

