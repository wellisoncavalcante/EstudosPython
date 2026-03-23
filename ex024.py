#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras em maiúsculas
# O nome com todas as letras em minúsculas
# Quantas letras no total (sem considerar os espaços)
# Quantas letras tem o primeiro nome.

nome = input("Digite seu nome: ")

print(nome.upper())
print(nome.lower())

#Substitui os espaços ' ' utilizando o "".
#Depois conta a quantidade de caracteres pelo len.
print(len(nome.replace(' ', "")))

#nome.split() = separa a String em listas.
#[0] pega a primeira lista.
#len(nome.split()[0])) == Conta quantos caracteres tem na primeira lista.

print(len(nome.split()[0]))