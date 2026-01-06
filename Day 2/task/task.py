def calculaTotalCadaPessoa(refeicao, gorjeta, divisao):
    return (refeicao + gorjeta) / divisao


x = input("Aperte x para comecar\n")

if x == "x":
    print("Bem vindo a calculadora de Gorjeta!")
    refeicao = int(input("Qual o total da Compra?\n"))
    gorjeta = int(input("quanto gostaria de dar de gorjeta\n"))
    divisao = int(input("Com quantas pessoas gostaria de dividir a gorjeta?\n"))

    total_cadapessoa = calculaTotalCadaPessoa(refeicao, gorjeta, divisao)
    print(f"Cada pessoa deve pagar: ${total_cadapessoa}")
else:
    print("tecla errada")
