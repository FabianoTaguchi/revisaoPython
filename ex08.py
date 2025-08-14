# Crie uma lista de preços com valores de produtos. Calcule a soma de todos os preços. Imprima o resultado final com a mensagem "O valor total da compra é: R$ [valor]" formatando o valor para duas casas decimais.

lista=[]
preco1 = float(input("Informe o primeiro valor da lista: "))
preco2 = float(input("Informe o segundo valor da lista: "))
preco3 = float(input("Informe o terceiro valor da lista: "))
preco4 = float(input("Informe o quarto valor da lista: "))

lista.append(preco1)
lista.append(preco2)
lista.append(preco3)
lista.append(preco4)

total = sum(lista)

print(f"O valor total da compra é: R${total:.2f}")