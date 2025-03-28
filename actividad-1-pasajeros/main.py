nombre = input ("Ingrese su nombre:")
pasajeros = int(input("Ingrese la cantidad de pasajeros:"))
acompañantes = pasajeros // 30 + 1
precio = 500 * (pasajeros + acompañantes)
print (f"El precio final es de: {precio}")
