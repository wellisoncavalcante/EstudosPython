import math
import random

n = int(input("Informe um número: "))
#math.sqrt == calcula a raíz de um número
#math.ceil == arredonda um número para cima
#math.floor == arredonda um número para baixo
raiz = math.sqrt(n)
print(f"A raiz de {n} é igual a {raiz}")
print(f"A raiz de {n} é igual a {raiz.__ceil__()}")
print(f"A raiz de {n} é igual a {raiz.__floor__()}")

#random.randint(x,y) == gera um número aleatório de x até y
num = random.randint(1,100)
print(num)