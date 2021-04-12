print('Este algoritmo verifica de um número está na sequência de Fibonnaci.')

value = int(input('Por favor, informe o número a ser verificado: '))
fibonnaciElement = 1
lastFibonnaciElement = 0

while fibonnaciElement < value:
    element = fibonnaciElement
    fibonnaciElement += lastFibonnaciElement
    lastFibonnaciElement = element


if fibonnaciElement == value:
    print('Ação bem sucedida!')
else:
    print('A ação falhou...')
