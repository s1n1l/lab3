"""1. Підрахувати k - кількість цифр в десятковому запису цілого невід'ємного числа n."""

a = int(input())

def ch(a):
    b = len(str(a))
    return b


print(ch(a))