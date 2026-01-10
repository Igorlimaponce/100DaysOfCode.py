print("Bem vindo ao parque de diversoes!")
altura = float(input("Qual a sua altura? (Em metros)"))
total = 0

if altura >= 1.2:
    print("pode entrar no brinquedo")
    idade = int(input("Qual sua idade?\n"))

    if idade >= 18:
        print("Voce devera pagar 12 reais")
        total = 12
    elif idade >= 45 and idade <= 55:
        print("Fique a vontade, seu ingresso foi de graca")
    else:
        print("Voce devera pagar 7 reais")
        total = 7

    foto = str(
        input(
            "Deseja adicionar fotografias ao seu pacote de brinquedos?\nDigite apenas 'sim' ou 'nao'"
        )
    )

    if foto == "sim":
        total += 3

    print(f"total da sua conta = {total}")

else:
    print("nao pode entrar no brinquedo")
