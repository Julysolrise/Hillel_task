# Задача 1
# Дано список словорей
# создать список кортежей
d = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
lst_tpl = [tuple(item.values()) for item in d]
print(lst_tpl)

[('red', 'high'), ('yellow', 'low')]


# Задача 2
# Дано словарь
# преобразовать его в список кортежей
a_dictionary = {"a": 1, "b": 2, "c": 3}
lst = list(a_dictionary.items())
print(lst)

# Задача 3
# Дано два списка
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

list2 = list(zip(list_a, list_b))
print(list2)

# Задача 4
# Дано словарь
# Создать кортеж занчений для первих трьох єлементов словоря

dict4 = {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}
list4 = list(dict4.values())[:3]
print(list4)

# Задача 5
# Дано список
# Создать кортеж
lst5 = ["bar", "baz", "qux", "etc"]
tpl5 = tuple(lst5)
print(tpl5)













