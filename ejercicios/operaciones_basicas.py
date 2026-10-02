print("Calculadora")
a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
if b != 0:
    print("División:", a / b)
else:
    print("No se puede dividir entre cero")