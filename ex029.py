#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Wellison Ruan de Oliveira Cavalcante
# primeiro = Wellison
# segundo = Cavalcante

n = input("Digite seu nome completo: ")

print(f'Seu primeiro nome é: {n.split()[0]}')
print(f'Seu último nome é: {n.split()[-1]}')