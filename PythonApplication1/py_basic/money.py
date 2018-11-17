money = input('총액을 입력하세요')
amount = int(money) # 캐스팅

if amount < 100:
    discount = amount * 0.05
    print('5% 할인금액', int(discount), '원 할인')
else:
    discount = amount * 0.1
    print('10% 할인금액', int(discount), '원 할인')
