import random
import string
# Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
d = dict((i, i) for i in range(7))
print(id(dict))
print(d)
d_lst = list(d.items())
d_lst[0], d_lst[-1] = d_lst[-1], d_lst[0]
d.clear()
d.update((d_lst))
print(id(dict))
print(d)

# Что выведет этот код? p = {"name": "Mike", "salary": 8000} print(p.get("age")).
student = {"name": "Emmma", "class": 9, "marks": 75}
# use [] notation, but if key will not exists, it will raise KeyError
marks = student["marks"]
print(marks)

# use dict.get(), if key will not exists, it returns None
marks = student["marks"]
print(marks)

# look at the previous comment
p = {"name": "Mike", "salary": 8000}
print(p.get("age"))

# "d":sample = {"1":["a","b"], "2":["c","d"]}

list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
countries_cities = dict([word.split("-") for word in list_1])
cities_countries = dict((city, country) for country, city in countries_cities.items())
for city in list_2:
    print('City: ', city, 'Country: ', cities_countries.get(city))
print(countries_cities)

# alphabet = x
# print(alphabet)

# this task works only for English language, sorry
symbols = string.ascii_letters + string.digits + string.punctuation + string.whitespace
print(string.whitespace)
dict_encode = {}
dict_decode = {}

encode_list = list(symbols)
decode_list = list(symbols)
random.shuffle(decode_list)
for e, d in zip(encode_list, decode_list):
    dict_encode[e] = d
    dict_decode[d] = e

print(dict_decode)
print(dict_encode)


def encode_msg(msg):
    return ''.join([dict_encode.get(s) for s in msg])


def decode_msg(msg):
    return ''.join([dict_decode.get(s) for s in msg])


msg = input('Enter your msg: ')
encoded_msg = encode_msg(msg)
print('Encoded message: ', encoded_msg)
decoded_msg = decode_msg(encoded_msg)
print('Decoded message: ', decoded_msg)

# task with numbers dict
nums_dict = dict([(num, num**3) for num in range(1, 11)])
print(nums_dict.items())

string = "I wish I had an Angel"
frequency = {}
for letter in string:
    frequency[letter] = frequency.get(letter, 0) + 1

print(frequency.items())











