numero = int(input("Digite um número inteiro: "))
base = int(input("Escolha a base de conversão (1 - binário, 2 - octal, 3 - hexadecimal): "))

if base == 1:
    print("O número", numero, "em binário é:", bin(numero))
elif base == 2:
    print("O número", numero, "em octal é:", oct(numero))
elif base == 3:
    print("O número", numero, "em hexadecimal é:", hex(numero))
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")
