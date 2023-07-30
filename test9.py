def str_to_num(num):
    result = f'вы ввели неверное число {num}'

    if num.isdigit():
        if int(num) > 0:
            result = f'вы ввели положительное целое число {int(num)}'
        else:
            result = f'вы ввели ноль'

    elif num[0] == '-' and len(num) > 1 and num[1:].isdigit():
        result = f'вы ввели отрицательное целое число {int(num)}'

    elif num.replace('.', '', 1).replace('-', '', 1).isdigit()\
            and num.find('-') in (-1, 0):
        if float(num) > 0:
            result = f'вы ввели положительное дробное число {float(num)}'
        elif float(num) < 0:
            result = f'вы ввели отрицательное дробное число {float(num)}'

    return result


while True:
    input_str = input('введите число: ').replace(',', '.')
    if input_str.lower() in ('выход', 'exit', 'quit', 'e', 'q', 'в'):
        break
    elif input_str:
        print(str_to_num(input_str))
    else:
        print('Вы ничего не ввели, попробуйте ещё раз')