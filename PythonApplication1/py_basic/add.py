# **************************************
# -- 데이터 타입 6가지
# **************************************
'''
-------------- 스칼라 개념
Number: int, float, complex(복소수)
String: str
Boolean: 잘 안쓰임
-------------- 벡터 개념
List
Tuple
Dictionary
Set
'''

# String s = "Str"; # 자바
# var s = "Str"; # 자바 스크립트
hello = "Hello Python !!" # 파이선 변수선언시 선언 타입이 없음
print(hello[0]) # H
print(hello[2:5]) # llo
print(hello * 2)
print(hello + "JAVA")

a = 3
b = 4
print(a+b)


alist = ['a','b','c']
alist.append('d')
print(alist)

# Tuple : 읽기전용 리스트 read-only list
aTouple = ('a','b','c')
bTouple = alist

print(alist)
print(aTouple)
print(bTouple)

# Dictionart 헤쉬테이블 (맵, Json)
aDic = {}
print(aDic)


# 분기문

money = 100
if (money == 100):
    print('100원')
print('END')










