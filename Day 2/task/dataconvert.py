def dataconvert():
    """converting data types"""
    print(int("123") + int("456"))  # int result
    print(float("123") + int("456"))  # float result

    print(type(input("Digite seu nome:\n")))
    print(
        f"Numero de letras no seu nome: {len(input('Digite seu nome: '))}"
    )  # Se eu usar essa forma de concatenar ele aceita o len() sem o str() antes
    print(
        "Numero de letras no seu nome: " + str(len(input("Digite seu nome: \n")))
    )  # Se eu usar essa forma de concatenar ele NAO aceita o len() sem o str() antes


dataconvert()
