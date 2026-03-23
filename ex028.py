#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece pela última vez.

n = input("Digite uma frase: ")
y = n.upper()

print(f'Quantas vezes aparece a letra A?: {y.count('A')}')
print(f'Em que posição aparece pela primeira vez a letra A?: {y.find('A')}')
print(f'Em que posição aparece pela última vez a letra A?: {y.rfind('A')}')
