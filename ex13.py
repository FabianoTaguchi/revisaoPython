
numero = int(input("Deseja que seja feit a tabuada de qual número? "))

print(f"Tabuada do {numero}:")
for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")