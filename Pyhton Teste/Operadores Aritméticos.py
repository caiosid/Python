numero1 = int(input("Um valor: "))
numero2 = int(input("Outro valor: "))
soma = numero1 + numero2
multiplicação = numero1 * numero2
divisão = numero1 / numero2
divisãoint = numero1 // numero2
expodenciação = numero1 ** numero2
print(" A soma é {}, \n o produto é {} e a \n divisão é {}".format(soma,multiplicação,divisão), end=" ")
print("Divisão inteira {} e potência {}".format(divisão,expodenciação))