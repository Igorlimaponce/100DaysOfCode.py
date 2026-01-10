print("Bem vindo ao delivery de pizza do python!")
print("Vamos comecar seu pedido!")

tamanho = str(input("Qual tamanho da pizza desejada? 's' 'm' 'g'\n"))
pepperoni = str(input("Deseja adicionar pepperoni na sua pizza? 's' 'n'\n"))
while pepperoni != "s" and pepperoni != "n":
    pepperoni = str(input("Deseja adicionar pepperoni na sua pizza? 's' 'n'\n"))
extra_queijo = str(input("Deseja adicionar mais queijo na pizza? 's' 'n'\n"))

conta = 0

match tamanho.lower():
    case "s":
        conta += 10
    case "m":
        conta += 15
    case "g":
        conta += 20

if pepperoni.lower() == "s":
    if tamanho.lower() == "s":
        conta += 5
    elif tamanho.lower() == "m":
        conta += 6
    else:
        conta += 7


if extra_queijo.lower() == "s":
    if tamanho.lower() == "s":
        conta += 3
    elif tamanho.lower() == "m":
        conta += 4
    else:
        conta += 5

print(f"Sua conta final deu {conta}, qual seria a forma de pagamento?")
print("Muito obrigado por pedir com a gente")
