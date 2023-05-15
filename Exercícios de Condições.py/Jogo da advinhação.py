"""import random
número_aleatório = random.randint(0,5)
palpite = int(input("Tente adivinhar o número que eu estou pensando (entre 0 e 5)"))

if palpite == número_aleatório:
    print("Parabéns! Você acertou o número!")
else:
    print("Que pena! O número que estava pensando era o {}. Tente novamente! ".format(número_aleatório))"""


from random import randint
from time import sleep
computador = randint(0,5) # faz com que o computador pense
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print("-=-" * 20)
jogador = int(input("Em que número eu pensei?")) # Jogador tenta adivinhar
print("PROCESSANDO....")
sleep(3)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(computador,jogador))

