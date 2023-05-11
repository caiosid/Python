from random import shuffle
número1 = str(input("Primeiro Aluno: "))
número2 = str(input("Segundo Aluno:  ")) 
núemro3 = str(input("Terceiro Aluno: ")) 
número4 = str(input("Quarto Aluno: "))

lista = [número1,número2,núemro3,número4]  
shuffle(lista)  
print("A ordem de apresentação será ") 
print(lista)
