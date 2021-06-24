# capitalize()
txt = "original string"
x = txt.capitalize()
print(x)

# casefold()
txt = "My Original String"
x = txt.casefold()
print(x)

# center()
txt = "my string"
x = txt.center(50)
# в конце строки добавляем точку, чтобы видеть,
# где заканчивается новая строка
print(x + ".")

# count()
txt = '''Whether you use After Effects to animate a simple
video title sequence of to create complex special effects,
you generallly follow the same basic workflow.
The After Effects interface facilitates you work and adapts
to each stage of production'''
value = "ffects"
x = txt.count(value)
print(x)

# encode()
x = txt.encode()
print(x)

txt = "текст на русском языке"
x = txt.encode()
print(x)
