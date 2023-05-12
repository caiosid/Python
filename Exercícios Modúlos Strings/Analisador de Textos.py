#Lê o nome completo da pessoa 
nomecompleto = str(input("Digite seu nome compelto: "))
#Mostra o nome com todas as letras maiúsculas e minúsculas
print(" {} em letras maiúsculas: ".format(nomecompleto.upper()))
print("{} em letras maiúsculas: ".format(nomecompleto.lower()))
# Conta o número total de letras (sem considerar espaços)
númeroletras = str(len(nomecompleto(" "," ")))
print("{} total de letras (sem espaços): ".format(númeroletras))
#Conta o número de letras do primeiro nome
primeironome = nomecompleto.split()[0]
númeroletras_primeironome = len(primeironome)
print("{} de letras do primeiro nome: ".format(númeroletras_primeironome))



