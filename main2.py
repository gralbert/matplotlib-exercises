import matplotlib.pyplot as plt
import numpy as np


def ex1():
    """ Make currency dynamics. """
    cy = []
    date = []
    d = 1
    with open("file1.txt") as f:
        for item in f:
            date.append(d)
            item = float(item)
            cy.append(item)
            d += 1
    plt.plot(date, cy)
    plt.xlabel('Дни')
    plt.ylabel('Курс валюты')
    plt.title('Курс валюты США')
    plt.show()


def ex2():
    """ Make multiple currency dynamics. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as _file:
        for item in _file:
            date.append(d)
            a, b, c = item.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1
    plt.plot(date, cur1, date, cur2, date, cur3)
    plt.xlabel('Дни')
    plt.ylabel('Курс валюты')
    plt.title('Сравнение курса доллара, йены, евро ')
    plt.show()


def ex3():
    """ Improve currency dynamics. """
    cur1 = []
    cur2 = []
    cur3 = []
    date = []
    d = 1
    with open('file2.txt') as f:
        for item in f:
            date.append(d)
            a, b, c = item.split()
            cur1.append(float(a))
            cur2.append(float(b))
            cur3.append(float(c))
            d += 1

    plt.plot(date, cur1, date, cur2, date, cur3)
    plt.xlabel('Дни')
    plt.ylabel('Курс  валюты')
    plt.title('Сравнение курса  валюты доллара, йены, евро')
    plt.grid(True)
    plt.show()


def main():
    num = int(input('Введите номер задачи: '))
    if num == 1:
        ex1()
    if num == 2:
        ex2()
    if num == 3:
        ex3()


if __name__ == "__main__":
    main()
