# Crie um programa que leia o nome de uma pessoa e diga se ela possui "Cavalcante" no sobrenome.

n = input("Digite seu nome e sobrenome: ")
y = n.upper()
z = 'CAVALCANTE' in y

print(f'Se true você possui Cavalcante no sobrenome: {z}')