# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open("Makeeva_X.txt", "w", encoding="utf-8")
line = input('Введите данные >> \n')
while line:
    f.writelines(line)
    line = input('Введите данные>> \n')
    f.writelines('\n')
    if not line:
        break
f.close()