""""
1)«Отдел» и «Сотрудник» связаны соотношением один-ко-многим.
 Выведите список всех отделов, у которых название начинается с буквы «А», и список работающих
  в них сотрудников.
2)«Отдел» и «Сотрудник» связаны соотношением один-ко-многим.
Выведите список отделов с максимальной зарплатой сотрудников в каждом отделе,
 отсортированный по максимальной зарплате.
3)«Отдел» и «Сотрудник» связаны соотношением многие-ко-многим.
Выведите список всех связанных сотрудников и отделов, отсортированный по отделам,
сортировка по сотрудникам произвольная.
7 Вариант (Микропроцессор, Компьютер,)
"""
from operator import itemgetter


class Micro:
    """Микропроцессор"""

    def __init__(self, id, name, sal, comp_id):
        self.id = id
        self.name = name
        self.sal = sal
        self.comp_id = comp_id


class Computer:
    """Компьютер"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class MicroInComputer:
    """
    'Микропроцессор' для реализации
    связи многие-ко-многим
    """

    def __init__(self, comp_id, emp_id):
        self.comp_id = comp_id
        self.micro_id = emp_id


# Компьтеры
computers = [
    Computer(1, 'MacBook'),
    Computer(2, 'RedmiBook'),
    Computer(3, 'AirBook'),

    Computer(11, 'HP'),
    Computer(22, 'Aurora'),
    Computer(33, 'Xiaomi'),
]

# Микропроцессоры
micros = [
    Micro(1, 'Intel-i5',  1),
    Micro(2, 'AMD-4000',  2),
    Micro(3, 'AMD-5000',  3),
    Micro(4, 'Intel-i7',  3),
    Micro(5, 'Intel-i9',  3),
]

goslings = [
    MicroInComputer(1, 1),
    MicroInComputer(2, 2),
    MicroInComputer(3, 3),
    MicroInComputer(3, 4),
    MicroInComputer(3, 5),

    MicroInComputer(11, 1),
    MicroInComputer(22, 2),
    MicroInComputer(33, 3),
    MicroInComputer(33, 4),
    MicroInComputer(33, 5),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many_fq = [(comp.name, mic.name)
                      for comp in computers
                      for mic in micros
                      if comp.id == mic.comp_id]
    # Соединение данных один-ко-многим
    one_to_many_curr = [(comp.name, dia.comp_id, dia.micro_id)
                      for comp in computers
                      for dia in goslings
                      if comp.id == dia.comp_id]

    many_to_many_ans = [(comp_name, m.name)
                    for comp_name, comp_id, mic_id in one_to_many_curr
                    for m in micros if m.id == mic_id]

    print("First Question")
    sorted(one_to_many_fq, key=itemgetter(0))
    i = 0
    j = 0
    """Sliding windows"""
    while i < len(one_to_many_fq) and one_to_many_fq[i][0].startswith('А'):
        if i == j:
            print(one_to_many_fq[j][0])
        while j < len(one_to_many_fq) and one_to_many_fq[j][0] == one_to_many_fq[i][0]:
            print(one_to_many_fq[j][1] + ' ' + str(one_to_many_fq[j][2]))
            j += 1
        i = j

    print("Second Question")
    sorted(one_to_many_fq, key=itemgetter(0,2))
    i = 0
    j = 0
    parks_maximus = []
    """Sliding windows"""
    while i < len(one_to_many_fq):
        curr = 0
        while j < len(one_to_many_fq) and one_to_many_fq[j][0] == one_to_many_fq[i][0]:
            if one_to_many_fq[j][2] > curr:
                curr = one_to_many_fq[j][2]
            j += 1
        parks_maximus.append((one_to_many_fq[i][0], curr))
        i = j
    for e in parks_maximus:
        print(e)
    print("Third Question")
    sorted(many_to_many_ans, key=itemgetter(0, 1))
    i = 0
    j = 0
    while i < len(many_to_many_ans) and j < len(many_to_many_ans):
        print(many_to_many_ans[i][0])
        while j < len(many_to_many_ans) and many_to_many_ans[j][0] == many_to_many_ans[i][0]:
            print('\t' + str(many_to_many_ans[j][1]))
            j += 1
        i = j
if __name__ == '__main__':
    main()