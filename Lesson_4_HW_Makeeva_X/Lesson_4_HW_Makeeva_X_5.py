# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
my_list_new = []
my_list = [i for i in range(100, 1001, 2)]
for j in range(100, len(my_list)-1):
    for n in range(j, len(my_list)):
        my_list_new.append(j*n)
print(my_list_new)


# Не получилось :о(----------------------------------------------------------------------------------------------------------
'''
from  functools import reduce

def my_list_new2(x, y):
    return x * y

my_list2 = [z for z in range(100, 1001, 2)]
print(my_list2, reduce(my_list_new2, my_list2))'''
