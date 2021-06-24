# Вводятся три разных числа. Найти, какое из них является средним
# (Больше одного, но меньше другого)
print ("Введите три разных числа")
number_1 = float (input ("Введите первое число: "))
number_2 = float (input ("Введите второе число: "))
number_3 = float (input ("Введите третье число: "))
if (number_1 == number_2 or number_1 == number_3 or number_2 == number_3):
    print ("Вы ввели несколько одинаковых чисел.")
    print ("Но числа должны быть разными.")
    print ("Попробуйте еще раз.")
else:
    number_middle = None
    if (number_1 > number_2 and number_1 < number_3) or (number_1 < number_2 and number_1 > number_3):
        number_middle = number_1
    elif (number_2 > number_1 and number_2 < number_3) or (number_2 < number_1 and number_2 > number_3):
        number_middle = number_2
    elif (number_3 > number_1 and number_3 < number_1) or (number_3 < number_1 and number_3 > number_1):
        number_middle = number_3
    print ("Среднее число ", number_middle)
