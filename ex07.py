# Crie uma lista chamada carrinho com alguns itens. Em seguida, adicione um novo item e remova um item já existente. Por fim, imprima a lista completa.

carrinho = ["leite", "pão", "ovos"]

item = str(input("Informe o nome de um produto a ser adicionado: "))
carrinho.append(item)

itemRemover = input("Informe o nome de um produto a ser removido: ")
if itemRemover in carrinho:
    carrinho.remove(itemRemover)
    print(f"O item {itemRemover} foi removido.")
else:
    print(f"O item {itemRemover} não está no carrinho.")

print("Itens no carrinho:")
print(carrinho)