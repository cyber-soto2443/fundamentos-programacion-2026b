import math


def cuadrado():
    lado = float(input("Lado del cuadrado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print(f"Cuadrado -> área: {area}, perímetro: {perimetro}")


def rectangulo():
    base = float(input("Base del rectángulo: "))
    altura = float(input("Altura del rectángulo: "))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Rectángulo -> área: {area}, perímetro: {perimetro}")


def triangulo():
    base = float(input("Base del triángulo: "))
    altura = float(input("Altura del triángulo: "))
    lado1 = float(input("Longitud del lado 1: "))
    lado2 = float(input("Longitud del lado 2: "))
    area = (base * altura) / 2
    perimetro = base + lado1 + lado2
    print(f"Triángulo -> área: {area}, perímetro: {perimetro}")


def circulo():
    radio = float(input("Radio del círculo: "))
    area = math.pi * radio ** 2
    print(f"Círculo -> área: {area}")


def circunferencia():
    radio = float(input("Radio de la circunferencia: "))
    longitud = 2 * math.pi * radio
    print(f"Circunferencia -> longitud: {longitud}")


def main():
    print("Calculadora de áreas y perímetros")
    print("Seleccione la figura geométrica:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Circunferencia")

    opcion = int(input("Opción: "))

    if opcion == 1:
        cuadrado()
    elif opcion == 2:
        rectangulo()
    elif opcion == 3:
        circulo()
    elif opcion == 4:
        triangulo()
    elif opcion == 5:
        circunferencia()
    else:
        print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()