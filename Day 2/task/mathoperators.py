def mathoperators():
    print(1 + 2)
    print(1 - 2)
    print(10 * 5)
    print(2**4)
    print(10 / 5)  # Divisao dessa forma sempre retorna um float
    print(10 // 5)  # Divisao dessa forma sempre retorna um int
    print(round(10 / 3, 2))

    # PEMDAS (Ordem de Prioridade)
    # Parenteses () -> Expoentes ** -> Multiplicacao/Divisao *,/ -> Add/Subtracao +,-
    print(3 * 3 + 3 / 3 - 3)
    print(3 * (3 + 3) / 3 - 3)

    bmi = 84 / 1.65**2
    print(bmi)

    print(round(bmi))

    print(round(bmi, 2))

    score = 0

    score += 1

    print(score)


mathoperators()
