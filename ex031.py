#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado
#A multa irá custar R$7,00 por cada km acima do limite.

n = int(input("Digite a velocidade do carro: "))
if (n > 80):
    print("Você foi multado!")
    multa = (n - 80)*7
    print(f"O valor da multa será de R$: {multa}")