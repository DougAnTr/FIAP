print('Esse progrma calcula a velocidade média de um patinete')
distance = float(input('Qual foi a distância em metros percorrida pelo patinete? '))
time = float(input('Quantos minutos o patinete demorou para percorrer essa distância? '))
speed = distance / time
print('O patinete atingiu uma velociade média de {0:.2f} m/min'.format(speed))
