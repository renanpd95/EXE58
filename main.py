import os

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

os.system('clear')

if ( n1 % n2 ==0):
  print("N1 é múltiplo de N2")
else:
  print("N1 não é múltiplo de N2")