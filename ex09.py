# Crie três variáveis de string: nome, sobrenome e idade. Concatene-as para formar uma única frase e imprima o resultado.

nome = input("Qual seu nome? ") 
sobrenome = input("Qual seu sobrenome: ")
idade = int(input("Qual sua idade? "))

fraseCompleta = f"Olá, seu nome é {nome} {sobrenome} e você tem {idade} anos."

print(fraseCompleta)