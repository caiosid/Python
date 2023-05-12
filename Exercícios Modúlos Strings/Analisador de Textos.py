 
nomecompleto = str(input("Digite seu nome compelto: ")).strip()
print("Analisando seu nome...")
print(" O seu nome em letras maiúsculas é {}: ".format(nomecompleto.upper()))
print("O seu nome em letras maiúsculas é {}: ".format(nomecompleto.lower()))
print("A quantidade de letras do seu nome é {}:".format(len(nomecompleto) - nomecompleto.count(' ')))
#print("Seu primeiro nome tem {} letras".format(nomecompleto.find(' ')))
separa = nomecompleto.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))


