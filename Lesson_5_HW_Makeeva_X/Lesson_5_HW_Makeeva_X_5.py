# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def r_file():
    try:
        with open('Makeeva_5_X.txt.txt', 'r+') as f:
            f.write(input('Введите числа через пробел: '))
            l = map(int, f.read().split())
            print(sum(l))
    except FileNotFoundError:
        return 'Файл не найден.'


r_file()