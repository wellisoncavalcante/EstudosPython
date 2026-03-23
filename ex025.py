#Faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite o número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

n = (input("Digite um número inteiro de 0 a 9999: "))

print(f"Unidade: {n[0]}")
print(f"Dezena: {n[1]}")
print(f"Centena: {n[2]}")
print(f"Milhar: {n[3]}")