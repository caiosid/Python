import math
ângulo = float(input("Digite o valor o ângulo em graus: "))
ânguloRadianos = math.radians(ângulo)

seno = math.sin(ânguloRadianos)
cosseno = math.cos(ânguloRadianos)
tangente = math.tan(ânguloRadianos)

print("O valor do {} é: ". format(seno))
print("O valor do {} é: ".format(cosseno))
print("O valor da {} é:".format(tangente))
