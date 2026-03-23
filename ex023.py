#O mesmo professor do exercicio anterior quer sortear a ordem da apresentação de trabalhos de alunos. Faça um programa que leia
#o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

#Os [ ] guardam várias variáveis == lista.
alunos = [aluno1, aluno2, aluno3, aluno4]

print(f"A ordem apresentação dos alunos será de: {random.sample(alunos, 4)}")