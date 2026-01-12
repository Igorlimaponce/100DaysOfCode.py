# Nesse caso ele nao pega o 10, entao seria number >= 0. and number < 10

for number in range(0, 10):
    print(number)

print("\n\n")
for number in range(0, 10, 2):
    print(number)

soma = 0

for number in range(0, 101):
    soma += number

print(f"Soma = {soma}")
