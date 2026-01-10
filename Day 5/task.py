import random


def task_of_day():
    print("Gerador de senhas automaticas")
    letras = int(input("Quantas letras quer que a senha tenha?"))
    simbolos = int(input("Quantos simbolos quer que a senha tenha?"))
    numeros = int(input("Quantos numeros quer que a senha tenha?"))

    lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_letras = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    lista_simbolos = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    lista_completa = []
    lista_completa.extend(random.sample(lista_numeros, numeros - 1))
    lista_completa.extend(random.sample(lista_letras, letras - 1))
    lista_completa.extend(random.sample(lista_simbolos, simbolos - 1))
    print(lista_completa)
    for index, character in enumerate(lista_completa):
        lista_completa[index] = str(character)
    random.shuffle(lista_completa)
    print(lista_completa)
    senha = "".join(lista_completa)

    print(f"Sua nova senha = {senha}")


task_of_day()
