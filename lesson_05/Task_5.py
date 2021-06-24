# Вводятся три целых числа. Определить какое из них наибольшее.
print ("Введите три числа")
number_1 = float (input ("Введите первое число: "))
number_2 = float (input ("Введите второе число: "))
number_3 = float (input ("Введите третье число: "))
# в условии задачи не сказано, что числа должны быть разными
if number_1 >= number_2 and number_1 >= number_3:
    number_max = number_1
elif number_2 >= number_1 and number_2 >= number_3:
    number_max = number_2
else:
    number_max = number_3
print ("Наибольшее число ", number_max)