# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
finans_pr = float(input('Введите сумму прибыли >> '))
finans_ub = float(input('Введите сумму издержек >> '))
if finans_pr > finans_ub:
    print('Поздравляем, Ваш доход составил', finans_pr - finans_ub)
sotr = int(input('Введите количество сотрудников Вашей фирмы >> '))
print('Доход на каждого сотрудника составляет', (finans_pr - finans_ub) / sotr)