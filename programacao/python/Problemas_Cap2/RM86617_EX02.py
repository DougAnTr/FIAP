print('Este algoritmo exibe o bônus adquirido de acordo com o plano escolhido.')

plan = int(input('Digite o número correspondente ao plano adquirido:\n 1) Basic\n 2) Silver\n 3) Gold\n 4) Platinum\n -> '))
revenue = float(input('Informe o faturamento em reais (utilize vírgula para decimais e ponto para milhares): R$ ').replace('.', '').replace(',', '.'))


def calculate_bonus(percent):
    bonus = revenue * (percent / 100)
    print('O bônus a receber é R${0:.2f}'.format(bonus))


if plan == 1:
    calculate_bonus(30)
elif plan == 2:
    calculate_bonus(20)
elif plan == 3:
    calculate_bonus(10)
elif plan == 4:
    calculate_bonus(5)
