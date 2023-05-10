from math import sqrt
catetoOposto = float(input("Digite o comprimento do cateto oposto"))
catetoAdjacente = float(input("Digite o comprimento do cateto adjacente"))

hipotenusa = sqrt(catetoOposto ** 2 +  catetoAdjacente ** 2 )

print("O comprimento da {} é: ".format(hipotenusa))