# CREE UNA VARIABLE 'GLOBAL' PARA NO TENER QUE DECLARARLA EN CADA METODO
ok = False


def limpiarConsola():
    print('\n')


def menuConfirmacion(mensaje):
    opcion = input(mensaje + "\nPresione '1' para confirmar u otra tecla para cancelar.\n")

    while not opcion or opcion.isspace():
        print("ERROR. INTENTE NUEVAMENTE.")
        opcion = input("Presione '1' para confirmar u otra tecla para cancelar.\n")

    # UNA VEZ QUE TERMINA LA VERIFICACION, CASTEO OPCION A ENTERO PARA CONTINUAR
    if int(opcion) == 1:
        return True
    else:
        print("Cancelado por el usuario.")
        return False


# CREE UNA LISTA CON LOS DEPARTAMENTOS DEL GRAN MENDOZA PARA QUE EL USUARIO ELIJA
# ESTO LO HICE POR UNA CUESTION DE SIMPLICIDAD DEL PROGRAMA
def elegir_direccion():
    lista_direcciones = ["CIUDAD", "GODOY CRUZ", "GUAYMALLÉN", "LAS HERAS", "LUJÁN", "MAIPÚ"]

    while not ok:
        try:
            limpiarConsola()
            print("\nSELECCIONE SU DEPARTAMENTO:")
            print("1: CIUDAD\n2: GODOY CRUZ\n3: GUAYMALLÉN\n4: LAS HERAS\n5: LUJÁN\n6: MAIPÚ")
            opcion = int(input("\nIngrese el número de su departamento: "))

            while opcion < 1 or opcion > 6:
                opcion = int(
                    input("\nNúmero de departamento incorrecto.\nVuelva a ingresar el número de su departamento: "))

            #  SE LE RESTA 1 A LA LISTA PARA QUE COINCIDA CON LO QUE INGRESA EL USUARIO
            direccion = lista_direcciones[opcion - 1]

            print("\nLa dirección seleccionada es:", direccion)

            if menuConfirmacion("¿Es correcta la dirección?"):
                return direccion

        except ValueError:
            print("\nERROR. ESPACIO EN BLANCO.")


# LO QUE HACE ESTA FUNCION ES VERIFICAR QUE EL NOMBRE O APELLIDO INGRESADO NO SEA DEMASIADO LARGO O CONSISTA DE ESPACIOS EN BLANCO
# A SU VEZ PONE EN MAYUSCULA LA PRIMERA LETRA DE CADA PALABRA INGRESADA PARA EVITAR CONFUSIONES
def verificar_nombreApellido(nombre_apellido):
    while not ok:
        nombre = input("\nIngrese {}: ".format(nombre_apellido)).title()

        # VERIFICAR LONGITUD
        while len(nombre) <= 0 or len(nombre) > 30:
            nombre = input(
                "{} demasiado corto o largo.\nVuelva a ingresarlo: ".format(nombre_apellido.capitalize())).title()

        # VERIFICAR QUE NO CONTENGA ESPACIOS VACIOS
        while nombre.isspace():
            nombre = input("{} no puede contener espacios vacíos.\nVuelva a ingresarlo: ".format(
                nombre_apellido.capitalize())).title()

        print("\nUsted ha ingresado ", nombre)

        if menuConfirmacion("¿Es correcto el nombre ingresado?"):
            return nombre


def elegir_sexo():
    lista_sexos = ["MASCULINO", "FEMENINO", "INDEFINIDO"]

    while not ok:
        try:
            limpiarConsola()
            print("\nSELECCIONE SU SEXO:")
            print("1: MASCULINO\n2: FEMENINO\n3: INDEFINIDO")
            opcion = int(input("\nIngrese el número correspondiente a su sexo: "))

            while opcion < 1 or opcion > 3:
                opcion = int(
                    input("\nOpción incorrecta.\nVuelva a ingresar el número correspondiente a su sexo: "))

            #  SE LE RESTA 1 A LA LISTA PARA QUE COINCIDA CON LO QUE INGRESA EL USUARIO
            sexo = lista_sexos[opcion - 1]

            print("\nEl sexo elegido es:", sexo)

            if menuConfirmacion("¿Es correcto el sexo ingresado?"):
                return sexo

        except ValueError:
            print("\nERROR. ESPACIO EN BLANCO\n")
