nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print("Média:", media)
    print("Reprovado")
elif media >= 5.0 and media <= 6.9:
    print("Média:", media)
    print("Recuperação")
else:
    print("Média:", media)
    print("Aprovado")
