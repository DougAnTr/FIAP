print('Este algoritmo verifica o dia da semana mais votado, de acordo com o votos inputados.')

print('A seguir, digite a quantidade de votos de acordo com o dia da semana:')

monday = int(input('Segunda-feira: '))
tuesday = int(input('Terça-feira: '))
wednesday = int(input('Quarta-feira: '))
thursday = int(input('Quinta-feira: '))
friday = int(input('Sexta-feira: '))

most_voted = 0
winner = ''

if monday > most_voted:
    most_voted = monday
    winner = 'Segunda-feira'

if tuesday > most_voted:
    most_voted = tuesday
    winner = 'Terça-feira'

if wednesday > most_voted:
    most_voted = wednesday
    winner = 'Quarta-feira'

if thursday > most_voted:
    most_voted = thursday
    winner = 'Quinta-feira'

if friday > most_voted:
    most_voted = friday
    winner = 'Sexta-feira'

print('O dia mais votado foi ' + winner + '!')
