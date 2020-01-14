def pos_and_neg(numbers):
    ''' Разделяет положительные и отрицательные в разные списки'''
    pos_numbers = []
    neg_numbers = []
    for number in numbers:
        try:               # если введен не integer, пропускает элемент списка
            if int(number) > 0:
                pos_numbers.append(number)
            elif int(number) < 0:
                neg_numbers.append(number) 
        except ValueError:
            pass
    return pos_numbers, neg_numbers


numbers_list = input('Type numbers divided by space\n').split(' ')

pos_numbers, neg_numbers = pos_and_neg(numbers_list)

print (f'Positive numbers: {pos_numbers} \nNegative numbers: {neg_numbers}.')