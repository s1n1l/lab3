"""11. Дано число A (> 1). Вивести найменше з цілих чисел K, для яких сума 1 + 1/2 + … + 1/K будет
більше A, і саму цю суму."""


a = int(input())

def mch(a, k = 1, s= 0 ):

    s += 1 / k
    if k > a and s > a:
        return k
    k += 1
    return (a, k, s)

print(mch(a))