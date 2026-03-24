# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print("Informe 3 comprimentos e veremos se é possível formar um triângulo!")
a = float(input("Digite o comprimento de A: "))
b = float(input("Digite o comprimento de B: "))
c = float(input("Digite o comprimento de C: "))

if (a < b + c and b < a + c and c < a + b):
    print("O triângulo existe!")
else:
    print("O triângulo não existe!")