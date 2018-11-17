class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("안녕하세요. 저는 {0} 입니다. {1} 이에요.".format(self.name, self.name))
