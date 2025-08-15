
# Crie uma lista vazia. Use um laço de repetição para preencher essa lista com os primeiros 5 números pares (de 2 a 10). Ao final, imprima a lista.

numerosPares = []

for i in range(2, 11, 2):
    numerosPares.append(i)

print("Números pares na lista:")
print(numerosPares)