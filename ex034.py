# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

n = int(input("Digite um ano qualquer: "))

if (n % 4 == 0 and n % 100 != 0):
    print("O ano é BISSEXTO!")
elif (n % 4 == 0 and n % 100 == 0 and n % 400 == 0):
    print("O ano é BISSEXTO!")
else:
    print("O ano não é BISSEXTO!")
