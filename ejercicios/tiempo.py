print("1. Segundos a horas/minutos/segundos\n2. Horas, minutos y segundos a segundos")
opcion = int(input("Elige: "))
if opcion == 1:
    segundos = int(input("Segundos: "))
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    resto = segundos % 60
    print(f"{horas} horas, {minutos} minutos y {resto} segundos")
elif opcion == 2:
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    total = horas * 3600 + minutos * 60 + segundos
    print("Total:", total, "segundos")
else:
    print("Opción inválida")