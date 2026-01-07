def calculatotalcadapessoa(value_refeicao, porgorjeta, value_divisao):
    """Function return the value each pearson will pay"""
    value_gorjeta = (porgorjeta * value_refeicao) / 100
    return round((value_refeicao + value_gorjeta) / value_divisao, 2)


x = input("Aperte x para comecar\n")

if x == "x":
    print("Bem vindo a calculadora de Gorjeta!")
    refeicao = float(input("Qual o total da Compra?\n"))
    gorjeta = int(input("quanto % gostaria de dar de gorjeta?\n"))
    divisao = int(input("Com quantas pessoas gostaria de dividir a gorjeta?\n"))

    total_cadapessoa = round(calculatotalcadapessoa(refeicao, gorjeta, divisao), 2)
    print(f"Cada pessoa deve pagar: ${total_cadapessoa}")
else:
    print("tecla errada")
