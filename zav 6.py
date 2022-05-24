"""6. Логічній змінній t присвоїти значення true або false залежно від того, є натуральне число k
ступенем 3 чи ні."""


a = int(input())
def ph(a):
 t = 0
 while (a % 3) == 0:
  a = a / 3
 if a==1:
  t = 1
  if t==1:
   return 'true'
  else:
      return'false'


print (ph(a))