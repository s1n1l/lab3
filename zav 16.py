"""16. Дано додатні числа A і B (A> B). На відрізку довжиною A розміщено максимально можлива
кількість відрізків довжиною B (без накладання). Не використовуючи операції множення і ділення,
знайти довжину незайнятої частини відрізка A."""

a = int(input())
b = int(input())

def dl(a, b):
    while a >= b:
        a -= b
    return a

print(dl(a, b))

