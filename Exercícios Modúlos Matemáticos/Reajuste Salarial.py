salário = float(input("Qual é o salário do funcionário?"))
novo = salário + (salário + 15 / 100)
print("Um funcionário que gnha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário,novo))