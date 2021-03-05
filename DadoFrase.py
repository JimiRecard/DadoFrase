import random, math
from word_list import word_list

rng = random.SystemRandom()
entropy_increment = math.log2(7776)


def DiceWord():
    a = ""
    for i in range(5):
        a += str(rng.randint(1, 6))
    print(a)

    return word_list.get(int(a))


password = ""
entropy = 0
first = True

for i in range(int(input("Informe a quantidade de palavras: "))):
    if first:
        password += DiceWord()
        first = False
    else:
        password += " " + DiceWord()
    entropy += entropy_increment
print(f'Sua senha é: "{password}"')
print(f"Sua senha possui {round(entropy,2)} bits de entropia")
