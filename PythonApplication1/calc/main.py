
from calc import Calc

def main():
    calc = Calc(int(input('첫번째 수: ')), int(input('두번재 수: ')))
    print(calc.first)
    print(calc.second)
    print('{} + {} = {}'.format(calc.first, calc.second, calc.sum()))
    print('{} * {} = {}'.format(calc.first, calc.second, calc.mul()))
    print('{} - {} = {}'.format(calc.first, calc.second, calc.sub()))
    print('{} / {} = {}'.format(calc.first, calc.second, calc.div()))



if __name__=='__main__':
    main()