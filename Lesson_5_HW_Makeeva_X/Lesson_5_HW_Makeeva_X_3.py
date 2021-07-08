# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

def workers_list():
    workers = [['Ford ', '24536.25 \n'], ['Kyk ', '18754.54 \n'], ['Zig ', '100000.56 \n'], ['Zag ', '465768.88']]
    try:
        with open('Makeeva_3_X.txt', 'r+', encoding="utf-8") as f:
            for i in range(len(workers)):
                f.writelines(workers[i])
            l = f.readlines()
            p = []
            sum_w = 0
            for i in range(len(l)):
                s = float((l[i].split())[1])
                if s < 20000:
                    p.append((l[i].split())[0])
                sum_w += s
            print(f'Средняя величина дохода сотрудников равна {sum_w / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(p)}')
    except FileNotFoundError:
        return 'Файл не найден.'


workers_list()