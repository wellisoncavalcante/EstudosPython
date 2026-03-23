frase = "Curso em Vídeo Python"
"""
C = 00 // u = 01 // r = 02 // s = 03 // o = 04  //   = 05
e = 06 // m = 07 //   = 08 // V = 09 // í = 10 // d = 11
e = 12 // o = 13 //   = 14 // P = 15 // y = 16 // t = 17
h = 18 // o = 19 // n = 20
"""
#Encontra a String número 9
print(frase[9])

#Começa da string 9 até a String 12
print(frase[9:13])

#Começa da String 9 até a String 20
print(frase[9:21])

#Começa da String 9 até a String 20, pulando de 2 em 2
print(frase[9:21:2])

#Começa da String 0 até a String 4
print(frase[:5])

#Começa da String 15 até o final
print(frase[15:])

#Começa da String 9, até o final, pulando de 3 em 3
print(frase[9::3])

#Fala o comprimento da frase
print(len(frase))

#Conta quantas vezes aparece a String 'o'
print(frase.count('o'))

#Procure por 'o', comece do 0 até a String 13
print(frase.count('o', 0, 13))

#Indica onde começa o 'deo'
print(frase.find('deo'))

#Indica onde começa a palavra Android. Se não existir, retorna -1
print(frase.find('Android'))

#Retorna true or false se existir a palavra 'Curso' na variável frase.
print('Curso' in frase)

#Altera 'Python' por 'Android' == Curso em Vídeo Android
print(frase.replace('Python', 'Android'))

#Transforma toda a frase em maiúsculo
print(frase.upper())

#Transforma a frase em minúsculo
print(frase.lower())

#Deixa apenas a primeira String da variável em maiúscula
print(frase.capitalize())

frase2 = '   Aprenda Python  '

#Retira todos os espaços inúteis do começo e do fim.
print(frase2.strip())

#Retira apenas os espaços inúteis do final
print(frase2.rstrip())

#Retira apenas os espaços inúteis do começo
print(frase2.lstrip())

#Cada palavra dessa variável vira uma nova lista ['Curso', 'em', 'Vídeo', 'Python']
print(frase.split())

#Adiciona '-' após cada letra.
print('-'.join(frase))