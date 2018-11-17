
class MyStatic:
    def reset(self): # 파이썬 메소드 선언방식 self 는 인스턴스로 외부에서 호출할때 파람으로 주지 않음
        self.x = 0
        self.y = 0


a = MyStatic()

# 아래 두가지 명령의 결과는 같음. 인스턴트형태일대에는 self는 자도응로 자신이되지만 클래스에 접근할때에는 self 를 던저야함
a.reset()
MyStatic.reset(a)

print('a 값: ', a.x)
print('b 값: ', a.y)




