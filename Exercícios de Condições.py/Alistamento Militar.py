from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Digite o ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade < 18:
    anosFaltantes = 18 - idade
    print("Você ainda vai se alistar ao serviço militar. Faltam {} anos".format(anosFaltantes))
elif idade == 18:
    print("É a hora de se alistar no serviço militar!")
else:
    anosPassados = idade - 18
    print("Já passou o tempo do alistamento. Passaram-se {} anos.".format(anosPassados))
