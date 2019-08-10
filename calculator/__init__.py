from calculator.controller import Calculatorcontroller
if __name__ == '__main__':
    num1 = int(input('첫번째 수\n'))
    num2 = int(input('두번째 수\n'))
    calc = Calculatorcontroller(num1, num2)
    op = input('연산자는?')
    result = calc.exec(op)
    print('계산결과 : %d ' % result)
    # %d 정수 %s 문장  %f 소수점

