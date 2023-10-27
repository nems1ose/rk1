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
7 Вариант (Микропроцессор, Компьютер)
"""
from operator import itemgetter


class Driver:
    """Микропроцессор"""

    def __init__(self, id, name, date, comp_id):
        self.id = id
        self.name = name
        self.date = date
        self.comp_id = comp_id


class Computer:
    """Компьютер"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DriverInComputer:
    """
    'Микропроцессоры' для реализации
    связи многие-ко-многим
    """

    def __init__(self, comp_id, emp_id):
        self.comp_id = comp_id
        self.driver_id = emp_id


# Компьютеры
computers = [
    Computer(1, 'MacBook'),
    Computer(2, 'RedmiBook'),
    Computer(3, 'Imac'),

    Computer(11, 'XiaomiBook'),
    Computer(22, 'Ipad'),
    Computer(33, 'PopicBook'),
]

# Микропроцессоры
drivers = [
    Driver(1, 'Intel-i5' , 1998, 1),
    Driver(2, 'Intel-i7',  2010, 2),
    Driver(3, 'Intel-i9',  2021, 3),
    Driver(4, 'AMD-3',  2001, 3),
    Driver(5, 'AMD-6',  2004, 3),
]

goslings = [
    DriverInComputer(1, 1),
    DriverInComputer(2, 2),
    DriverInComputer(3, 3),
    DriverInComputer(3, 4),
    DriverInComputer(3, 5),

    DriverInComputer(11, 1),
    DriverInComputer(22, 2),
    DriverInComputer(33, 3),
    DriverInComputer(33, 4),
    DriverInComputer(33, 5),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many_fq = [(comp.name, driver.name, driver.date)
                      for comp in computers
                      for driver in drivers
                      if comp.id == driver.comp_id]
    # Соединение данных один-ко-многим
    one_to_many_curr = [(comp.name, dia.comp_id, dia.driver_id)
                      for comp in computers
                      for dia in goslings
                      if comp.id == dia.comp_id]

    many_to_many_ans = [(comp_name, d.name)
                    for comp_name, comp_id, driver_id in one_to_many_curr
                    for d in drivers if d.id == driver_id]

    print("First Question")
    sorted(one_to_many_fq, key=itemgetter(0))
    i = 0
    j = 0
    """Sliding windows"""
    while i < len(one_to_many_fq) and one_to_many_fq[i][0].startswith('M'):
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
