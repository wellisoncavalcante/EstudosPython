# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,5 por km para viagens até 200km.
# Acima de 200km, cobre R$0,45

n = float(input("Digite a quantidade de km percorrido na sua viagem: "))

if (n <= 200):
    preco1 = (n*0.5)
    print(f"Você percorreu {n}km e o preço a ser pago será de: R${preco1}")
else:
    preco2 = (n*0.45)
    print(f"Você percorreu {n} e o preço a ser pago será de : R${preco2}")