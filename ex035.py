# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcula um aumenta 10%
# Para os inferiores ou iguais, o aumento é de 15%

n = float(input("Informe o seu salário: "))
if (n > 1250):
    aumento10 = (n*1.1)
    print(f"O seu salário de {n} recebeu um aumento de 10%, agora é de: {aumento10:.2f}")
else:
    aumenta15 = n*1.15
    print(f"O seu salário de {n} recebeu um aumento de 15%, agora é de {aumenta15:.2f}")