xs = []

for i in range(5):
    temp = float(input(f"Informe a temperatura do {i+1}º dia em °C: "))
    xs.append(temp)

maior = xs[0]
menor = xs[0]

# Verifica maior e menor
for x in xs:
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(f"A maior temperatura registrada foi: {maior}°C")
print(f"A menor temperatura registrada foi: {menor}°C")
