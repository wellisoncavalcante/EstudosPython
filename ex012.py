largura = float(input("Informe a largura da parede: "))
altura = float(input("Informa a altura da parede: "))
area = largura*altura
pintura = area/2
print(f"A dimensão da sua parede é igual a: {largura} x {altura} e a sua área é igual a: {area:.2f} m²")
print(f"Para pintar a sua parede, você vai necessitar de {pintura}l de tinta.")

