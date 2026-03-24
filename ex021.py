#Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
import math

n = float(input("Digite um valor de um ângulo qualquer: "))
m = math.radians(n)
print(f"O seno desse ângulo é de: {math.sin(m):.2f}, o cosseno é de: {math.cos(m):.2f}, a tangente é de: {math.tan(m):.2f}")
