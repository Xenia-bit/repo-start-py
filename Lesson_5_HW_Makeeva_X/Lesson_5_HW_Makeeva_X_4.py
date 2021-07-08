# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def r_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('Makeeva_4_X.txt', 'r+', encoding="utf-8") as f:
            with open('New_Makeeva_4_X.txt', 'r+', encoding="utf-8") as n_file:
                l = f.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                n_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


r_file()