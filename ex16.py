# Crie uma lista com alguns valores do histórico de temperatura de uma cidade. Use um laço de repetição para encontrar a maior e a menor temperatura na lista. Imprima os resultados formatados.

temperatura = []
continuar = "S"

while continuar.upper() == "S":
    temp = float(input("Informe a temperatura em °C: "))
    temperatura.append(temp)
    continuar = input("Deseja informar outra temperatura? (S/N): ")

# Inicializa maior e menor com o primeiro valor informado
maior = temperatura[0]
menor = temperatura[0]

# Verifica maior e menor
for x in temperatura:
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(f"\nA maior temperatura registrada foi: {maior}°C")
print(f"A menor temperatura registrada foi: {menor}°C")
