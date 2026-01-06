x = input("Aperte x para comecar\n")

if x == "x":
    sobrenome_usuario = input("Digite seu sobrenome: \n")
    animal = input("Digite o nome do seu animal de estimacao: \n")

    print(f"Nome da sua banda: {sobrenome_usuario} {animal}")
    # print(f"Quantidade de characteres do sobrenome: {len(sobrenome_usuario)}")
    # print(f"Characteres cortados do sobrenome: {sobrenome_usuario[0:3]}")
else:
    print("tecla errada")
