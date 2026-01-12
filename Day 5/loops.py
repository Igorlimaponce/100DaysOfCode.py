frutas = ["maca", "banana", "laranja", "manga"]

for fruta in frutas:
    print(fruta)
    print(fruta + " pie")

students_score = [
    150,
    180,
    120,
    190,
    200,
    160,
    170,
    175,
    145,
    185,
    155,
    165,
    195,
    130,
    140,
    210,
    220,
    230,
    240,
    250,
    260,
    270,
    280,
    290,
    300,
    310,
]

high_score = students_score[0]
lower_score = students_score[0]


for score in students_score:
    if score > high_score:
        high_score = score

    if score < lower_score:
        lower_score = score

print(f"Maior numero = {high_score}")
print(f"Menor numero = {lower_score}")

soma = sum(students_score)

print(f"A soma dos scores é {soma}")

max_score = max(students_score)

print(f"O maior score é {max_score}")

lower_score = min(students_score)

print(f"O menor score é {lower_score}")
