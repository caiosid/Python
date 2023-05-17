valorCasa = float(input("Digite o valor da casa: "))
salarioComprador = float(input("Digite o salário do comprador: "))
anosPagamento =  int(input("Digite em quantos anos será do comprador: "))

prestacaoMensal = valorCasa / (anosPagamento * 12)

if prestacaoMensal > (salarioComprador * 0.3):
    print("Emprestimo negado. A prestação excede 30% do salário.")
else:
    print("Empréstimo aprovado. Valor da {}: R$,".format(prestacaoMensal))