# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Всего затрачено ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Абстрактный метод'


class Coat(Clothes):
    def consumption(self):
        return f'Чтобы сшить одно пальто необходимо: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Абстрактный метод 2'


class Costume(Clothes):
    def consumption(self):
        return f'Чтобы сшить один костюм необходимо: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(600)
costume = Costume(70)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())