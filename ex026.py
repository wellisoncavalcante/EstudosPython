#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

n = input("Digite o nome da sua cidade: ")
y = n.upper()
if (y.split()[0] == "SANTO"):
    print("O nome da cidade começa com Santo!")
else:
    print("O nome da cidade não começa com Santo!")