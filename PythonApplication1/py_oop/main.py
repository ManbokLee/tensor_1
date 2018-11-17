from py_inher import Dog
from py_inher import Cat
from py_inher import Pet
# from py_inher import * # <- 모든 클래스 전부 가져옴. import py_inher 와 같음

def main():
    catPet = Pet('도둑고양이', '코리안숏헤어')
    dogPet = Pet('누렁이', '똥개')
    print(catPet)
    print(dogPet)

    cat = Cat('노랑고양이')
    dog = Dog('누렁이')

    print(cat)
    print(dog)

print('현재 실행중인 파일 이름 : %s' % __name__)
if __name__ == "__main__":
    main()


