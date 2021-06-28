import math
"""
Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
Сформировать возрастающий список из чётных чисел (количество элементов 45);
Пользователь вводит число. Определить, содержит ли список данное число x. Вивести информационное сообщение содержит или не содержит ;
Найдите сумму и произведение элементов списка. Результаты вывести на экран;
Найти наибольший элемент списка и вывести его на экран;
Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение;
Поменять местами самый большой и самый маленький элементы списка;
Дан произвольный список. Представьте его в обратном порядке.
"""
lst_1 = [1] + [0] * 100 + [0]
print(lst_1)

lst_2 = list(range(2, 93, 2))
print(lst_2)

usr_num = int(input('Enter number: '))
if usr_num in lst_2:
    print('Yes, num is in list')
else:
    print('No, num is not in list')

s = sum(lst_2)
print('sum of elems in lst_2 is: ', s)

prod = math.prod(lst_2)
print('Product of elems in lst_2 is: ', prod)

m = max(lst_2)
print('Max of elems in lst_2 is: ', m)

lst_repeat = [1, 2, 2, 3, 4, 5]

set_of_elems = set(lst_repeat)
repeated_elems = []
for el in set_of_elems:
    num_of_elems = lst_repeat.count(el)
    if num_of_elems > 1:
        repeated_elems.append(el)

if repeated_elems:
    print(repeated_elems)
else:
    print('There is not repeated elems in the list')

min_el_index, max_el_index = lst_2.index(min(lst_2)), lst_2.index(max(lst_2))
lst_2[min_el_index], lst_2[max_el_index] = lst_2[max_el_index], lst_2[min_el_index]
print(lst_2)

reversed_lst = lst_2[::-1]
print(reversed_lst)



