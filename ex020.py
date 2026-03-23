#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa

import math

a = float(input("Informe o valor do cateto adjacente: "))
b = float(input("Informe o valor do cateto oposto: "))
print(f"O cateto adjacente é {a}, cateto oposto é {b} e sua hipotenusa é {math.hypot(a, b)}")