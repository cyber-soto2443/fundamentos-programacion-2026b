print("1. Celsius a Fahrenheit\n2. Kilómetros a millas\n3. Dólares a pesos\n4. Kilogramos a libras")
opcion = int(input("Elige: "))
valor = float(input("Cantidad: "))
if opcion == 1:
    print("Resultado:", valor * 9 / 5 + 32)
elif opcion == 2:
    print("Resultado:", valor * 0.621371)
elif opcion == 3:
    tasa = float(input("Tasa por dólar: "))
    print("Resultado:", valor * tasa)
elif opcion == 4:
    print("Resultado:", valor * 2.20462)
else:
    print("Opción inválida")