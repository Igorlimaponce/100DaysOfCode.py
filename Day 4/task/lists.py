# lists sao data structures que armazenam varios valores em uma unica variavel
# listas sao mutaveis, ou seja, podemos alterar os valores dentro dela
# listas podem ter qualquer tipo de dados, podem ser so numerico, só string ou ambos misturados

# a ordem com que eu coloco os atributos dentro de uma lista se mantem, posso usar da mesma forma que foi declarado no futuro
frutas = ["maca", "banana"]

print(type(frutas))
print(frutas)
print(frutas[0])

for i, fruta in enumerate(frutas):
    if i == 0:
        frutas[i] = "pera"

    print(fruta)

print(frutas[0:2])

frutas.append("uva")

print(frutas[-1])

print(frutas)

frutas.extend(["abacaxi", "tomate"])

print(frutas)

import random


def friend_account():
    friends = ["joao", "ana", "murilo", "pedro", "lucas", "erica"]

    print("Hoje quem pagara a conta será: ")
    # print(friends[random.randint(0, 5)]) Essa é a primeira forma de fazer
    print(random.choice(friends))


friend_account()

# Também é possível criar listas aninhadas

vegetais = [
    "Avocados",
    "Sweet corn",
    "Cabbages",
    "Onions",
    "Sweet peas (frozen)",
    "Papayas",
]


frutas_e_vegetais = [frutas, vegetais]

print(frutas_e_vegetais)
print(frutas_e_vegetais[1][1])
