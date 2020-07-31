def calc():
    operand = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operand == '0':
        print('Вы вышли из программы!\n')
    else:
        try:
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))
            if operand == '+':
                print('Сумма равна: ', num1 + num2)
                calc()
            if operand == '-':
                print('Разность равна: ', num1 - num2)
                calc()
            if operand == '*':
                print('Произведение равно: ', num1 * num2)
                calc()
            try:
                if operand == '/':
                    print('Частное равно: ', num1 / num2)
                    calc()
            except ZeroDivisionError:
                print('Нельзя делить на ноль!\n')
                calc()
            else:
                print('Вы ввели неизвестный оператор!\n')
                calc()
        except ValueError:
            print('Надо вводить числа!!!\n')
            calc()


calc()
