velocidade = float(input("Qual a velocidade do carro em km/h?" ))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Vocçe foi multado! O valor da multa é de R$ {:.2f} ".format(multa))
else:
    print("Você está dentro do limite de velocidaade. Dirija com segurança!")