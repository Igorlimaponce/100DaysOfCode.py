def task_of_day():
    print("Bem vindo a ilha do tesouro!!")
    print("Sua missao é achar o tesouro")
    resposta_caminho = str(
        input(
            "Voce esta na estrada, onde gostaria de ir?\nDigite 'esquerda' ou 'direita'\n"
        )
    )

    if resposta_caminho.lower() == "esquerda":
        print("voce chegou a uma montanha!")
        resposta_caminho2 = str(
            input(
                "Voce pode escolher entre:\n'esperar' por um barco ou 'nadar' até a ilha\n"
            )
        )
        match resposta_caminho2.lower():
            case "esperar":
                print(
                    "Voce chegou a um vilarejo, tem uma casa vermelha, uma amarela e uma azul"
                )
                resposta_caminho3 = str(input("Qual voce escolheria?\n"))

                match resposta_caminho3.lower():
                    case "vermelha":
                        print("Uma casa pegando fogo, jogo encerrado.")
                    case "amarela":
                        print(
                            "Uma casa com o tesouro dentro!!!!\nParabens voce ganhou!!!!"
                        )
                    case "azul":
                        print("Entrou em um quarto com bestas, jogo encerrado.")

            case "nadar":
                print("Voce foi atacado por uma criatura do mar, jogo encerrado.")

    elif resposta_caminho.lower() == "direita":
        print("Voce caiu do penhasco, jogo encerrado.")

    else:
        task_of_day()


task_of_day()
