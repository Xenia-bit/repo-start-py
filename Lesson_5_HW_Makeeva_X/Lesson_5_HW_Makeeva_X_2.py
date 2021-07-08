# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
def count_file():
    try:
        with open('Makeeva_2_X.txt', 'r', encoding="utf-8") as f:
            my_ = f.readlines()
            for i in range(len(my_)):
                l = my_[i].split()
                print(f'Количество строк в файле {len(my_)}. В {i + 1}-ой строке {len(l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'
count_file()