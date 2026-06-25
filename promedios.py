print("Calculadora de Promedios")

notas_ingresadas = []

for i in range(3):
    nota_actual = float(input(f"Ingrese la nota {i+1}: "))
    notas_ingresadas.append(nota_actual)

promedio_final = sum(notas_ingresadas) / len(notas_ingresadas)

print(f"El promedio final es: {promedio_final:.2f}")