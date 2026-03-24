# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

n = int(input("Tente adivinhar o número que o computador pensou de 0 a 5: "))
b = random.randint(0,5)
print(f"O número escolhido pelo computador foi de: {b}")

if (b == n):
    print("PARABÉNS! Você escolheu o número correto!")
else:
    print("Você escolheu o número errado!")