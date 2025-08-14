# Crie uma lista de números vazia. Use um if-else para verificar se a lista está vazia. Se estiver, imprima "A lista está vazia." Caso contrário, imprima a quantidade de elementos na lista.

numeros = [12,23]

if len(numeros) == 0:
    print("A lista está vazia.")
else:
    print(f"A lista tem {len(numeros)} elementos.")