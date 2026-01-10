import random


def task_of_day():
    escolha = int(
        input("Oque voce escolhe? Digite 0 para pedra, 1 para papel e 2 para tesoura\n")
    )
    resultado(escolha)

    random_number = random.randint(0, 2)

    print("Computador Escolheu: ")
    resultado(random_number)

    if escolha == 0 and random_number == 1:
        print("Computador Ganhou")
    elif escolha == 0 and random_number == 2:
        print("Voce ganhou parabens")
    elif escolha == 1 and random_number == 0:
        print("Voce ganhou parabens")
    elif escolha == 1 and random_number == 2:
        print("Computador Ganhou")
    elif escolha == 2 and random_number == 1:
        print("Voce ganhou parabens")
    elif escolha == 2 and random_number == 0:
        print("Computador Ganhou")
    else:
        print("Empate")


def resultado(escolha):
    if escolha == 0:
        print(
            """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
        )
    elif escolha == 1:
        print(
            """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
        )
    elif escolha == 2:
        print(
            """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
        )
    else:
        print("Escolha impossivel -_-")
        task_of_day()


task_of_day()
