print('Vamos calcular o seu IMC!')

weight = float(input('Informe o seu peso (Kg): ').replace(',', '.'))
height = float(input('Informe a sua altura (metros) (utlize vírgula para dezenas, ex.: 1,74): ').replace(',', '.'))
imc = weight / (height * height)

if imc < 16:
    print('Seu IMC é {0:.2f}. Que classifica-se como Baixo pesso Grau III'.format(imc))
elif 16 <= imc < 17:
    print('Seu IMC é {0:.2f}. Que classifica-se como Baixo pesso Grau II'.format(imc))
elif 17 <= imc < 18.50:
    print('Seu IMC é {0:.2f}. Que classifica-se como Baixo pesso Grau I'.format(imc))
elif 18.50 <= imc < 25:
    print('Seu IMC é {0:.2f}. Que classifica-se como Peso Ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {0:.2f}. Que classifica-se como Sobrepeso'.format(imc))
elif 30 <= imc < 35:
    print('Seu IMC é {0:.2f}. Que classifica-se como Obesidade Grau I'.format(imc))
elif 35 <= imc < 40:
    print('Seu IMC é {0:.2f}. Que classifica-se como Obesidade Grau II'.format(imc))
else:
    print('Seu IMC é {0:.2f}. Que classifica-se como Obesidade Grau III'.format(imc))
