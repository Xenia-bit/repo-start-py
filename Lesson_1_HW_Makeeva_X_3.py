# 3. Узнайте у пользователя число n (число в диапазоне от 0 до 9 включительно). Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input('Пожалуйста, введите цифру от 0 до 9  >> '))
print(n + (n*10+n) + (n*100 + (n*10) + n))