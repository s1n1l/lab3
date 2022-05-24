"""7. Дано ціле число N (> 2) і дві дійсні точки на числовій осі: A, B (A <B). Функція F (X) задана
формулою F (X) = 1 - sin (X). Вивести значення функції F в N рівновіддалених точках, що
утворюють розбиття відрізка [A, B]: F (A), F (A + H), F (A + 2H), ..., F (B)"""

import math


def foo(x):
    q = round(math.sin(math.radians(x)), 1)
    r = 1 - math.sin(x)
    return r

n = int(input())
a = float(input("A = "))
b = float(input("B (>A) = "))
h = (b - a) / n
for i in range(n + 1):
    f = a + i * h
    print(foo(f))