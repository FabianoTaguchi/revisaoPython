# Crie uma variável que receba um valor inteiro. Use um laço de repetição para imprimir a tabuada desse número, de 1 a 10

numero = int(input("Deseja que seja feit a tabuada de qual número? "))

print(f"Tabuada do {numero}:")
for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")