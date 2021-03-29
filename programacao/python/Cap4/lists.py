#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor no final da lista
jedi.append("Mace Windu")
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

# criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# incluindo um valor digitado no final da lista
jedi.append(input("Digite o nome de um jedi"))

# A variável assumirá cada um dos valores da lista
for nome in jedi:
    # para cada volta do loop, exibir o valor assumido
    print(nome)

#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)


#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor pelo usuário em uma posição específica da lista
jedi.insert(2, input("Digite o nome de um Jedi"))
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)


#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo o último valor inserido na lista
jedi.pop()
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)


#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo um valor em uma posição específica
jedi.pop(2)
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)


#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo um valor específico da lista
jedi.remove("Yoda")
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)


#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]
#exibição da lista
print("A lista foi criada assim: {}".format(valores))
#contagem de elementos
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))
#invertendo a lista
valores.reverse()
print("A lista agora está invertida: {}".format(valores))
#ordenando a lista
valores.sort()
print("A lista agora está ordenada: {}".format(valores))


#valores de uma lista
valores = [2, 3, 5, 10]
#tamanho da lista
tamanho = len(valores)
print("A lista tem {} elementos".format(tamanho))
#soma dos elementos
soma = sum(valores)
print("A soma dos elementos é {}".format(soma))


