import random
número_aleatório = random.randint(0,5)
palpite = int(input("Tente adivinhar o número que eu estou pensando (entre 0 e 5)"))

if palpite == número_aleatório:
    print("Parabéns! Você acertou o número!")
else:
    print("Que pena! O número que estava pensando era o {}. Tente novamente! ".format(número_aleatório))