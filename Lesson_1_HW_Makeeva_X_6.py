# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = int(input('Введите количество километров в первый день >> '))
b = int(input('Введите количество километров, которого хотите достичь >> '))
day = 1
while a <= b:
    a = a + a*0.1
    day +=1
print(day)