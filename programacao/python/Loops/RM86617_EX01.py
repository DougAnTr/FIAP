print('Este algoritmo calcula a quantidade de calorias ingeridas diariamente.')

quantityFood = int(input('Por favor, informe a quantidade de alimentos que ingeriu hoje: '))
calories = 0

for food in range(quantityFood):
    calories += int(input('Digite a quantidade de calorias do {}º alimento: '.format(food + 1)))

print('{} calorias foram ingeridas hoje.'.format(calories))
