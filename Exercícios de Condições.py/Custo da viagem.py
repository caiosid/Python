distância = float(input("Qual é a distância da viagem em km?"))

if distância <= 200:
    preço = distância * 0.5
else:
    preço = distância * 0.45

    print("O preço da passagem é de R$ {:.2f}".format(preço))