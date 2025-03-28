boleteria = True
while(boleteria):
    opcion = int(input(
    '''
    Elija una funcion:
    1)Relatos Salvajes (600p)
    2)Esperando la Carroza (400p)
    3)El secreto de sus ojos (500p)
    4)Cerrar
    '''))
    if opcion == 4:
        boleteria = False
    elif opcion >= 5:
        print("No es una opcion")
        boleteria = False



        