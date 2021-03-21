def switch():
    value1 = input("Por favor, digite o primeiro valor: ")
    value2 = input("Por favor, digite o segundo valor: ")
    operation = int(input("Escolha a operação desejada: \n 1)Soma\n 2)Subtração\n 3)Multiplicação\n 4)Divisão \n -> "))

    def sum_numbers():
        result = float(value1) + float(value2)
        print("O resultado é {}".format(result))

    def subtract_numbers():
        result = float(value1) - float(value2)
        print("O resultado é {}".format(result))

    def multiply_numbers():
        result = float(value1) * float(value2)
        print("O resultado é {}".format(result))

    def divide_numbers():
        result = float(value1) / float(value2)
        print("O resultado é {}".format(result))

    def default():
        print("Operação não encontrada")

    operations = {
        1: sum_numbers,
        2: subtract_numbers,
        3: multiply_numbers,
        4: divide_numbers
    }
    operations.get(operation, default)()


switch()
