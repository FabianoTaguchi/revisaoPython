# Crie duas listas: primeiroNome e sobrenome. Crie uma variável nomeCompleto que combine o primeiro nome e o sobrenome de cada lista e imprima o resultado.

primeiroNome = ["João", "Ana", "Carlos"]
sobrenome = ["Silva", "Lima", "Souza"]

for i in range(len(primeiroNome)):
    print(f"{primeiroNome[i]} {sobrenome[i]}")