primeironúmero = int(input("Digite o primeiro número: "))
segundonúmero = int(input("Digite o segundo número: "))

if primeironúmero > segundonúmero:
    print("O primeiro valor é maior:")
elif segundonúmero > primeironúmero:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior. Os dois são iguais.")