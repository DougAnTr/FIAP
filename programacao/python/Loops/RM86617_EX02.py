print('Este algoritmo calcula a média e o total gasto em dinheiro no dia.')

quantityExpenses = int(input('Por favor, informe quantas transações realizou hoje: '))
totalExpenses = 0.00
averageExpenses = 0.00

for expense in range(quantityExpenses):
    totalExpenses += float(input('Informe o valor gasto na {}ª transação (Ex.: 1.050,40) R$: '.format(expense + 1))
                           .replace('.', '')
                           .replace(',', '.'))

averageExpenses = totalExpenses / quantityExpenses

print('O total gasto hoje foi de R$ {0:.2f}'.format(totalExpenses))
print('A média de gastos do dia é R$ {0:.2f}'.format(averageExpenses))
