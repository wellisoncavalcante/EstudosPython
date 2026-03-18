#Desenvolva um programa que leia as duas notas de um aluno, calcule a nota e mostre sua média.

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
media = (n1+n2)/2
print("A média entre {:.1f} e {:.1f} foi de: {}" .format(n1, n2, media))