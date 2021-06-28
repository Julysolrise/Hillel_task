# Задан некоторый список Aсодержащий целые числа. Pазработать программу, которая вычисляет сумму элементов списка.
import random
from string import ascii_lowercase as letters

# generate random length of list
lst_len_rand = random.randint(2, 30)

# generate list of random nums
lst = [random.randint(0, 100) for i in range(lst_len_rand)]

print(lst)


def custom_sum(lst):
    length = len(lst)
    index = 0
    sum_of_list = 0
    while index < length:
        sum_of_list += lst[index]
        index += 1
    return sum_of_list


s_native = sum(lst)
s_custom = custom_sum((lst))

print('s_native: ', s_native)
print('s_custom: ', s_custom)

# Задан список строк. В каждой строке подсчитать количество вхождений заданного символа

# generate length for list of strings
len_lstOfStrings = random.randint(2, 10)

# create the empty list
listOfStrings = list()

# fill list with ransom strings
MAX_LENGH_OF_STR = 20
for i in range(len_lstOfStrings):
    # len of random string
    len_rand_str = random.randint(2, MAX_LENGH_OF_STR)
    word = ''
    # create random string
    for j in range(len_rand_str):
        letter = random.choice(letters)
        word += letter
    listOfStrings.append(word)

# create random letter, for what we are searching
rand_letter = random.choice(letters)
print(listOfStrings)
print('String'.ljust(MAX_LENGH_OF_STR), 'letter for search'.ljust(MAX_LENGH_OF_STR), 'Count'.ljust(MAX_LENGH_OF_STR))
for word in listOfStrings:
    print(word.ljust(MAX_LENGH_OF_STR), rand_letter.ljust(MAX_LENGH_OF_STR), str(word.count(rand_letter)).ljust(MAX_LENGH_OF_STR))

# Пользователь вводит число. Определение наличия заданного элемента в списке list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]. Если элемент не найден, то выводится соответствующее сообщение

list = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
user_num_inp = int(input('Enter number: '))
is_in_list = user_num_inp in list
if is_in_list:
    print('Yes, num is in list.')
else:
    print('No, num is not in list.')
