import random

palavras_aleatorias = [
    "teste",
    "python",
    "programacao",
    "desenvolvedor",
    "codigo",
    "computador",
    "teclado",
    "monitor",
    "internet",
    "software",
    "hardware",
    "algoritmo",
    "função",
    "variavel",
    "loop",
    "condicional",
    "lista",
    "dicionario",
    "string",
    "inteiro",
    "float",
]

palavra = random.choice(palavras_aleatorias).lower()

tentativa_palavra = ""
tentativas = 5

letras_usadas = []

for index in range(len(palavra)):
    tentativa_palavra += "_"

print(tentativa_palavra)

while tentativa_palavra != palavra and tentativas > 0:
    letra = ""
    while letra not in letras_usadas:
        letra = input("Digite uma letra\n").lower()
        if letra in letras_usadas:
            print("Voce nao pode repetir letras")
        else:
            letras_usadas.append(letra)

    achou_letra = False
    for index, letras in enumerate(palavra):
        if letra == letras:
            tentativa_palavra = (
                tentativa_palavra[:index] + letras + tentativa_palavra[index + 1 :]
            )
            achou_letra = True
    if not achou_letra:
        tentativas -= 1

    print(tentativa_palavra)
    print(f"Quantidade de tentativas restantes: {tentativas}")
if tentativa_palavra == palavra:
    print(f"Parabens voce acertou!! A palvra era {tentativa_palavra}")
else:
    print(f"Voce perdeu, a palavra era {palavra}")
